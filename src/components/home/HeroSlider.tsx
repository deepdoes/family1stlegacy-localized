"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";

interface HeroSliderProps {
  lang: "en" | "es";
}

export default function HeroSlider({ lang }: HeroSliderProps) {
  const [currentSlide, setCurrentSlide] = useState(0);
  const isEs = lang === "es";

  const slidesEn = [
    {
      eyebrow: "LIFE INSURANCE PROTECTION",
      title: <>Protect the People<br />Who Matter <em>Most.</em></>,
      sub: "Life can change in a moment. The people you love deserve a plan that helps protect them when they need it most. We help you explore coverage options from well-established carriers — designed to fit your needs, budget, and life.",
      ctaPrimaryText: "Get Protected Today",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Explore Coverage",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_life_insurance_diverse_1777335713599.png",
    },
    {
      eyebrow: "RETIREMENT PLANNING",
      title: <>Your Golden Years,<br />Planned With <em>Care.</em></>,
      sub: "Retirement should feel peaceful, not uncertain. Whether you’re just starting to save or fine-tuning an existing plan, we help you build a retirement strategy tailored to your timeline — so you can move toward the future you’ve imagined with clarity and confidence.",
      ctaPrimaryText: "Plan My Retirement",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn More",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_retirement_diverse_1777335727638.png",
    },
    {
      eyebrow: "EDUCATION PLANNING",
      title: <>Invest in Their<br />Brilliant <em>Future.</em></>,
      sub: "Every child deserves the chance to dream bigger. Start planning today so your children can pursue any dream — any school, any path — with fewer financial limits standing in the way.",
      ctaPrimaryText: "Start an Education Fund",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn More",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_education_diverse_1777335740128.png",
    },
    {
      eyebrow: "ESTATE & LEGACY PLANNING",
      title: <>Leave a Legacy That<br />Lasts <em>Generations.</em></>,
      sub: "Everything you worked for tells a story. We help you explore estate and legacy strategies that honor your values and help your family be better prepared.",
      ctaPrimaryText: "Preserve My Legacy",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn More",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_estate_diverse_1777335759302.png",
    },
    {
      eyebrow: "BUSINESS STRATEGIES",
      title: <>Protect the Business<br />You <em>Built.</em></>,
      sub: "You worked hard to build your business. From key-person coverage and buy-sell planning to executive benefits and succession strategies, we help business owners protect what they created.",
      ctaPrimaryText: "Protect My Business",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Explore Business Solutions",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_business_diverse_1777335776243.png",
    },
    {
      eyebrow: "CAREER OPPORTUNITY",
      title: <>Build a Meaningful<br />Business Serving <em>Others.</em></>,
      sub: "Looking for a career where your effort directly impacts families in your community? We empower motivated individuals to build licensed, flexible financial services careers with mentorship and four potential revenue streams.",
      ctaPrimaryText: "Explore Opportunity",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn How It Works",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_career_diverse_1777335790957.png",
    },
  ];

  const slidesEs = [
    {
      eyebrow: "PROTECCIÓN CON SEGURO DE VIDA",
      title: <>Protege a las personas<br />que más <em>importan.</em></>,
      sub: "La vida puede cambiar en un momento. Las personas que amas merecen un plan que ayude a protegerlas cuando más lo necesiten. Te ayudamos a explorar opciones de cobertura de compañías bien establecidas, diseñadas para ajustarse a tus necesidades, tu presupuesto y tu vida.",
      ctaPrimaryText: "Obtén protección hoy",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Conoce la cobertura",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_life_insurance_diverse_1777335713599.png",
    },
    {
      eyebrow: "PLANIFICACIÓN PARA LA JUBILACIÓN",
      title: <>Tus años dorados,<br />planificados con <em>cuidado.</em></>,
      sub: "La jubilación debería sentirse tranquila, no incierta. Ya sea que estés comenzando a ahorrar o ajustando un plan existente, te ayudamos a crear una estrategia de jubilación adaptada a tu tiempo — para que puedas avanzar hacia el futuro que has imaginado con más claridad y confianza.",
      ctaPrimaryText: "Comienza mi plan de jubilación",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_retirement_diverse_1777335727638.png",
    },
    {
      eyebrow: "PLANIFICACIÓN EDUCATIVA",
      title: <>Invierte en su<br />futuro <em>brillante.</em></>,
      sub: "Cada niño merece la oportunidad de soñar en grande. Comienza a planificar hoy para que tus hijos puedan seguir cualquier sueño — cualquier escuela, cualquier camino — con menos límites financieros en el camino. Dales oportunidades, sin perder de vista el futuro de tu familia.",
      ctaPrimaryText: "Comienza un fondo educativo",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_education_diverse_1777335740128.png",
    },
    {
      eyebrow: "PLANIFICACIÓN PATRIMONIAL Y DE LEGADO",
      title: <>Deja un legado que<br />pueda durar <em>generaciones.</em></>,
      sub: "Todo por lo que has trabajado cuenta una historia. Te ayudamos a explorar estrategias patrimoniales y de legado que honren tus valores y ayuden a tu familia a estar mejor preparada. Tu legado no es solo lo que dejas atrás; también es la manera en que cuidas a las personas y causas que más importan.",
      ctaPrimaryText: "Protege mi legado",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_estate_diverse_1777335759302.png",
    },
    {
      eyebrow: "ESTRATEGIAS PARA NEGOCIOS",
      title: <>Protege el negocio<br />que <em>construiste.</em></>,
      sub: "Trabajaste con esfuerzo para construir tu negocio. Desde cobertura para personas clave y planificación buy-sell hasta beneficios ejecutivos y estrategias de sucesión, ayudamos a dueños de negocios a explorar formas de proteger lo que han construido con tanto esfuerzo.",
      ctaPrimaryText: "Protege mi negocio",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_business_diverse_1777335776243.png",
    },
    {
      eyebrow: "LA OPORTUNIDAD DE CARRERA",
      title: <>Construye tu propio<br /><em>legado financiero.</em></>,
      sub: "Convierte tu pasión por ayudar a las familias en una carrera significativa en servicios financieros. Puedes comenzar a tiempo parcial o crecer a tiempo completo, con capacitación, mentoría y apoyo en el camino. Construye algo con propósito mientras ayudas a las familias a entender cómo proteger lo que más importa.",
      ctaPrimaryText: "Explora la oportunidad",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Habla con nosotros",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_career_diverse_1777335790957.png",
    },
  ];

  const slides = isEs ? slidesEs : slidesEn;
  const totalSlides = slides.length;

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % totalSlides);
    }, 7000);
    return () => clearInterval(timer);
  }, [totalSlides]);

  const handlePrev = () => {
    setCurrentSlide((prev) => (prev - 1 + totalSlides) % totalSlides);
  };

  const handleNext = () => {
    setCurrentSlide((prev) => (prev + 1) % totalSlides);
  };

  return (
    <section id="hero" className="relative w-full h-screen min-h-[650px] overflow-hidden bg-black">
      {slides.map((slide, idx) => {
        const isActive = currentSlide === idx;
        return (
          <div
            key={idx}
            className={`absolute inset-0 transition-opacity duration-1000 ease-in-out ${
              isActive ? "opacity-100 z-10 pointer-events-auto" : "opacity-0 z-0 pointer-events-none"
            }`}
          >
            {/* Background Image */}
            <div
              className="absolute inset-0 bg-cover bg-center transition-transform duration-[8000ms] ease-out scale-105"
              style={{ backgroundImage: `url('${slide.bgImage}')` }}
            />

            {/* Dark Vignette Overlay */}
            <div className="absolute inset-0 bg-gradient-to-r from-black/85 via-black/60 to-black/30" />

            {/* Slide Content */}
            <div className="relative z-20 h-full max-w-[1400px] mx-auto px-10 md:px-20 flex items-center pt-16">
              <div className="max-w-[720px] text-white">
                <div className="inline-flex items-center gap-2 text-[11px] font-bold tracking-[3.5px] uppercase text-purple-200/80 mb-6">
                  <span className="w-9 h-[1.5px] bg-purple-400" />
                  {slide.eyebrow}
                </div>

                <h1 className="font-extrabold text-4xl sm:text-5xl md:text-6xl lg:text-7xl leading-[0.95] tracking-tight text-white mb-6">
                  {slide.title}
                </h1>

                <p className="text-base sm:text-lg font-light text-gray-200/90 leading-relaxed mb-8 max-w-[560px]">
                  {slide.sub}
                </p>

                <div className="flex flex-wrap items-center gap-4">
                  <Link
                    href={slide.ctaPrimaryLink}
                    className="inline-flex items-center gap-2 px-7 py-3.5 rounded-full bg-purple-900 text-white font-semibold text-sm shadow-xl hover:bg-purple-800 transition-all hover:-translate-y-0.5"
                  >
                    <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M5 12h14M12 5l7 7-7 7" />
                    </svg>
                    {slide.ctaPrimaryText}
                  </Link>
                  <Link
                    href={slide.ctaSecondaryLink}
                    className="inline-flex items-center gap-2 px-7 py-3.5 rounded-full border border-white/40 text-white font-semibold text-sm hover:bg-white/10 transition-all"
                  >
                    {slide.ctaSecondaryText}
                  </Link>
                </div>
              </div>
            </div>
          </div>
        );
      })}

      {/* Hero Stats Bar */}
      <div className="absolute bottom-20 left-10 md:left-20 z-30 hidden lg:flex items-center gap-12 text-white">
        <div className="border-l-2 border-purple-400 pl-4">
          <div className="text-2xl font-extrabold">2,000+</div>
          <div className="text-[11px] tracking-wider text-gray-300 uppercase mt-1">Families Served</div>
        </div>
        <div className="border-l-2 border-purple-400 pl-4">
          <div className="text-2xl font-extrabold">100%</div>
          <div className="text-[11px] tracking-wider text-gray-300 uppercase mt-1">Licensed Professionals</div>
        </div>
        <div className="border-l-2 border-purple-400 pl-4">
          <div className="text-2xl font-extrabold">DFW &amp; US</div>
          <div className="text-[11px] tracking-wider text-gray-300 uppercase mt-1">Serving Families Nationwide</div>
        </div>
      </div>

      {/* Slide Arrow Navigation */}
      <button
        onClick={handlePrev}
        className="absolute left-6 top-1/2 -translate-y-1/2 z-30 w-12 h-12 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 flex items-center justify-center text-white backdrop-blur-md transition-all"
        aria-label="Previous slide"
      >
        <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M15 18l-6-6 6-6" />
        </svg>
      </button>

      <button
        onClick={handleNext}
        className="absolute right-6 top-1/2 -translate-y-1/2 z-30 w-12 h-12 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 flex items-center justify-center text-white backdrop-blur-md transition-all"
        aria-label="Next slide"
      >
        <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M9 18l6-6-6-6" />
        </svg>
      </button>

      {/* Slide Counter */}
      <div className="absolute top-24 right-8 z-30 hidden sm:flex items-center gap-2.5 bg-black/40 backdrop-blur-md border border-white/20 px-4 py-2 rounded-full text-white text-xs font-bold">
        <span>{String(currentSlide + 1).padStart(2, "0")}</span>
        <span className="w-4 h-[1px] bg-white/40" />
        <span className="text-gray-400">{String(totalSlides).padStart(2, "0")}</span>
      </div>
    </section>
  );
}
