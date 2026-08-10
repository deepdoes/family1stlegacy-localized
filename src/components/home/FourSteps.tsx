"use client";

import React from "react";
import Link from "next/link";
import { ArrowRight, Clock } from "lucide-react";

interface FourStepsProps {
  lang: "en" | "es";
}

export default function FourSteps({ lang }: FourStepsProps) {
  const isEs = lang === "es";

  const stepsEn = [
    {
      num: "STEP ONE",
      title: "Discovery Call",
      desc: "A no-obligation conversation to understand your family, your goals, and where you stand financially — at no cost.",
      time: "30 minutes",
    },
    {
      num: "STEP TWO",
      title: "Understand Your Needs",
      desc: "We use a Financial Needs Analysis to review your current picture and help identify where protection, savings, or retirement options may fit your needs.",
      time: "45–60 minutes",
    },
    {
      num: "STEP THREE",
      title: "Your Personalized Options",
      desc: "We present clear options from well-established insurance and financial services companies — explained in simple language, with no pressure.",
      time: "1 week follow-up",
    },
    {
      num: "ONGOING",
      title: "Ongoing Guidance",
      desc: "Life changes — and your plan may need to change with it. We stay available to review your plan, answer questions, and help you adjust as your family grows.",
      time: "Support over time",
    },
  ];

  const stepsEs = [
    {
      num: "PASO UNO",
      title: "Llamada de descubrimiento",
      desc: "Una conversación sin compromiso para entender a tu familia, tus metas y tu situación financiera actual, sin costo.",
      time: "30 minutos",
    },
    {
      num: "PASO DOS",
      title: "Entender tus necesidades",
      desc: "Utilizamos un Análisis de Necesidades Financieras para revisar tu panorama actual e identificar dónde pueden ajustarse opciones de protección o jubilación.",
      time: "45–60 minutos",
    },
    {
      num: "PASO TRES",
      title: "Tus opciones personalizadas",
      desc: "Presentamos opciones claras de compañías de seguros y servicios financieros bien establecidas, explicadas en lenguaje sencillo y sin presión.",
      time: "Seguimiento de 1 semana",
    },
    {
      num: "CONTINUO",
      title: "Orientación continua",
      desc: "La vida cambia y tu plan puede necesitar cambiar con ella. Nos mantenemos disponibles para revisar tu plan y ayudarte a hacer ajustes a medida que tu familia crece.",
      time: "Apoyo continuo",
    },
  ];

  const steps = isEs ? stepsEs : stepsEn;

  return (
    <section id="process" className="py-24 bg-white border-t border-gray-100">
      <div className="max-w-7xl mx-auto px-6 md:px-12">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <span className="text-xs font-bold tracking-[3px] text-purple-900 uppercase block mb-3">
            {isEs ? "NUESTRO PROCESO" : "OUR PROCESS"}
          </span>
          <h2 className="text-3xl md:text-5xl font-extrabold text-gray-900 leading-tight mb-4">
            {isEs ? "4 pasos hacia la claridad financiera" : "Four Steps to Financial Clarity"}
          </h2>
          <p className="text-base text-gray-600 font-light leading-relaxed">
            {isEs
              ? "Hacemos que las conversaciones financieras sean sencillas, honestas y personales."
              : "We make financial conversations simple, honest, and personal."}
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {steps.map((step, idx) => (
            <div
              key={idx}
              className="bg-purple-50/50 border border-purple-100 rounded-3xl p-8 flex flex-col justify-between hover:shadow-lg transition-all duration-300 relative"
            >
              <div>
                <div className="flex justify-between items-center mb-4">
                  <span className="text-xs font-bold tracking-wider text-purple-900 uppercase">
                    {step.num}
                  </span>
                  <span className="inline-flex items-center gap-1 text-[11px] bg-purple-900/10 text-purple-900 px-2.5 py-1 rounded-full font-semibold">
                    <Clock className="w-3 h-3" />
                    {step.time}
                  </span>
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-3">{step.title}</h3>
                <p className="text-sm text-gray-600 leading-relaxed font-light">{step.desc}</p>
              </div>
            </div>
          ))}
        </div>

        <div className="text-center mt-12">
          <Link
            href={isEs ? "/es#contact" : "/#contact"}
            className="bg-purple-900 hover:bg-purple-800 text-white font-bold px-8 py-4 rounded-full text-sm inline-flex items-center gap-2 transition-all shadow-md"
          >
            {isEs ? "Comienza con el Paso Uno hoy" : "Start Step One Today"}
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </div>
    </section>
  );
}
