"use client";

import React from "react";

interface NumbersBandProps {
  lang?: "en" | "es";
}

export default function NumbersBand({ lang = "en" }: NumbersBandProps) {
  const isEs = lang === "es";

  return (
    <section id="numbers">
      <div className="container-full">
        <div className="numbers-grid">
          <div className="number-item">
            <div className="ni-num">{isEs ? "EDUCACIÓN PRIMERO" : "EDUCATION FIRST"}</div>
            <div className="ni-label">{isEs ? "Explicaciones claras antes de tomar decisiones" : "Clear explanations before decisions"}</div>
          </div>
          <div className="number-item">
            <div className="ni-num">{isEs ? "ORIENTACIÓN 1 A 1" : "1-ON-1 GUIDANCE"}</div>
            <div className="ni-label">{isEs ? "Apoyo personal que comienza escuchando" : "Personal support that starts with listening"}</div>
          </div>
          <div className="number-item">
            <div className="ni-num">{isEs ? "LA FAMILIA PRIMERO" : "FAMILY FOCUSED"}</div>
            <div className="ni-label">{isEs ? "Planificación centrada en las personas que amas" : "Planning around the people you love"}</div>
          </div>
          <div className="number-item">
            <div className="ni-num">{isEs ? "ORIENTACIÓN DE PROFESIONALES CON LICENCIA" : "LICENSED GUIDANCE"}</div>
            <div className="ni-label">{isEs ? "Profesionales que explican antes de recomendar" : "Professionals who explain before recommending"}</div>
          </div>
        </div>
      </div>
    </section>
  );
}
