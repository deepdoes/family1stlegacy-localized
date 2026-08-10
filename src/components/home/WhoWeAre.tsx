"use client";

import React from "react";
import Link from "next/link";
import { ArrowRight, BookOpen, UserCheck, Heart, Award } from "lucide-react";

interface WhoWeAreProps {
  lang: "en" | "es";
}

export default function WhoWeAre({ lang }: WhoWeAreProps) {
  const isEs = lang === "es";

  const tilesEn = [
    {
      icon: BookOpen,
      title: "EDUCATION FIRST",
      desc: "Clear explanations before decisions",
    },
    {
      icon: UserCheck,
      title: "1-ON-1 GUIDANCE",
      desc: "Personal support that starts with listening",
    },
    {
      icon: Heart,
      title: "FAMILY FOCUSED",
      desc: "Planning around the people you love",
    },
    {
      icon: Award,
      title: "LICENSED GUIDANCE",
      desc: "Professionals who explain before recommending",
    },
  ];

  const tilesEs = [
    {
      icon: BookOpen,
      title: "EDUCACIÓN PRIMERO",
      desc: "Explicaciones claras antes de tomar decisiones",
    },
    {
      icon: UserCheck,
      title: "ORIENTACIÓN 1 A 1",
      desc: "Apoyo personal que comienza escuchándote",
    },
    {
      icon: Heart,
      title: "ENFOQUE FAMILIAR",
      desc: "Planificación centrada en las personas que amas",
    },
    {
      icon: Award,
      title: "GUÍA CON LICENCIA",
      desc: "Profesionales que explican antes de recomendar",
    },
  ];

  const tiles = isEs ? tilesEs : tilesEn;

  return (
    <section id="about" className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-6 md:px-12">
        <div className="max-w-4xl mx-auto text-left">
          <span className="text-xs font-bold tracking-[3px] text-purple-900 uppercase block mb-3">
            {isEs ? "QUIÉNES SOMOS" : "WHO WE ARE"}
          </span>
          <h2 className="text-3xl md:text-5xl font-extrabold text-gray-900 leading-tight mb-8">
            {isEs ? "Ponemos a la familia primero. Siempre." : "We Put Family First. Always."}
          </h2>

          <p className="text-lg md:text-xl font-medium text-gray-800 leading-relaxed mb-6">
            {isEs
              ? "Toda familia merece la oportunidad de proteger lo que ha construido, prepararse para el mañana y perseguir el futuro que sueña."
              : "Every family deserves the opportunity to protect what they’ve built, prepare for tomorrow, and pursue the future they dream of."}
          </p>

          <p className="text-base text-gray-600 leading-relaxed mb-6 font-light">
            {isEs
              ? "Creemos que toda familia, sin importar su origen o nivel de ingresos, merece acceso a orientación honesta y bien informada que le ayude a tomar decisiones financieras con conocimiento."
              : "We believe every family — regardless of background or income — deserves access to honest, knowledgeable guidance to help them make informed financial decisions."}
          </p>

          <p className="text-base text-gray-600 leading-relaxed mb-6 font-light">
            {isEs
              ? "Family First Legacy es una agencia independiente de servicios financieros con raíces en la comunidad de Dallas-Fort Worth y que sirve a familias en todo Estados Unidos. Ayudamos a individuos, familias y dueños de negocios a explorar opciones de seguros y servicios financieros a través de una red de compañías bien establecidas."
              : "Family First Legacy is an independent financial services agency rooted in the Dallas–Fort Worth community and serving families across the United States. We help individuals, families, and business owners explore insurance and financial options from a network of well-established insurance and financial services companies."}
          </p>

          <p className="text-base text-gray-600 leading-relaxed mb-6 font-light">
            {isEs
              ? "Nuestros profesionales con licencia se toman el tiempo para escucharte, entender tus metas y preocupaciones, y conocer a las personas que más importan en tu vida antes de ayudarte a explorar opciones que puedan alinearse con tus necesidades."
              : "Our licensed professionals take the time to listen, understand your goals and concerns, and learn about the people who matter most to you before helping you explore options that may align with your needs."}
          </p>

          <p className="text-base text-gray-600 leading-relaxed mb-8 font-light">
            {isEs
              ? "Ya sea que estés protegiendo a tu familia, preparándote para la jubilación, planificando el futuro de tus hijos o construyendo un legado, nuestra meta es brindarte orientación honesta, explicaciones claras y la información que necesitas para tomar decisiones con confianza, sin presión y a tu propio ritmo."
              : "Whether you’re protecting your family, preparing for retirement, planning for your children’s future, or building a legacy, our goal is to provide honest guidance, clear explanations, and the information you need to make confident decisions — without pressure and at your own pace."}
          </p>

          {/* 4 PDF Feature Tiles Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 my-10">
            {tiles.map((t, idx) => {
              const Icon = t.icon;
              return (
                <div
                  key={idx}
                  className="bg-purple-50/70 border border-purple-100/80 rounded-2xl p-5 text-center flex flex-col items-center justify-center hover:border-purple-300 transition-all"
                >
                  <div className="w-10 h-10 bg-purple-900/10 rounded-xl flex items-center justify-center text-purple-900 mb-3">
                    <Icon className="w-5 h-5" />
                  </div>
                  <h4 className="text-xs font-extrabold text-purple-900 tracking-wider uppercase mb-1">
                    {t.title}
                  </h4>
                  <p className="text-xs text-gray-600 font-light">{t.desc}</p>
                </div>
              );
            })}
          </div>

          {/* Quote Box */}
          <blockquote className="border-l-4 border-purple-900 pl-6 py-2 italic text-purple-950 font-serif text-lg leading-relaxed mb-10 bg-purple-50/50 rounded-r-2xl">
            {isEs
              ? "“Hacemos más que ofrecer seguros: construimos relaciones, educamos a las familias y les ayudamos a crear planes enfocados en proteger lo que más importa.”"
              : "“We do more than offer insurance — we build relationships, educate families, and help them create plans focused on protecting what matters most.”"}
            <footer className="not-italic text-xs font-sans font-bold text-gray-500 mt-2 uppercase tracking-widest">
              {isEs ? "— Equipo de Family First Legacy" : "— Family First Legacy Team"}
            </footer>
          </blockquote>

          <div>
            <Link
              href={isEs ? "/es#contact" : "/#contact"}
              className="bg-purple-900 hover:bg-purple-800 text-white font-bold px-8 py-4 rounded-full text-sm inline-flex items-center gap-2 transition-all shadow-md"
            >
              {isEs ? "Programa una revisión gratuita" : "Schedule a Free Review"}
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}
