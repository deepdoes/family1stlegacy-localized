"use client";

import React, { useState } from "react";
import { Send, CheckCircle2 } from "lucide-react";

interface ContactFormProps {
  lang: "en" | "es";
}

export default function ContactForm({ lang }: ContactFormProps) {
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);
  const isEs = lang === "es";

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    // Simulate submission delay
    await new Promise((resolve) => setTimeout(resolve, 800));
    setLoading(false);
    setSubmitted(true);
  };

  return (
    <section id="contact" className="py-24 bg-white border-t border-gray-100">
      <div className="max-w-4xl mx-auto px-6 md:px-12">
        <div className="bg-gradient-to-br from-[#3A2060] to-[#201238] rounded-3xl p-8 md:p-14 text-white shadow-2xl relative overflow-hidden">
          <div className="max-w-2xl mx-auto text-center relative z-10">
            <span className="text-xs font-bold tracking-[3px] text-amber-300 uppercase block mb-3">
              {isEs ? "CONSULTA GRATUITA" : "FREE CONSULTATION"}
            </span>
            <h2 className="text-3xl md:text-5xl font-extrabold text-white leading-tight mb-4">
              {isEs ? "Hablemos de lo que más importa" : "Let’s Talk About What Matters Most"}
            </h2>
            <p className="text-white/80 text-base font-light mb-10 leading-relaxed">
              {isEs
                ? "Programa una revisión gratuita de 15 minutos sin ningún compromiso. Escuchamos tus metas y te explicamos tus opciones con claridad."
                : "Schedule a complimentary 15-minute review with no obligation. We listen to your goals and explain your options clearly."}
            </p>

            {submitted ? (
              <div className="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl p-8 text-center animate-in fade-in">
                <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-4" />
                <h3 className="text-2xl font-bold text-white mb-2">
                  {isEs ? "¡Gracias por contactarnos!" : "Thank You for Reaching Out!"}
                </h3>
                <p className="text-white/80 text-sm">
                  {isEs
                    ? "Un profesional de Family First Legacy se comunicará contigo pronto."
                    : "A Family First Legacy professional will reach out to you shortly."}
                </p>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className="flex flex-col gap-4 text-left">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <input
                    type="text"
                    required
                    placeholder={isEs ? "Tu nombre completo" : "Your Full Name"}
                    className="w-full bg-white/10 border border-white/20 rounded-xl px-4 py-3.5 text-white placeholder:text-white/50 focus:outline-none focus:border-amber-300 text-sm"
                  />
                  <input
                    type="email"
                    required
                    placeholder={isEs ? "Tu correo electrónico" : "Your Email Address"}
                    className="w-full bg-white/10 border border-white/20 rounded-xl px-4 py-3.5 text-white placeholder:text-white/50 focus:outline-none focus:border-amber-300 text-sm"
                  />
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <input
                    type="tel"
                    required
                    placeholder={isEs ? "Número de teléfono" : "Phone Number"}
                    className="w-full bg-white/10 border border-white/20 rounded-xl px-4 py-3.5 text-white placeholder:text-white/50 focus:outline-none focus:border-amber-300 text-sm"
                  />
                  <select
                    className="w-full bg-[#201238] border border-white/20 rounded-xl px-4 py-3.5 text-white focus:outline-none focus:border-amber-300 text-sm"
                  >
                    <option value="">{isEs ? "Selecciona un servicio" : "Select a Service"}</option>
                    <option value="family-protection">{isEs ? "Protección familiar" : "Family Protection"}</option>
                    <option value="retirement">{isEs ? "Planificación de jubilación" : "Retirement Planning"}</option>
                    <option value="education">{isEs ? "Planificación educativa" : "Education Planning"}</option>
                    <option value="estate">{isEs ? "Planificación de legado" : "Estate & Legacy Planning"}</option>
                    <option value="business">{isEs ? "Estrategias para negocios" : "Business Strategies"}</option>
                    <option value="opportunity">{isEs ? "Oportunidad de carrera" : "Career Opportunity"}</option>
                  </select>
                </div>
                <textarea
                  rows={3}
                  placeholder={isEs ? "¿En qué podemos ayudarte hoy?" : "How can we help you today?"}
                  className="w-full bg-white/10 border border-white/20 rounded-xl px-4 py-3.5 text-white placeholder:text-white/50 focus:outline-none focus:border-amber-300 text-sm"
                />

                <button
                  type="submit"
                  disabled={loading}
                  className="bg-amber-400 hover:bg-amber-300 text-gray-950 font-bold py-4 rounded-xl text-sm transition-all shadow-lg flex items-center justify-center gap-2 mt-2"
                >
                  {loading ? (
                    <span>{isEs ? "Enviando..." : "Submitting..."}</span>
                  ) : (
                    <>
                      <span>{isEs ? "Solicitar consulta gratuita" : "Request Free Consultation"}</span>
                      <Send className="w-4 h-4" />
                    </>
                  )}
                </button>
              </form>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}
