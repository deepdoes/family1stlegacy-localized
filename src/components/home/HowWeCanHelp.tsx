"use client";

import React from "react";
import Link from "next/link";
import { Shield, TrendingUp, GraduationCap, FileText, Briefcase, ArrowRight } from "lucide-react";

interface HowWeCanHelpProps {
  lang: "en" | "es";
}

export default function HowWeCanHelp({ lang }: HowWeCanHelpProps) {
  const isEs = lang === "es";

  const servicesEn = [
    {
      title: "Life Insurance Protection",
      desc: "Your family depends on you every day. We help explain term, whole life, and indexed universal life in simple language, so you can choose coverage that supports the people you love, your budget, and your future goals.",
      icon: Shield,
      btnText: "Learn How It Works",
      link: "/services/family-protection",
    },
    {
      title: "Retirement Planning",
      desc: "Retirement should not feel like a guess. Whether you’re just starting to save or reviewing a plan you already have, we help you understand your options and create a plan designed to support the future you want.",
      icon: TrendingUp,
      btnText: "Learn How It Works",
      link: "/services/retirement-planning",
    },
    {
      title: "Estate & Legacy Planning",
      desc: "Your legacy is more than money — it’s the people, values, and future you care about. We help you understand ways to organize your assets and work alongside your legal and tax professionals to help create a plan focused on what matters most.",
      icon: FileText,
      btnText: "Start a Legacy Conversation",
      link: "/services/estate-planning",
    },
    {
      title: "Education Planning",
      desc: "Every parent wants to give their child more opportunities for the future. Whether your child chooses college, trade school, or another path, we help you understand education savings options and build a plan designed to support their goals while keeping your retirement in mind.",
      icon: GraduationCap,
      btnText: "Learn How It Works",
      link: "/services/education-planning",
    },
    {
      title: "Business Strategies",
      desc: "Your business carries your work, your income, and the people who depend on it. We help business owners understand protection options, succession strategies, and planning tools that may help support long-term stability.",
      icon: Briefcase,
      btnText: "Learn How It Works",
      link: "/business-strategies",
    },
  ];

  const servicesEs = [
    {
      title: "Protección con seguro de vida",
      desc: "Tu familia depende de ti todos los días. Te ayudamos a entender el seguro de término, seguro de vida entera e indexed universal life en un lenguaje sencillo, para que puedas elegir una cobertura que apoye a las personas que amas, tu presupuesto y tus metas futuras.",
      icon: Shield,
      btnText: "Conoce cómo funciona",
      link: "/es/services/family-protection",
    },
    {
      title: "Planificación para la jubilación",
      desc: "La jubilación no debería sentirse como una adivinanza. Ya sea que estés comenzando a ahorrar o revisando un plan que ya tienes, te ayudamos a entender tus opciones y crear un plan diseñado para apoyar el futuro que deseas.",
      icon: TrendingUp,
      btnText: "Conoce cómo funciona",
      link: "/es/services/retirement-planning",
    },
    {
      title: "Planificación patrimonial y de legado",
      desc: "Tu legado es más que dinero: son las personas, los valores y el futuro que te importan. Te ayudamos a entender formas de organizar tus activos y trabajamos junto con tus profesionales legales y de impuestos para ayudar a crear un plan enfocado en lo que más importa.",
      icon: FileText,
      btnText: "Inicia una conversación sobre tu legado",
      link: "/es/services/estate-planning",
    },
    {
      title: "Planificación educativa",
      desc: "Todo padre desea darle a su hijo más oportunidades para el futuro. Ya sea que tu hijo elija la universidad, una escuela técnica u otro camino, te ayudamos a entender opciones de ahorro educativo y crear un plan diseñado para apoyar sus metas sin perder de vista tu jubilación.",
      icon: GraduationCap,
      btnText: "Conoce cómo funciona",
      link: "/es/services/education-planning",
    },
    {
      title: "Estrategias para Negocios",
      desc: "Su negocio representa su trabajo, sus ingresos y a las personas que dependen de él. Ayudamos a los dueños de negocios a entender opciones de protección, estrategias de sucesión y herramientas de planificación que pueden ayudar a apoyar la estabilidad a largo plazo.",
      icon: Briefcase,
      btnText: "Conoce cómo funciona",
      link: "/es/business-strategies",
    },
  ];

  const services = isEs ? servicesEs : servicesEn;

  return (
    <section id="services" className="py-24 bg-white border-t border-gray-100">
      <div className="max-w-7xl mx-auto px-6 md:px-12">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <span className="text-xs font-bold tracking-[3px] text-purple-900 uppercase block mb-3">
            {isEs ? "CÓMO PODEMOS AYUDAR" : "HOW WE CAN HELP"}
          </span>
          <h2 className="text-3xl md:text-5xl font-extrabold text-gray-900 leading-tight mb-4">
            {isEs ? "Orientación para cada etapa de la vida" : "Guidance for Every Stage of Life"}
          </h2>
          <p className="text-base text-gray-600 font-light leading-relaxed mb-6">
            {isEs
              ? "Desde proteger a tu familia hoy hasta prepararte para la jubilación y planificar el legado que deseas dejar, estamos aquí para ayudarte a entender tus opciones y crear una estrategia que se ajuste a cada capítulo de tu vida."
              : "From protecting your family today to preparing for retirement and planning the legacy you want to leave behind, we’re here to help you understand your options and build a strategy that fits each chapter of your life."}
          </p>
          <Link
            href={isEs ? "/es#contact" : "/#contact"}
            className="inline-flex items-center gap-2 bg-purple-900 hover:bg-purple-800 text-white font-bold px-6 py-3 rounded-full text-xs transition-all shadow-sm"
          >
            {isEs ? "Comienza con una conversación" : "Start With a Conversation"}
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>

        {/* 5 Tiles Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((item, idx) => {
            const Icon = item.icon;
            return (
              <div
                key={idx}
                className="bg-white border border-gray-200 rounded-3xl p-8 flex flex-col justify-between hover:shadow-xl hover:-translate-y-1 transition-all duration-300"
              >
                <div>
                  <div className="w-12 h-12 bg-purple-50 rounded-2xl flex items-center justify-center mb-6 text-purple-900">
                    <Icon className="w-6 h-6" />
                  </div>
                  <h3 className="text-xl font-bold text-gray-900 mb-3">{item.title}</h3>
                  <p className="text-sm text-gray-600 leading-relaxed font-light mb-8">{item.desc}</p>
                </div>
                <Link
                  href={item.link}
                  className="inline-flex items-center justify-center w-full py-3 px-4 rounded-xl border border-purple-900/20 text-purple-900 font-semibold text-xs hover:bg-purple-900 hover:text-white transition-colors gap-1.5"
                >
                  {item.btnText} →
                </Link>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
