// api/unsubscribe.js
// Vercel Serverless Function to handle click-to-unsubscribe requests

export default async function handler(req, res) {
  // CORS Headers
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,POST');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // Get email from query parameter
  const { email } = req.query;

  if (!email) {
    return renderHtmlResponse(res, false, "Invalid unsubscribe link. Missing email parameter.");
  }

  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseKey = process.env.SUPABASE_ANON_KEY;

  if (!supabaseUrl || !supabaseKey) {
    console.error("Missing Supabase configuration.");
    return renderHtmlResponse(res, false, "Server configuration error. Please try again later.");
  }

  try {
    // Call Supabase REST API to update subscriber status to 'unsubscribed'
    const response = await fetch(`${supabaseUrl}/rest/v1/subscribers?email=eq.${encodeURIComponent(email)}`, {
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

    if (!response.ok) {
      const errorData = await response.json();
      console.error("Supabase Error during unsubscribe:", errorData);
      return renderHtmlResponse(res, false, "Could not find your email in our newsletter subscription list.");
    }

    const data = await response.json();

    if (data.length === 0) {
      return renderHtmlResponse(res, false, "This email is not currently subscribed to our newsletter.");
    }

    return renderHtmlResponse(res, true, `The email <strong>${email}</strong> has been successfully unsubscribed from all future communications.`, email);

  } catch (error) {
    console.error("Unsubscribe handler error:", error);
    return renderHtmlResponse(res, false, "An unexpected error occurred. Please try again later.");
  }
}

function renderHtmlResponse(res, success, message, email = '') {
  res.setHeader('Content-Type', 'text/html');
  
  const title = success ? "Successfully Unsubscribed" : "Unsubscribe Error";
  const icon = success 
    ? `<svg style="width: 64px; height: 64px; color: #f59e0b; margin-bottom: 24px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`
    : `<svg style="width: 64px; height: 64px; color: #ef4444; margin-bottom: 24px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>`;

  const html = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>${title} | Family First Legacy</title>
      <link rel="icon" type="image/png" href="/images/FamilyFirstLogo.png">
      <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
      <style>
        :root {
          --dark: #0d1117;
          --light: #f8fafc;
          --purple: #4A2D7A;
          --purple-light: #6b46a1;
          --amber: #f59e0b;
        }
        body {
          margin: 0;
          padding: 0;
          font-family: 'Plus Jakarta Sans', sans-serif;
          background: radial-gradient(circle at top, #1e1333 0%, #0d0a14 100%);
          color: #ffffff;
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 24px;
          box-sizing: border-box;
        }
        .container {
          background: rgba(255, 255, 255, 0.03);
          border: 1px solid rgba(255, 255, 255, 0.08);
          backdrop-filter: blur(20px);
          -webkit-backdrop-filter: blur(20px);
          max-width: 480px;
          width: 100%;
          border-radius: 24px;
          padding: 48px 32px;
          text-align: center;
          box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        }
        .logo {
          height: 48px;
          margin-bottom: 32px;
        }
        h1 {
          font-family: 'Outfit', sans-serif;
          font-size: 28px;
          font-weight: 700;
          margin: 0 0 16px 0;
          letter-spacing: -0.5px;
        }
        p {
          font-size: 16px;
          color: rgba(255, 255, 255, 0.7);
          line-height: 1.6;
          margin: 0 0 32px 0;
        }
        strong {
          color: var(--amber);
        }
        .btn {
          display: inline-block;
          background: linear-gradient(135deg, var(--purple) 0%, var(--purple-light) 100%);
          color: #ffffff;
          text-decoration: none;
          padding: 14px 28px;
          border-radius: 12px;
          font-weight: 600;
          font-size: 16px;
          transition: all 0.3s ease;
          border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .btn:hover {
          transform: translateY(-2px);
          box-shadow: 0 8px 20px rgba(107, 70, 161, 0.3);
          border-color: rgba(255, 255, 255, 0.2);
        }
        .footer {
          margin-top: 32px;
          font-size: 12px;
          color: rgba(255, 255, 255, 0.4);
        }
      </style>
    </head>
    <body>
      <div class="container">
        <a href="https://family1stlegacy.com">
          <img class="logo" src="https://family1stlegacy.com/images/FamilyFirstLogo.png" alt="Family First Legacy">
        </a>
        ${icon}
        <h1>${title}</h1>
        <p>${message}</p>
        <a href="https://family1stlegacy.com" class="btn">Return to Website</a>
        <div class="footer">
          © ${new Date().getFullYear()} Family First Legacy. All rights reserved.
        </div>
      </div>
    </body>
    </html>
  `;
  
  return res.status(200).send(html);
}
