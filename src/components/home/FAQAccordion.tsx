"use client";

import React, { useState } from "react";
import { ChevronDown } from "lucide-react";

interface FAQAccordionProps {
  lang: "en" | "es";
}

export default function FAQAccordion({ lang }: FAQAccordionProps) {
  const [openIdx, setOpenIdx] = useState<number | null>(0);
  const isEs = lang === "es";

  const faqsEn = [
    {
      q: "Why is family protection important?",
      a: "Family protection helps ensure that if something unexpected happens to you, your loved ones are not left carrying financial hardship alone. It provides funds to help cover mortgage payments, daily expenses, education costs, and final arrangements.",
    },
    {
      q: "How much life insurance coverage do I actually need?",
      a: "The right amount of coverage depends on your household income, debts, mortgage, future education goals for children, and ongoing living expenses. A simple review with one of our licensed professionals can help you determine an appropriate amount for your family.",
    },
    {
      q: "What is the difference between term life and permanent life insurance?",
      a: "Term life insurance provides coverage for a specific period (such as 10, 20, or 30 years) and is generally lower cost. Permanent life insurance provides lifelong protection and can build cash value over time.",
    },
    {
      q: "Are living benefits included with life insurance policies?",
      a: "Many modern life insurance policies offer living benefits riders that allow policyholders to access a portion of their death benefit while still living if diagnosed with a qualifying critical, chronic, or terminal illness.",
    },
    {
      q: "Can Family First Legacy help small business owners?",
      a: "Yes! We specialize in key-person insurance, buy-sell planning, executive bonus plans, and business succession strategies to help business owners protect their company, partners, and key employees.",
    },
  ];

  const faqsEs = [
    {
      q: "¿Por qué es importante la protección familiar?",
      a: "La protección familiar ayuda a garantizar que, si te sucede algo inesperado, tus seres queridos no se queden solos enfrentando dificultades financieras. Proporciona fondos para ayudar a cubrir pagos de hipoteca, gastos diarios, costos educativos y arreglos finales.",
    },
    {
      q: "¿Mucha cobertura de seguro de vida necesito realmente?",
      a: "La cantidad adecuada de cobertura depende de tus ingresos familiares, deudas, hipoteca, metas educativas futuras para tus hijos y gastos diarios continuos. Una revisión sencilla con uno de nuestros profesionales con licencia puede ayudarte a determinar la cantidad adecuada para tu familia.",
    },
    {
      q: "¿Cuál es la diferencia entre el seguro de vida a término y el permanente?",
      a: "El seguro de vida a término proporciona cobertura durante un período específico (como 10, 20 o 30 años) y generalmente tiene un costo menor. El seguro de vida permanente ofrece protección de por vida y puede acumular valor en efectivo con el tiempo.",
    },
    {
      q: "¿Los beneficios en vida están incluidos en las pólizas de seguro de vida?",
      a: "Muchas pólizas de seguro de vida modernas ofrecen cláusulas de beneficios en vida que permiten a los titulares acceder a una parte de su beneficio por fallecimiento mientras aún están vivos si son diagnosticados con una enfermedad crítica, crónica o terminal calificable.",
    },
    {
      q: "¿Puede Family First Legacy ayudar a pequeños empresarios?",
      a: "¡Sí! Nos especializamos en seguros para personas clave, planificación buy-sell, planes de bonos ejecutivos y estrategias de sucesión empresarial para ayudar a los dueños de negocios a proteger su empresa, socios y empleados clave.",
    },
  ];

  const faqs = isEs ? faqsEs : faqsEn;

  return (
    <section className="py-24 bg-[#F4F2F6] border-t border-gray-200">
      <div className="max-w-4xl mx-auto px-6 md:px-12">
        <div className="text-center mb-16">
          <span className="text-xs font-bold tracking-[3px] text-purple-900 uppercase block mb-3">
            {isEs ? "PREGUNTAS FRECUENTES" : "FREQUENTLY ASKED QUESTIONS"}
          </span>
          <h2 className="text-3xl md:text-5xl font-extrabold text-gray-900 leading-tight">
            {isEs ? "Respuestas claras a tus preguntas" : "Clear Answers to Your Questions"}
          </h2>
        </div>

        <div className="flex flex-col gap-4">
          {faqs.map((faq, idx) => {
            const isOpen = openIdx === idx;
            return (
              <div
                key={idx}
                className="bg-white border border-gray-200 rounded-2xl overflow-hidden shadow-sm transition-all"
              >
                <button
                  onClick={() => setOpenIdx(isOpen ? null : idx)}
                  className="w-full text-left p-6 md:p-8 flex justify-between items-center gap-4 focus:outline-none"
                >
                  <h3 className="text-base md:text-lg font-bold text-gray-900">{faq.q}</h3>
                  <ChevronDown
                    className={`w-5 h-5 text-purple-900 flex-shrink-0 transition-transform duration-200 ${
                      isOpen ? "rotate-180" : ""
                    }`}
                  />
                </button>
                {isOpen && (
                  <div className="px-6 pb-6 md:px-8 md:pb-8 pt-0 text-sm md:text-base text-gray-600 font-light leading-relaxed border-t border-gray-100 mt-2 pt-4">
                    {faq.a}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
