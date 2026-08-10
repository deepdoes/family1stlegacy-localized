"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { ChevronLeft, ChevronRight, ArrowRight } from "lucide-react";

interface HeroSliderProps {
  lang: "en" | "es";
}

export default function HeroSlider({ lang }: HeroSliderProps) {
  const [currentSlide, setCurrentSlide] = useState(0);
  const isEs = lang === "es";

  const slidesEn = [
    {
      eyebrow: "LIFE INSURANCE PROTECTION",
      title: "Protect the People Who Matter Most",
      desc: "Life can change in a moment. The people you love deserve a plan that helps protect them when they need it most.\n\nWe help you explore coverage options from well-established carriers — designed to fit your needs, budget, and life.",
      ctaPrimaryText: "Get Protected Today",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Explore Coverage",
      ctaSecondaryLink: "/services/family-protection",
      bgImage: "/images/FamilyFirstHero1.jpg",
    },
    {
      eyebrow: "RETIREMENT PLANNING",
      title: "Your Golden Years, Planned With Care",
      desc: "Retirement should feel peaceful, not uncertain. Whether you’re just starting to save or fine-tuning an existing plan, we help you build a retirement strategy tailored to your timeline.\n\nSo you can move toward the future you’ve imagined with more clarity and confidence.",
      ctaPrimaryText: "Plan My Retirement",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn More",
      ctaSecondaryLink: "/services/retirement-planning",
      bgImage: "/images/FamilyFirstHero2.jpg",
    },
    {
      eyebrow: "EDUCATION PLANNING",
      title: "Invest in Their Brilliant Future",
      desc: "Every child deserves the chance to dream bigger. Start planning today so your children can pursue any dream — any school, any path — with fewer financial limits standing in the way.\n\nGive them opportunity, while keeping your family’s future in mind.",
      ctaPrimaryText: "Start an Education Fund",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn More",
      ctaSecondaryLink: "/services/education-planning",
      bgImage: "/images/FamilyFirstHero3.jpg",
    },
    {
      eyebrow: "ESTATE & LEGACY PLANNING",
      title: "Leave a Legacy That Can Last Generations",
      desc: "Everything you worked for tells a story. We help you explore estate and legacy strategies that honor your values and help your family be better prepared.\n\nYour legacy is not just what you leave behind — it is how you care for the people and causes that matter most.",
      ctaPrimaryText: "Preserve My Legacy",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn More",
      ctaSecondaryLink: "/services/estate-planning",
      bgImage: "/images/FamilyFirstHero4.jpg",
    },
    {
      eyebrow: "BUSINESS STRATEGIES",
      title: "Protect the Business You Built",
      desc: "You worked hard to build your business. From key-person coverage and buy-sell planning to executive benefits and succession strategies, we help business owners explore ways to protect what they have worked so hard to create.\n\nBecause your business is more than income — it is responsibility, sacrifice, and legacy.",
      ctaPrimaryText: "Protect My Business",
      ctaPrimaryLink: "/business-strategies",
      ctaSecondaryText: "Learn More",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/small_business_hero_1777398700055.png",
    },
    {
      eyebrow: "THE CAREER OPPORTUNITY",
      title: "Build Your Own Financial Legacy",
      desc: "Turn your passion for helping families into a meaningful financial services career. Start part-time or grow full-time — with training, mentorship, and support along the way.\n\nBuild something with purpose while helping families understand how to protect what matters most.",
      ctaPrimaryText: "Explore the Opportunity",
      ctaPrimaryLink: "/opportunity",
      ctaSecondaryText: "Talk to Us",
      ctaSecondaryLink: "/#contact",
      bgImage: "/images/FamilyFirstHero5.jpg",
    },
  ];

  const slidesEs = [
    {
      eyebrow: "PROTECCIÓN CON SEGURO DE VIDA",
      title: "Protege a las personas que más importan",
      desc: "La vida puede cambiar en un momento. Las personas que amas merecen un plan que ayude a protegerlas cuando más lo necesiten.\n\nTe ayudamos a explorar opciones de cobertura de compañías bien establecidas, diseñadas para ajustarse a tus necesidades, tu presupuesto y tu vida.",
      ctaPrimaryText: "Obtén protección hoy",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Conoce la cobertura",
      ctaSecondaryLink: "/es/services/family-protection",
      bgImage: "/images/FamilyFirstHero1.jpg",
    },
    {
      eyebrow: "PLANIFICACIÓN PARA LA JUBILACIÓN",
      title: "Tus años dorados, planificados con cuidado",
      desc: "La jubilación debería sentirse tranquila, no incierta. Ya sea que estés comenzando a ahorrar o ajustando un plan existente, te ayudamos a crear una estrategia de jubilación adaptada a tu tiempo.\n\nPara que puedas avanzar hacia el futuro que has imaginado con más claridad y confianza.",
      ctaPrimaryText: "Comienza mi plan de jubilación",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/services/retirement-planning",
      bgImage: "/images/FamilyFirstHero2.jpg",
    },
    {
      eyebrow: "PLANIFICACIÓN EDUCATIVA",
      title: "Invierte en su futuro brillante",
      desc: "Cada niño merece la oportunidad de soñar en grande. Comienza a planificar hoy para que tus hijos puedan seguir cualquier sueño — cualquier escuela, cualquier camino — con menos límites financieros en el camino.\n\nDales oportunidades, sin perder de vista el futuro de tu familia.",
      ctaPrimaryText: "Comienza un fondo educativo",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/services/education-planning",
      bgImage: "/images/FamilyFirstHero3.jpg",
    },
    {
      eyebrow: "PLANIFICACIÓN PATRIMONIAL Y DE LEGADO",
      title: "Deja un legado que pueda durar generaciones",
      desc: "Todo por lo que has trabajado cuenta una historia. Te ayudamos a explorar estrategias patrimoniales y de legado que honren tus valores y ayuden a tu familia a estar mejor preparada.\n\nTu legado no es solo lo que dejas atrás; también es la manera en que cuidas a las personas y causas que más importan.",
      ctaPrimaryText: "Protege mi legado",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/services/estate-planning",
      bgImage: "/images/FamilyFirstHero4.jpg",
    },
    {
      eyebrow: "ESTRATEGIAS PARA NEGOCIOS",
      title: "Protege el negocio que construiste",
      desc: "Trabajaste con esfuerzo para construir tu negocio. Desde cobertura para personas clave y planificación buy-sell hasta beneficios ejecutivos y estrategias de sucesión, ayudamos a dueños de negocios a explorar formas de proteger lo que han construido con tanto esfuerzo.\n\nPorque tu negocio es más que ingresos: es responsabilidad, sacrificio y legado.",
      ctaPrimaryText: "Protege mi negocio",
      ctaPrimaryLink: "/es/business-strategies",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/small_business_hero_1777398700055.png",
    },
    {
      eyebrow: "LA OPORTUNIDAD DE CARRERA",
      title: "Construye tu propio legado financiero",
      desc: "Convierte tu pasión por ayudar a las familias en una carrera significativa en servicios financieros. Puedes comenzar a tiempo parcial o crecer a tiempo completo, con capacitación, mentoría y apoyo en el camino.\n\nConstruye algo con propósito mientras ayudas a las familias a entender cómo proteger lo que más importa.",
      ctaPrimaryText: "Explora la oportunidad",
      ctaPrimaryLink: "/es/opportunity",
      ctaSecondaryText: "Habla con nosotros",
      ctaSecondaryLink: "/es#contact",
      bgImage: "/images/FamilyFirstHero5.jpg",
    },
  ];

  const slides = isEs ? slidesEs : slidesEn;

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % slides.length);
    }, 7000);
    return () => clearInterval(interval);
  }, [slides.length]);

  const slide = slides[currentSlide];

  return (
    <section className="relative min-h-screen bg-[#0A0A0F] text-white flex items-center pt-28 pb-16 overflow-hidden">
      {/* Background Image Carousel */}
      <div
        className="absolute inset-0 bg-cover bg-center transition-all duration-1000 transform scale-105"
        style={{
          backgroundImage: `url(${slide.bgImage})`,
          opacity: 0.35,
        }}
      />
      <div className="absolute inset-0 bg-gradient-to-r from-[#0A0A0F] via-[#0A0A0F]/80 to-transparent" />

      <div className="max-w-7xl mx-auto px-6 md:px-12 w-full relative z-10">
        <div className="max-w-3xl">
          <span className="text-xs md:text-sm font-bold tracking-[3px] text-purple-300 uppercase block mb-4">
            {slide.eyebrow}
          </span>
          <h1 className="text-4xl md:text-6xl font-extrabold text-white leading-[1.1] mb-6 tracking-tight">
            {slide.title}
          </h1>
          <p className="text-base md:text-lg text-gray-300 font-light leading-relaxed mb-8 whitespace-pre-line">
            {slide.desc}
          </p>

          <div className="flex flex-wrap gap-4">
            <Link
              href={slide.ctaPrimaryLink}
              className="bg-purple-900 hover:bg-purple-800 text-white font-bold px-8 py-4 rounded-full text-sm inline-flex items-center gap-2 transition-all shadow-lg hover:shadow-purple-900/30"
            >
              {slide.ctaPrimaryText}
              <ArrowRight className="w-4 h-4" />
            </Link>
            <Link
              href={slide.ctaSecondaryLink}
              className="bg-white/10 hover:bg-white/20 text-white font-semibold px-8 py-4 rounded-full text-sm backdrop-blur-md border border-white/20 transition-all"
            >
              {slide.ctaSecondaryText}
            </Link>
          </div>
        </div>
      </div>

      {/* Slide Navigation Controls */}
      <div className="absolute bottom-8 right-8 z-20 flex items-center gap-3">
        <button
          onClick={() => setCurrentSlide((prev) => (prev - 1 + slides.length) % slides.length)}
          className="p-3 rounded-full bg-white/10 hover:bg-white/20 text-white backdrop-blur-md border border-white/15 transition-all"
          aria-label="Previous slide"
        >
          <ChevronLeft className="w-5 h-5" />
        </button>
        <span className="text-xs font-bold tracking-widest text-white/70 px-2">
          {String(currentSlide + 1).padStart(2, "0")} / {String(slides.length).padStart(2, "0")}
        </span>
        <button
          onClick={() => setCurrentSlide((prev) => (prev + 1) % slides.length)}
          className="p-3 rounded-full bg-white/10 hover:bg-white/20 text-white backdrop-blur-md border border-white/15 transition-all"
          aria-label="Next slide"
        >
          <ChevronRight className="w-5 h-5" />
        </button>
      </div>
    </section>
  );
}
