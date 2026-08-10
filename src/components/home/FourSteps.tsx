"use client";

import React from "react";
import Link from "next/link";
import { ArrowRight } from "lucide-react";

interface FourStepsProps {
  lang: "en" | "es";
}

export default function FourSteps({ lang }: FourStepsProps) {
  const isEs = lang === "es";

  const stepsEn = [
    {
      num: "01",
      title: "Have an Open Conversation",
      desc: "We start by listening to your goals, concerns, family priorities, and current financial situation.",
    },
    {
      num: "02",
      title: "Review Your Options Clearly",
      desc: "We walk you through suitable strategies, explaining how each works in plain language with no hidden details.",
    },
    {
      num: "03",
      title: "Choose What Fits Your Family",
      desc: "You make decisions at your pace. We help you select coverage and plans that align with your needs and budget.",
    },
    {
      num: "04",
      title: "Enjoy Ongoing Support",
      desc: "Life changes over time. We stay connected to review your plan whenever your family reaches new milestones.",
    },
  ];

  const stepsEs = [
    {
      num: "01",
      title: "Ten una conversación abierta",
      desc: "Comenzamos escuchando tus metas, preocupaciones, prioridades familiares y tu situación financiera actual.",
    },
    {
      num: "02",
      title: "Revisa tus opciones con claridad",
      desc: "Te guiamos a través de estrategias adecuadas, explicando cómo funciona cada una en un lenguaje sencillo.",
    },
    {
      num: "03",
      title: "Elige lo que se adapte a tu familia",
      desc: "Tomas decisiones a tu propio ritmo. Te ayudamos a seleccionar coberturas y planes alineados con tus necesidades y presupuesto.",
    },
    {
      num: "04",
      title: "Disfruta de apoyo continuo",
      desc: "La vida cambia con el tiempo. Nos mantenemos conectados para revisar tu plan cada vez que tu familia alcance nuevas metas.",
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
            {isEs ? "4 pasos hacia la claridad financiera" : "4 Steps to Financial Clarity"}
          </h2>
          <p className="text-base text-gray-600 font-light leading-relaxed">
            {isEs
              ? "Un enfoque sencillo y sin presiones para ayudarte a tomar las mejores decisiones para tu familia."
              : "A simple, no-pressure approach to helping you make the best decisions for your family."}
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {steps.map((step, idx) => (
            <div
              key={idx}
              className="bg-purple-50/50 border border-purple-100 rounded-3xl p-8 flex flex-col justify-between hover:shadow-lg transition-all duration-300"
            >
              <div>
                <span className="text-4xl font-extrabold text-purple-900/30 block mb-4 font-mono">
                  {step.num}
                </span>
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
            {isEs ? "Comienza tu paso 1 hoy" : "Start Step 1 Today"}
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </div>
    </section>
  );
}
