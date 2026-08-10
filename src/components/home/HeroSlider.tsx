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
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_life_insurance_diverse_1777335713599.png",
    },
    {
      eyebrow: "RETIREMENT PLANNING",
      title: "Your Golden Years, Planned With Care",
      desc: "Retirement should feel peaceful, not uncertain. Whether you’re just starting to save or fine-tuning an existing plan, we help you build a retirement strategy tailored to your timeline.\n\nSo you can move toward the future you’ve imagined with more clarity and confidence.",
      ctaPrimaryText: "Plan My Retirement",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn More",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_retirement_diverse_1777335727638.png",
    },
    {
      eyebrow: "EDUCATION PLANNING",
      title: "Invest in Their Brilliant Future",
      desc: "Every child deserves the chance to dream bigger. Start planning today so your children can pursue any dream — any school, any path — with fewer financial limits standing in the way.\n\nGive them opportunity, while keeping your family’s future in mind.",
      ctaPrimaryText: "Start an Education Fund",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn More",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_education_diverse_1777335740128.png",
    },
    {
      eyebrow: "ESTATE & LEGACY PLANNING",
      title: "Leave a Legacy That Can Last Generations",
      desc: "Everything you worked for tells a story. We help you explore estate and legacy strategies that honor your values and help your family be better prepared.\n\nYour legacy is not just what you leave behind — it is how you care for the people and causes that matter most.",
      ctaPrimaryText: "Preserve My Legacy",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn More",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_estate_diverse_1777335759302.png",
    },
    {
      eyebrow: "BUSINESS STRATEGIES",
      title: "Protect the Business You Built",
      desc: "You worked hard to build your business. From key-person coverage and buy-sell planning to executive benefits and succession strategies, we help business owners explore ways to protect what they have worked so hard to create.\n\nBecause your business is more than income — it is responsibility, sacrifice, and legacy.",
      ctaPrimaryText: "Protect My Business",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Explore Business Solutions",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_business_diverse_1777335776243.png",
    },
    {
      eyebrow: "CAREER OPPORTUNITY",
      title: "Build a Meaningful Business Serving Others",
      desc: "Looking for a career where your effort directly impacts families in your community? We empower motivated individuals to build licensed, flexible financial services careers with mentorship and four potential revenue streams.\n\nNo prior financial experience required — we provide the education and support to help you get started.",
      ctaPrimaryText: "Explore Opportunity",
      ctaPrimaryLink: "/#contact",
      ctaSecondaryText: "Learn How It Works",
      ctaSecondaryLink: "/business-strategies",
      bgImage: "/images/hero_career_diverse_1777335790957.png",
    },
  ];

  const slidesEs = [
    {
      eyebrow: "PROTECCIÓN DE SEGURO DE VIDA",
      title: "Proteja a las personas que más importan",
      desc: "La vida puede cambiar en un momento. Las personas que amas merecen un plan que ayude a protegerlas cuando más lo necesitan.\n\nTe ayudamos a explorar opciones de cobertura de compañías bien establecidas, diseñadas para adaptarse a tus necesidades, presupuesto y vida.",
      ctaPrimaryText: "Obtenga protección hoy",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Explorar cobertura",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_life_insurance_diverse_1777335713599.png",
    },
    {
      eyebrow: "PLANIFICACIÓN PARA LA JUBILACIÓN",
      title: "Sus años dorados, planificados con cuidado",
      desc: "La jubilación debe sentirse tranquila, no incierta. Ya sea que estés comenzando a ahorrar o perfeccionando un plan existente, te ayudamos a construir una estrategia de jubilación adaptada a tu cronograma.\n\nPara que puedas avanzar hacia el futuro que has imaginado con mayor claridad y confianza.",
      ctaPrimaryText: "Planificar mi jubilación",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_retirement_diverse_1777335727638.png",
    },
    {
      eyebrow: "PLANIFICACIÓN EDUCATIVA",
      title: "Invierta en su brillante futuro",
      desc: "Cada niño merece la oportunidad de soñar en grande. Comienza a planificar hoy para que tus hijos puedan seguir cualquier sueño, cualquier escuela o cualquier camino con menos límites financieros.\n\nDales la oportunidad, mientras mantienes en mente el futuro de tu familia.",
      ctaPrimaryText: "Iniciar un fondo educativo",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_education_diverse_1777335740128.png",
    },
    {
      eyebrow: "PLANIFICACIÓN PATRIMONIAL Y DE LEGADO",
      title: "Deje un legado que perdure generaciones",
      desc: "Todo aquello por lo que has trabajado cuenta una historia. Te ayudamos a explorar estrategias patrimoniales y de legado que honren tus valores y ayuden a tu familia a estar mejor preparada.\n\nTu legado no es solo lo que dejas atrás: es cómo cuidas a las personas y causas que más importan.",
      ctaPrimaryText: "Preservar mi legado",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Aprende más",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_estate_diverse_1777335759302.png",
    },
    {
      eyebrow: "ESTRATEGIAS PARA NEGOCIOS",
      title: "Proteja el negocio que ha construido",
      desc: "Trabajaste duro para construir tu negocio. Desde cobertura para personas clave y planificación de compra-venta hasta beneficios ejecutivos y estrategias de sucesión, ayudamos a los dueños de negocios a explorar formas de proteger lo que tanto les costó crear.\n\nPorque tu negocio es más que ingresos: es responsabilidad, sacrificio y legado.",
      ctaPrimaryText: "Proteger mi negocio",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Explorar soluciones empresariales",
      ctaSecondaryLink: "/es/business-strategies",
      bgImage: "/images/hero_business_diverse_1777335776243.png",
    },
    {
      eyebrow: "OPORTUNIDAD DE CARRERA",
      title: "Construya un negocio significativo al servicio de los demás",
      desc: "¿Buscas una carrera donde tu esfuerzo impacte directamente a las familias de tu comunidad? Empoderamos a personas motivadas para construir carreras en servicios financieros flexibles y con licencia, con tutoría y cuatro fuentes de ingresos potenciales.\n\nNo se requiere experiencia financiera previa: brindamos la educación y el apoyo para ayudarte a comenzar.",
      ctaPrimaryText: "Explorar la oportunidad",
      ctaPrimaryLink: "/es#contact",
      ctaSecondaryText: "Conozca cómo funciona",
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

  const slide = slides[currentSlide];

  return (
    <section className="relative w-full min-h-[90vh] bg-purple-950 text-white flex items-center overflow-hidden">
      {/* Background Image Slideshow */}
      {slides.map((s, idx) => (
        <div
          key={idx}
          className={`absolute inset-0 transition-opacity duration-1000 ease-in-out ${
            idx === currentSlide ? "opacity-40 scale-100" : "opacity-0 scale-105 pointer-events-none"
          }`}
          style={{
            backgroundImage: `url(${s.bgImage})`,
            backgroundSize: "cover",
            backgroundPosition: "center",
          }}
        />
      ))}

      {/* Dark Gradient Overlay */}
      <div className="absolute inset-0 bg-gradient-to-r from-purple-950 via-purple-950/80 to-transparent z-10" />

      {/* Slide Content */}
      <div className="relative z-20 max-w-7xl mx-auto px-6 md:px-12 py-24 flex flex-col justify-center w-full">
        <div className="max-w-2xl">
          <span className="text-xs font-bold tracking-[3px] text-purple-200 uppercase mb-4 inline-block">
            {slide.eyebrow}
          </span>

          <h1 className="text-4xl md:text-6xl font-extrabold leading-tight text-white mb-6">
            {slide.title}
          </h1>

          <div className="text-base md:text-lg text-gray-200 font-light leading-relaxed mb-8 whitespace-pre-line">
            {slide.desc}
          </div>

          <div className="flex flex-wrap items-center gap-4">
            <Link
              href={slide.ctaPrimaryLink}
              className="bg-purple-900 hover:bg-purple-800 text-white font-bold px-8 py-4 rounded-full text-xs inline-flex items-center gap-2 transition-all shadow-lg hover:shadow-purple-900/40"
            >
              {slide.ctaPrimaryText}
              <ArrowRight className="w-4 h-4" />
            </Link>

            <Link
              href={slide.ctaSecondaryLink}
              className="bg-white/10 hover:bg-white/20 border border-white/20 text-white font-semibold px-8 py-4 rounded-full text-xs transition-all backdrop-blur-md"
            >
              {slide.ctaSecondaryText}
            </Link>
          </div>
        </div>

        {/* Slide Counter & Controls */}
        <div className="absolute bottom-8 right-6 md:right-12 flex items-center gap-4 z-30">
          <button
            onClick={handlePrev}
            aria-label="Previous Slide"
            className="w-12 h-12 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 flex items-center justify-center transition-all backdrop-blur-md"
          >
            <ChevronLeft className="w-5 h-5 text-white" />
          </button>

          <span className="text-xs font-mono tracking-widest text-purple-200">
            {String(currentSlide + 1).padStart(2, "0")} / {String(totalSlides).padStart(2, "0")}
          </span>

          <button
            onClick={handleNext}
            aria-label="Next Slide"
            className="w-12 h-12 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 flex items-center justify-center transition-all backdrop-blur-md"
          >
            <ChevronRight className="w-5 h-5 text-white" />
          </button>
        </div>
      </div>
    </section>
  );
}
