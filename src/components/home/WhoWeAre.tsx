"use client";

import React from "react";
import Link from "next/link";
import Image from "next/image";

interface WhoWeAreProps {
  lang: "en" | "es";
}

export default function WhoWeAre({ lang }: WhoWeAreProps) {
  const isEs = lang === "es";

  return (
    <section id="about" className="py-28 bg-white overflow-hidden">
      <div className="max-w-[1400px] mx-auto px-6 md:px-14">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16 items-start">
          
          {/* Photo Column */}
          <div className="relative">
            <div className="relative rounded-3xl overflow-visible">
              <Image
                className="w-full aspect-[4/5] object-cover rounded-3xl shadow-2xl block"
                src="/images/about.jpg"
                alt="Professional financial advisor"
                width={600}
                height={750}
                priority
              />

              {/* Floating Badge Tag (Bottom Right) */}
              <div className="absolute -bottom-6 -right-4 sm:bottom-10 sm:-right-6 bg-purple-900 text-white p-5 sm:p-6 rounded-2xl shadow-2xl z-20">
                <div className="font-extrabold text-3xl sm:text-4xl leading-none">2,000+</div>
                <div className="text-[11px] font-semibold tracking-wider uppercase mt-1 opacity-90">
                  {isEs ? "Familias atendidas" : "Families Served"}
                </div>
              </div>

              {/* Floating Badge (Top Right) */}
              <div className="absolute top-6 -right-2 sm:-right-4 bg-white text-gray-900 px-4 py-3 rounded-xl shadow-xl flex items-center gap-3 z-20 border border-gray-100">
                <span className="w-2.5 h-2.5 rounded-full bg-purple-600 animate-pulse" />
                <span className="text-xs font-bold whitespace-nowrap">
                  {isEs
                    ? "Sirviendo a familias en DFW y a nivel nacional"
                    : "Serving families across DFW & Nationwide"}
                </span>
              </div>
            </div>

            {/* Quote pull box under photo */}
            <div className="mt-8 p-8 bg-purple-50/80 border-l-4 border-purple-800 rounded-r-2xl">
              <p className="font-semibold text-lg sm:text-xl text-purple-950 italic leading-snug">
                {isEs
                  ? "“Hacemos más que ofrecer seguros: construimos relaciones, educamos a las familias y les ayudamos a crear planes centrados en proteger lo que más importa.”"
                  : "“We do more than offer insurance — we build relationships, educate families, and help them create plans focused on protecting what matters most.”"}
              </p>
              <cite className="block mt-3 text-xs font-bold tracking-widest uppercase text-purple-800 not-italic opacity-80">
                — Family First Legacy Team
              </cite>
            </div>
          </div>

          {/* Content Column */}
          <div className="lg:pl-8 py-4">
            <p className="text-xs font-bold tracking-[3.2px] uppercase text-purple-700 mb-4 flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-purple-600" />
              {isEs ? "Quiénes somos" : "Who We Are"}
            </p>

            <h2 className="font-extrabold text-4xl sm:text-5xl lg:text-6xl text-gray-950 leading-tight mb-7 tracking-tight">
              {isEs ? (
                <>Ponemos a la familia<br />primero. Siempre.</>
              ) : (
                <>We Put Family<br />First. Always.</>
              )}
            </h2>

            <div className="space-y-5 text-gray-600 text-base sm:text-lg font-light leading-relaxed mb-8">
              <p>
                {isEs
                  ? "Cada familia merece la oportunidad de proteger lo que ha construido, prepararse para el mañana y perseguir el futuro con el que sueña. Creemos que cada familia, independientemente de sus antecedentes o ingresos, merece acceso a orientación honesta y experta para ayudarla a tomar decisiones financieras informadas."
                  : "Every family deserves the opportunity to protect what they’ve built, prepare for tomorrow, and pursue the future they dream of. We believe every family — regardless of background or income — deserves access to honest, knowledgeable guidance to help them make informed financial decisions."}
              </p>

              <p>
                {isEs
                  ? "Family First Legacy es una agencia independiente de servicios financieros arraigada en la comunidad de Dallas-Fort Worth que presta servicios a familias en todo Estados Unidos. Ayudamos a personas, familias y dueños de negocios a explorar opciones financieras y de seguros de una red de compañías bien establecidas."
                  : "Family First Legacy is an independent financial services agency rooted in the Dallas–Fort Worth community and serving families across the United States. We help individuals, families, and business owners explore insurance and financial options from a network of well-established insurance and financial services companies."}
              </p>

              <p>
                {isEs
                  ? "Nuestros profesionales con licencia se toman el tiempo para escuchar, comprender sus metas y preocupaciones, y conocer a las personas que más le importan antes de ayudarle a explorar opciones que puedan alinearse con sus necesidades."
                  : "Our licensed professionals take the time to listen, understand your goals and concerns, and learn about the people who matter most to you before helping you explore options that may align with your needs."}
              </p>

              <p>
                {isEs
                  ? "Ya sea que esté protegiendo a su familia, preparándose para la jubilación, planificando el futuro de sus hijos o construyendo un legado, nuestra meta es brindarle orientación honesta, explicaciones claras y la información que necesita para tomar decisiones con confianza, sin presión y a su propio ritmo."
                  : "Whether you’re protecting your family, preparing for retirement, planning for your children’s future, or building a legacy, our goal is to provide honest guidance, clear explanations, and the information you need to make confident decisions — without pressure and at your own pace."}
              </p>
            </div>

            <Link
              href={isEs ? "/es#contact" : "/#contact"}
              className="inline-flex items-center gap-2.5 px-8 py-4 rounded-full bg-purple-900 text-white font-semibold text-sm shadow-xl hover:bg-purple-800 transition-all hover:-translate-y-0.5"
            >
              <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M5 12h14M12 5l7 7-7 7" />
              </svg>
              {isEs ? "Programe una revisión gratuita" : "Schedule a Free Review"}
            </Link>
          </div>

        </div>
      </div>
    </section>
  );
}
