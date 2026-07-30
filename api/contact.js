// api/contact.js
// Vercel Serverless Function to securely handle contact submissions & subscriptions via Resend
// Trigger Vercel rebuild (Updated receiver to info@family1stlegacy.com)

export default async function handler(req, res) {
  // CORS Headers
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
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

  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    console.error("Missing RESEND_API_KEY environment variable.");
    return res.status(500).json({ error: "Server configuration error. Missing API key." });
  }

  const receiverEmail = process.env.CONTACT_RECEIVER_EMAIL || 'info@family1stlegacy.com';

  try {
    // Parse request body
    let body = {};
    if (typeof req.body === 'string') {
      body = JSON.parse(req.body);
    } else {
      body = req.body;
    }

    const { firstName, lastName, email, phone, state, service, message, type } = body;

    // Determine submission type (Subscription vs Consultation Form)
    const isSubscription = type === 'subscription' || (!firstName && email);

    if (isSubscription) {
      if (!email) {
        return res.status(400).json({ error: "Missing email address for newsletter subscription." });
      }

      const emailSubject = `New Newsletter Subscription: ${email}`;
      const emailHtml = `
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; background-color: #fcfcfd;">
          <h2 style="color: #4A2D7A; border-bottom: 2px solid #4A2D7A; padding-bottom: 10px; margin-top: 0;">New Newsletter Subscription</h2>
          <p style="font-size: 16px; color: #333;">A visitor has subscribed to the newsletter on the Family First Legacy website.</p>
          
          <table style="width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 14px;">
            <tr style="background-color: #f8fafc;">
              <td style="padding: 10px; font-weight: bold; width: 150px; border-bottom: 1px solid #e2e8f0;">Email Address:</td>
              <td style="padding: 10px; border-bottom: 1px solid #e2e8f0;"><a href="mailto:${email}">${email}</a></td>
            </tr>
          </table>

          <p style="font-size: 12px; color: #777; margin-top: 30px; border-top: 1px solid #e2e8f0; padding-top: 10px; text-align: center;">
            Sent securely from the Family First Legacy Vercel Serverless Form handler.
          </p>
        </div>
      `;

      // Send to Resend
      const resendResponse = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          from: 'Family First Legacy <onboarding@resend.dev>',
          to: [receiverEmail],
          subject: emailSubject,
          html: emailHtml,
          reply_to: email
        })
      });

      const resendResult = await resendResponse.json();

      if (!resendResponse.ok) {
        console.error("Resend API Error (Subscription):", resendResult);
        return res.status(resendResponse.status).json({ error: resendResult.message || "Failed to send email." });
      }

      return res.status(200).json({ success: true, messageId: resendResult.id });

    } else {
      // Consultation Request
      if (!firstName || !lastName || !email || !phone) {
        return res.status(400).json({ error: "Missing required contact details (first name, last name, email, phone)." });
      }

      const emailSubject = `New Lead Form: ${firstName} ${lastName} (${service || 'General Inquiry'})`;
      const emailHtml = `
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; background-color: #fcfcfd;">
          <h2 style="color: #4A2D7A; border-bottom: 2px solid #4A2D7A; padding-bottom: 10px; margin-top: 0;">New Consultation Request</h2>
          <p style="font-size: 16px; color: #333;">A new lead has submitted a request on the Family First Legacy website.</p>
          
          <table style="width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 14px;">
            <tr style="background-color: #f8fafc;">
              <td style="padding: 10px; font-weight: bold; width: 150px; border-bottom: 1px solid #e2e8f0;">First Name:</td>
              <td style="padding: 10px; border-bottom: 1px solid #e2e8f0;">${firstName}</td>
            </tr>
            <tr>
              <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #e2e8f0;">Last Name:</td>
              <td style="padding: 10px; border-bottom: 1px solid #e2e8f0;">${lastName}</td>
            </tr>
            <tr style="background-color: #f8fafc;">
              <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #e2e8f0;">Email Address:</td>
              <td style="padding: 10px; border-bottom: 1px solid #e2e8f0;"><a href="mailto:${email}">${email}</a></td>
            </tr>
            <tr>
              <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #e2e8f0;">Phone Number:</td>
              <td style="padding: 10px; border-bottom: 1px solid #e2e8f0;"><a href="tel:${phone}">${phone}</a></td>
            </tr>
            <tr style="background-color: #f8fafc;">
              <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #e2e8f0;">State of Residence:</td>
              <td style="padding: 10px; border-bottom: 1px solid #e2e8f0;">${state || 'Not specified'}</td>
            </tr>
            <tr>
              <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #e2e8f0;">Service Selection:</td>
              <td style="padding: 10px; border-bottom: 1px solid #e2e8f0;"><strong>${service || 'General Inquiry'}</strong></td>
            </tr>
          </table>

          <div style="margin-top: 25px; padding: 15px; background-color: #f1ecf7; border-left: 4px solid #4A2D7A; border-radius: 4px;">
            <p style="margin: 0; font-weight: bold; color: #4A2D7A; font-size: 14px;">User Message:</p>
            <p style="margin: 10px 0 0 0; font-size: 14px; color: #333; line-height: 1.5; white-space: pre-wrap;">${message || 'No message provided.'}</p>
          </div>

          <p style="font-size: 12px; color: #777; margin-top: 30px; border-top: 1px solid #e2e8f0; padding-top: 10px; text-align: center;">
            Sent securely from the Family First Legacy Vercel Serverless Form handler.
          </p>
        </div>
      `;

      // Send to Resend
      const resendResponse = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          from: 'Family First Legacy <onboarding@resend.dev>',
          to: [receiverEmail],
          subject: emailSubject,
          html: emailHtml,
          reply_to: email
        })
      });

      const resendResult = await resendResponse.json();

      if (!resendResponse.ok) {
        console.error("Resend API Error (Lead):", resendResult);
        return res.status(resendResponse.status).json({ error: resendResult.message || "Failed to send email." });
      }

      return res.status(200).json({ success: true, messageId: resendResult.id });
    }

  } catch (error) {
    console.error("Serverless Function Error:", error);
    return res.status(500).json({ error: "Internal server error occurred." });
  }
}
