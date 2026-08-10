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
                ? "Diseñamos estrategias personalizadas adaptadas al camino único de su familia, brindándole claridad y confianza en cada hito."
                : "We design tailored strategies aligned with your family’s unique path, helping bring clarity and confidence to every milestone."}
            </p>
            <Link
              href={isEs ? "/es/business-strategies" : "/business-strategies"}
              className="st-link"
            >
              {isEs ? "Explorar todos los servicios" : "Explore All Services"}
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
              {isEs ? <>Protección de<br />seguro de vida</> : <>Life Insurance<br />Protection</>}
            </h3>
            <p className="sr-body">
              {isEs
                ? "El seguro de vida no se trata de usted; se trata de proteger a las personas que dependen de usted. Le ayudamos a explorar opciones de cobertura de compañías bien establecidas para ayudar a reemplazar ingresos, cubrir deudas y brindar estabilidad."
                : "Life insurance isn’t about you — it’s about protecting the people who depend on you. We help you explore coverage options from well-established carriers to help replace income, cover debts, and provide stability."}
            </p>
            <Link href={isEs ? "/es/business-strategies" : "/business-strategies"} className="sr-link">
              {isEs ? "Aprende más" : "Learn How It Works"}
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
                ? "La jubilación debe sentirse como una recompensa, no como una interrogante. Le ayudamos a explorar estrategias de ahorro e ingresos que buscan proteger su capital contra caídas del mercado y generar flujos de ingresos confiables."
                : "Retirement should feel like a reward, not a question mark. We help you explore savings and income strategies designed to seek principal protection from market downturns and support reliable income streams."}
            </p>
            <Link href={isEs ? "/es/business-strategies" : "/business-strategies"} className="sr-link">
              {isEs ? "Aprende más" : "Learn How It Works"}
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
                ? "El costo de la educación continúa aumentando. Le ayudamos a explorar opciones de planificación flexible que brindan crecimiento con ventajas impositivas y flexibilidad para apoyar los sueños de sus hijos."
                : "The cost of education continues to rise. We help you explore flexible planning choices designed to offer tax-advantaged growth and flexibility to support your children’s dreams."}
            </p>
            <Link href={isEs ? "/es/business-strategies" : "/business-strategies"} className="sr-link">
              {isEs ? "Aprende más" : "Learn How It Works"}
              <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" /></svg>
            </Link>
          </div>
        </div>

        {/* Service Row 4: Estate Preservation (Flip) */}
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
              {isEs ? <>Preservación<br />patrimonial</> : <>Estate<br />Preservation</>}
            </h3>
            <p className="sr-body">
              {isEs
                ? "Construir riqueza requiere tiempo; preservarla requiere planificación. Ayudamos a las familias a estructurar estrategias de transferencia de activos que buscan minimizar costos de legalización y transmitir su legado."
                : "Building wealth takes time; preserving it takes planning. We help families explore asset transfer strategies aimed at avoiding probate friction and passing on your legacy clearly."}
            </p>
            <Link href={isEs ? "/es/business-strategies" : "/business-strategies"} className="sr-link">
              {isEs ? "Aprende más" : "Learn How It Works"}
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
                ? "Su negocio lleva su trabajo, sus ingresos y las personas que dependen de él. Ayudamos a los dueños de negocios a comprender opciones de protección, estrategias de sucesión y herramientas de planificación."
                : "Your business carries your work, your income, and the people who depend on it. We help business owners understand protection options, succession strategies, and planning tools."}
            </p>
            <Link href={isEs ? "/es/business-strategies" : "/business-strategies"} className="sr-link">
              {isEs ? "Aprende más" : "Learn How It Works"}
              <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" /></svg>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}
