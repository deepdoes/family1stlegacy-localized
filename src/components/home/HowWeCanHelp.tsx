"use client";

import React from "react";
import Link from "next/link";
import Image from "next/image";

interface HowWeCanHelpProps {
  lang: "en" | "es";
}

export default function HowWeCanHelp({ lang }: HowWeCanHelpProps) {
  const isEs = lang === "es";

  return (
    <section id="services">
      <div className="container">
        {/* Header section */}
        <div className="services-top">
          <div className="services-top-left">
            <p className="t-label">
              <span className="green-dot"></span>
              {isEs ? "Cómo podemos ayudar" : "How We Can Help"}
            </p>
            <h2 className="t-h1 services-big-title">
              {isEs ? (
                <>Orientación para<br />cada etapa<br />de la <em>Vida.</em></>
              ) : (
                <>Guidance for<br />Every Stage<br />of <em>Life.</em></>
              )}
            </h2>
          </div>
          <div className="services-top-right">
            <div className="st-accent"></div>
            <p>
              {isEs
                ? "Desde proteger a tu familia hoy hasta prepararte para la jubilación y planificar el legado que deseas dejar, estamos aquí para ayudarte a entender tus opciones y crear una estrategia que se ajuste a cada capítulo de tu vida."
                : "From protecting your family today to preparing for retirement and planning the legacy you want to leave behind, we’re here to help you understand your options and build a strategy that fits each chapter of your life."}
            </p>
            <Link
              href={isEs ? "/es#contact" : "/#contact"}
              className="st-link"
            >
              {isEs ? "Comienza con una conversación" : "Start With a Conversation"}
              <svg viewBox="0 0 24 24">
                <path d="M5 12h14M12 5l7 7-7 7" />
              </svg>
            </Link>
          </div>
        </div>

        {/* Service Row 1: Life Insurance */}
        <div className="service-row">
          <div className="sr-photo-wrap">
            <Image
              className="sr-photo"
              src="/images/hero_life_insurance_diverse_1777335713599.png"
              alt="Life Insurance Protection"
              width={600}
              height={450}
            />
          </div>
          <div className="sr-content">
            <div className="sr-num">01</div>
            <h3 className="sr-title">
              {isEs ? <>Protección con<br />seguro de vida</> : <>Life Insurance<br />Protection</>}
            </h3>
            <p className="sr-body">
              {isEs
                ? "Tu familia depende de ti todos los días. Te ayudamos a entender el seguro de término, seguro de vida entera e indexed universal life en un lenguaje sencillo, para que puedas elegir una cobertura que apoye a las personas que amas, tu presupuesto y tus metas futuras."
                : "Your family depends on you every day. We help explain term, whole life, and indexed universal life in simple language, so you can choose coverage that supports the people you love, your budget, and your future goals."}
            </p>
            <Link href={isEs ? "/es/business-strategies" : "/business-strategies"} className="sr-link">
              {isEs ? "Conoce cómo funciona" : "Learn How It Works"}
              <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" /></svg>
            </Link>
          </div>
        </div>

        {/* Service Row 2: Retirement Planning (Flip) */}
        <div className="service-row flip">
          <div className="sr-photo-wrap">
            <Image
              className="sr-photo"
              src="/images/hero_retirement_diverse_1777335727638.png"
              alt="Retirement Planning"
              width={600}
              height={450}
            />
          </div>
          <div className="sr-content">
            <div className="sr-num">02</div>
            <h3 className="sr-title">
              {isEs ? <>Planificación para<br />la jubilación</> : <>Retirement<br />Planning</>}
            </h3>
            <p className="sr-body">
              {isEs
                ? "La jubilación no debería sentirse como una adivinanza. Ya sea que estés comenzando a ahorrar o revisando un plan que ya tienes, te ayudamos a entender tus opciones y crear un plan diseñado para apoyar el futuro que deseas."
                : "Retirement should not feel like a guess. Whether you’re just starting to save or reviewing a plan you already have, we help you understand your options and create a plan designed to support the future you want."}
            </p>
            <Link href={isEs ? "/es/business-strategies" : "/business-strategies"} className="sr-link">
              {isEs ? "Conoce cómo funciona" : "Learn How It Works"}
              <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" /></svg>
            </Link>
          </div>
        </div>

        {/* Service Row 3: Education Planning */}
        <div className="service-row">
          <div className="sr-photo-wrap">
            <Image
              className="sr-photo"
              src="/images/hero_education_diverse_1777335740128.png"
              alt="Education Planning"
              width={600}
              height={450}
            />
          </div>
          <div className="sr-content">
            <div className="sr-num">03</div>
            <h3 className="sr-title">
              {isEs ? <>Planificación<br />educativa</> : <>Education<br />Planning</>}
            </h3>
            <p className="sr-body">
              {isEs
                ? "Todo padre desea darle a su hijo más oportunidades para el futuro. Ya sea que tu hijo elija la universidad, una escuela técnica u otro camino, te ayudamos a entender opciones de ahorro educativo y crear un plan diseñado para apoyar sus metas sin perder de vista tu jubilación."
                : "Every parent wants to give their child more opportunities for the future. Whether your child chooses college, trade school, or another path, we help you understand education savings options and build a plan designed to support their goals while keeping your retirement in mind."}
            </p>
            <Link href={isEs ? "/es/business-strategies" : "/business-strategies"} className="sr-link">
              {isEs ? "Conoce cómo funciona" : "Learn How It Works"}
              <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" /></svg>
            </Link>
          </div>
        </div>

        {/* Service Row 4: Estate & Legacy Planning (Flip) */}
        <div className="service-row flip">
          <div className="sr-photo-wrap">
            <Image
              className="sr-photo"
              src="/images/hero_estate_diverse_1777335759302.png"
              alt="Estate Preservation"
              width={600}
              height={450}
            />
          </div>
          <div className="sr-content">
            <div className="sr-num">04</div>
            <h3 className="sr-title">
              {isEs ? <>Planificación patrimonial<br />y de legado</> : <>Estate &amp; Legacy<br />Planning</>}
            </h3>
            <p className="sr-body">
              {isEs
                ? "Tu legado es más que dinero: son las personas, los valores y el futuro que te importan. Te ayudamos a entender formas de organizar tus activos y trabajamos junto con tus profesionales legales y de impuestos para ayudar a crear un plan enfocado en lo que más importa."
                : "Your legacy is more than money — it’s the people, values, and future you care about. We help you understand ways to organize your assets and work alongside your legal and tax professionals to help create a plan focused on what matters most."}
            </p>
            <Link href={isEs ? "/es/business-strategies" : "/business-strategies"} className="sr-link">
              {isEs ? "Inicia una conversación sobre tu legado" : "Start a Legacy Conversation"}
              <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" /></svg>
            </Link>
          </div>
        </div>

        {/* Service Row 5: Business Strategies */}
        <div className="service-row">
          <div className="sr-photo-wrap">
            <Image
              className="sr-photo"
              src="/images/small_business_hero_1777398700055.png"
              alt="Business Strategies"
              width={600}
              height={450}
            />
          </div>
          <div className="sr-content">
            <div className="sr-num">05</div>
            <h3 className="sr-title">
              {isEs ? <>Estrategias para<br />negocios</> : <>Business<br />Strategies</>}
            </h3>
            <p className="sr-body">
              {isEs
                ? "Su negocio representa su trabajo, sus ingresos y a las personas que dependen de él. Ayudamos a los dueños de negocios a entender opciones de protección, estrategias de sucesión y herramientas de planificación que pueden ayudar a apoyar la estabilidad a largo plazo."
                : "Your business carries your work, your income, and the people who depend on it. We help business owners understand protection options, succession strategies, and planning tools that may help support long-term stability."}
            </p>
            <Link href={isEs ? "/es/business-strategies" : "/business-strategies"} className="sr-link">
              {isEs ? "Conoce cómo funciona" : "Learn How It Works"}
              <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" /></svg>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}
