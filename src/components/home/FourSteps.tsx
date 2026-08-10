"use client";

import React from "react";

interface FourStepsProps {
  lang: "en" | "es";
}

export default function FourSteps({ lang }: FourStepsProps) {
  const isEs = lang === "es";

  return (
    <section id="process">
      <div className="container">
        <div className="process-header">
          <p className="t-label" style={{ justifyContent: "center", display: "flex", alignItems: "center", gap: "8px" }}>
            <span className="green-dot"></span>
            {isEs ? "Cómo funciona" : "How It Works"}
          </p>
          <h2 className="t-h1" style={{ marginTop: "16px" }}>
            {isEs ? (
              <>Cuatro pasos para la<br />claridad financiera</>
            ) : (
              <>Four Steps to<br />Financial Clarity</>
            )}
          </h2>
          <p>{isEs ? "Hacemos que las conversaciones financieras sean sencillas, honestas y personales." : "We make financial conversations simple, honest, and personal."}</p>
        </div>

        <div className="process-steps">
          {/* Step 1 */}
          <div className="ps">
            <div className="ps-photo-wrap">
              <div
                className="ps-photo"
                style={{ backgroundImage: "url('https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=600&q=80')" }}
              ></div>
            </div>
            <div className="ps-num">01</div>
            <div className="ps-content">
              <div className="ps-step-label">{isEs ? "Paso uno" : "Step One"}</div>
              <div className="ps-title">{isEs ? "Llamada de descubrimiento" : "Discovery Call"}</div>
              <div className="ps-body">
                {isEs
                  ? "Una conversación sin compromiso para comprender a su familia, sus metas y su situación financiera actual, sin costo alguno."
                  : "A no-obligation conversation to understand your family, your goals, and where you stand financially — at no cost."}
              </div>
              <div className="ps-duration">
                <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><polyline points="12 6 12 12 16 14" /></svg>
                <span>30 minutes</span>
              </div>
            </div>
          </div>

          {/* Step 2 */}
          <div className="ps">
            <div className="ps-photo-wrap">
              <div
                className="ps-photo"
                style={{ backgroundImage: "url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80')" }}
              ></div>
            </div>
            <div className="ps-num">02</div>
            <div className="ps-content">
              <div className="ps-step-label">{isEs ? "Paso dos" : "Step Two"}</div>
              <div className="ps-title">{isEs ? "Entienda sus necesidades" : "Understand Your Needs"}</div>
              <div className="ps-body">
                {isEs
                  ? "Utilizamos un análisis de necesidades financieras para revisar su panorama actual y ayudar a identificar dónde pueden encajar las opciones de protección o ahorro."
                  : "We use a Financial Needs Analysis to review your current picture and help identify where protection, savings, or retirement options may fit your needs."}
              </div>
              <div className="ps-duration">
                <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><polyline points="12 6 12 12 16 14" /></svg>
                <span>45–60 minutes</span>
              </div>
            </div>
          </div>

          {/* Step 3 */}
          <div className="ps">
            <div className="ps-photo-wrap">
              <div
                className="ps-photo"
                style={{ backgroundImage: "url('https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=600&q=80')" }}
              ></div>
            </div>
            <div className="ps-num">03</div>
            <div className="ps-content">
              <div className="ps-step-label">{isEs ? "Paso tres" : "Step Three"}</div>
              <div className="ps-title">{isEs ? "Sus opciones personalizadas" : "Your Personalized Options"}</div>
              <div className="ps-body">
                {isEs
                  ? "Presentamos opciones claras de compañías de servicios financieros bien establecidas, explicadas en un lenguaje sencillo y sin presión."
                  : "We present clear options from well-established insurance and financial services companies — explained in simple language, with no pressure."}
              </div>
              <div className="ps-duration">
                <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><polyline points="12 6 12 12 16 14" /></svg>
                <span>1 week follow-up</span>
              </div>
            </div>
          </div>

          {/* Step 4 */}
          <div className="ps">
            <div className="ps-photo-wrap">
              <div
                className="ps-photo"
                style={{ backgroundImage: "url('https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=600&q=80')" }}
              ></div>
            </div>
            <div className="ps-num">04</div>
            <div className="ps-content">
              <div className="ps-step-label">{isEs ? "En curso" : "Ongoing"}</div>
              <div className="ps-title">{isEs ? "Orientación continua" : "Ongoing Guidance"}</div>
              <div className="ps-body">
                {isEs
                  ? "La vida cambia y su plan puede necesitar cambiar con ella. Permanecemos disponibles para revisar su plan y responder preguntas a medida que su familia crece."
                  : "Life changes — and your plan may need to change with it. We stay available to review your plan, answer questions, and help you adjust as your family grows."}
              </div>
              <div className="ps-duration">
                <svg viewBox="0 0 24 24"><path d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" /></svg>
                <span>Support over time</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
