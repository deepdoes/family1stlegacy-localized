// api/receive-email.js
// Vercel Serverless Function to process inbound catchall emails from Resend
// Automatically processes unsubscribe requests (replies) and forwards all emails to admins

export default async function handler(req, res) {
  // CORS Headers
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST,OPTIONS');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const resendApiKey = process.env.RESEND_API_KEY;
  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseKey = process.env.SUPABASE_ANON_KEY;

  if (!resendApiKey) {
    console.error("Missing RESEND_API_KEY environment variable.");
    return res.status(500).json({ error: "Server configuration error." });
  }

  const receiverEmail = process.env.CONTACT_RECEIVER_EMAIL || 'andresindayi@gmail.com';
  const ccEmail = process.env.CONTACT_CC_EMAIL || 'dfwbranding@gmail.com';

  try {
    // Parse request body
    let body = {};
    if (typeof req.body === 'string') {
      body = JSON.parse(req.body);
    } else {
      body = req.body;
    }

    const { from, to, subject, html, text } = body;

    if (!from || !to) {
      console.warn("Received inbound email missing from or to field:", body);
      return res.status(400).json({ error: "Missing from or to fields" });
    }

    // Extract sender email address
    // Format is usually "Name <email@example.com>" or "email@example.com"
    const senderEmailMatch = from.match(/<([^>]+)>/);
    const senderEmail = senderEmailMatch ? senderEmailMatch[1].trim() : from.trim();

    // Check if the reply is an unsubscribe request
    const checkSubject = (subject || "").toLowerCase();
    const checkBody = (text || html || "").toLowerCase();
    
    const isUnsubscribeRequest = 
      checkSubject.includes("unsubscribe") || 
      checkBody === "unsubscribe" || 
      checkBody.startsWith("unsubscribe\n") || 
      checkBody.startsWith("unsubscribe\r");

    if (isUnsubscribeRequest && supabaseUrl && supabaseKey) {
      console.log(`Processing auto-unsubscribe for: ${senderEmail}`);

      // Update Supabase to 'unsubscribed'
      const dbResponse = await fetch(`${supabaseUrl}/rest/v1/subscribers?email=eq.${encodeURIComponent(senderEmail)}`, {
        method: 'PATCH',
        headers: {
          'apikey': supabaseKey,
          'Authorization': `Bearer ${supabaseKey}`,
          'Content-Type': 'application/json',
          'Prefer': 'return=representation'
        },
        body: JSON.stringify({
          status: 'unsubscribed',
          unsubscribed_at: new Date().toISOString()
        })
      });

      let unsubscribeAlertHtml = "";

      if (dbResponse.ok) {
        const dbData = await dbResponse.json();
        if (dbData.length > 0) {
          unsubscribeAlertHtml = `
            <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px; background-color: #f8fafc;">
              <h2 style="color: #f59e0b; margin-top: 0;">Automated Unsubscribe Completed</h2>
              <p>The user <strong>${senderEmail}</strong> replied "unsubscribe" to your email.</p>
              <p><strong>Status:</strong> Successfully updated in your Supabase database.</p>
            </div>
          `;
        } else {
          unsubscribeAlertHtml = `
            <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px; background-color: #f8fafc;">
              <h2 style="color: #64748b; margin-top: 0;">Unsubscribe Reply Received (Not Subscribed)</h2>
              <p>The user <strong>${senderEmail}</strong> replied "unsubscribe", but their email was not found in your subscribers database.</p>
            </div>
          `;
        }
      } else {
        const errText = await dbResponse.text();
        console.error("Failed to update unsubscribe status in DB:", errText);
        unsubscribeAlertHtml = `
          <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #ef4444; border-radius: 8px; background-color: #fef2f2;">
            <h2 style="color: #ef4444; margin-top: 0;">Unsubscribe database update failed</h2>
            <p>The user <strong>${senderEmail}</strong> replied "unsubscribe" but the database update encountered an error.</p>
            <p>Error details: ${errText}</p>
            <p>Please update their status manually in the Supabase dashboard.</p>
          </div>
        `;
      }

      // Send the unsubscribe notification alert to the admins
      await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${resendApiKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          from: 'Family First Legacy <leads@family1stlegacy.com>',
          to: [receiverEmail],
          cc: ccEmail ? [ccEmail] : undefined,
          subject: `[Unsubscribe] Request from ${senderEmail}`,
          html: unsubscribeAlertHtml,
          reply_to: senderEmail
        })
      });

      return res.status(200).json({ success: true, type: 'unsubscribe_processed' });
    }

    // Normal Catchall email forwarding logic
    const forwardSubject = `[Inbound] ${subject || '(No Subject)'} (to ${to})`;
    const forwardHtml = `
      <div style="font-family: sans-serif; font-size: 14px; background-color: #f1f5f9; padding: 16px; border: 1px solid #cbd5e1; border-radius: 8px; margin-bottom: 24px; color: #334155;">
        <strong style="color: #4A2D7A; font-size: 16px;">Forwarded Catchall Email</strong><br>
        <hr style="border: 0; border-top: 1px solid #cbd5e1; margin: 10px 0;">
        <strong>From:</strong> ${from}<br>
        <strong>To:</strong> ${to}<br>
        <strong>Subject:</strong> ${subject || '(No Subject)'}<br>
        <strong>Date Received:</strong> ${new Date().toLocaleString('en-US', { timeZone: 'America/Chicago' })} CST
      </div>
      <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #1e293b;">
        ${html || (text ? text.replace(/\n/g, '<br>') : '(No body content)')}
      </div>
    `;

    // Forward to admins via Resend API
    const forwardResponse = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${resendApiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: 'Family First Legacy <leads@family1stlegacy.com>',
        to: [receiverEmail],
        cc: ccEmail ? [ccEmail] : undefined,
        subject: forwardSubject,
        html: forwardHtml,
        reply_to: senderEmail
      })
    });

    const forwardResult = await forwardResponse.json();

    if (!forwardResponse.ok) {
      console.error("Resend Forwarding Error:", forwardResult);
      return res.status(forwardResponse.status).json({ error: forwardResult.message || "Failed to forward email." });
    }

    return res.status(200).json({ success: true, forwarded: true, messageId: forwardResult.id });

  } catch (error) {
    console.error("Inbound handler error:", error);
    return res.status(500).json({ error: "Internal server error" });
  }
}
