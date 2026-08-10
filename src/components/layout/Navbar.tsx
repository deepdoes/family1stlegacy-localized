"use client";

import React, { useState, useEffect, useRef } from "react";
import Link from "next/link";
import Image from "next/image";
import { usePathname } from "next/navigation";
import { Globe, ChevronDown, Menu, X } from "lucide-react";

interface NavbarProps {
  lang: "en" | "es";
}

export default function Navbar({ lang }: NavbarProps) {
  const [isStuck, setIsStuck] = useState(false);
  const [isLangOpen, setIsLangOpen] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const pathname = usePathname();

  // Scroll listener for sticky header styling
  useEffect(() => {
    const handleScroll = () => {
      setIsStuck(window.scrollY > 40);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  // Close dropdowns on outside click
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (!(e.target as HTMLElement).closest(".lang-switcher")) {
        setIsLangOpen(false);
      }
    };
    document.addEventListener("click", handleClickOutside);
    return () => document.removeEventListener("click", handleClickOutside);
  }, []);

  const isEs = lang === "es";

  // Navigation Links Definition
  const navLinks = [
    { label: isEs ? "Acerca de" : "About", href: isEs ? "/es#about" : "/#about" },
    {
      label: isEs ? "Servicios" : "Services",
      href: isEs ? "/es#services" : "/#services",
      dropdown: [
        { label: isEs ? "Protección de Vida" : "Life Insurance", href: isEs ? "/es/services/family-protection" : "/services/family-protection" },
        { label: isEs ? "Planificación de Jubilación" : "Retirement Planning", href: isEs ? "/es/services/retirement-planning" : "/services/retirement-planning" },
        { label: isEs ? "Planificación Educativa" : "Education Planning", href: isEs ? "/es/services/education-planning" : "/services/education-planning" },
        { label: isEs ? "Preservación Patrimonial" : "Estate Preservation", href: isEs ? "/es/services/estate-planning" : "/services/estate-planning" },
        { label: isEs ? "Estrategia Financiera" : "Financial Strategy", href: isEs ? "/es/services/financial-strategy" : "/services/financial-strategy" },
        { label: isEs ? "Estrategias para Negocios" : "Business Strategies", href: isEs ? "/es/business-strategies" : "/business-strategies" },
      ],
    },
    { label: isEs ? "Cómo funciona" : "How It Works", href: isEs ? "/es#process" : "/#process" },
    { label: isEs ? "Oportunidad" : "Opportunity", href: isEs ? "/es/opportunity" : "/opportunity" },
    { label: isEs ? "Base de conocimientos" : "Knowledgebase", href: isEs ? "/es#blog" : "/#blog" },
  ];

  // Route target for language switcher
  const getAltLangPath = () => {
    if (isEs) {
      return pathname.replace(/^\/es/, "") || "/";
    } else {
      return `/es${pathname === "/" ? "" : pathname}`;
    }
  };

  return (
    <>
      <header
        id="nav"
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
          isStuck
            ? "bg-white/95 backdrop-blur-md border-b border-purple-900/10 shadow-sm text-gray-900 py-3"
            : "bg-transparent text-white py-5"
        }`}
      >
        <div className="max-w-7xl mx-auto px-6 md:px-12 flex items-center justify-between">
          {/* Logo */}
          <Link href={isEs ? "/es" : "/"} className="flex items-center">
            <Image
              src="/images/FamilyFirstLogo.png"
              alt="Family First Legacy"
              width={160}
              height={50}
              className={`h-12 w-auto object-contain transition-all duration-300 ${
                !isStuck ? "brightness-0 invert" : ""
              }`}
            />
          </Link>

          {/* Desktop Navigation Links */}
          <nav className="hidden lg:flex items-center gap-6">
            <ul className="flex items-center gap-6 list-none relative">
              {navLinks.map((item, idx) => (
                <li key={idx} className="relative group">
                  <Link
                    href={item.href}
                    className={`text-sm font-medium transition-colors hover:text-purple-600 flex items-center gap-1 ${
                      isStuck ? "text-gray-700" : "text-white/90"
                    }`}
                  >
                    {item.label}
                    {item.dropdown && <ChevronDown className="w-3.5 h-3.5 opacity-70 group-hover:rotate-180 transition-transform" />}
                  </Link>

                  {/* Dropdown Menu */}
                  {item.dropdown && (
                    <div className="absolute top-full left-0 mt-2 w-60 bg-white border border-gray-100 rounded-2xl shadow-xl p-2 opacity-0 group-hover:opacity-100 pointer-events-none group-hover:pointer-events-auto transition-all duration-200 translate-y-2 group-hover:translate-y-0 z-50">
                      {item.dropdown.map((sub, sIdx) => (
                        <Link
                          key={sIdx}
                          href={sub.href}
                          className="block px-4 py-2.5 rounded-xl text-sm font-medium text-gray-800 hover:bg-purple-50 hover:text-purple-900 transition-colors"
                        >
                          {sub.label}
                        </Link>
                      ))}
                    </div>
                  )}
                </li>
              ))}

              {/* 2-Language Selector Dropdown (EN & ES ONLY) */}
              <li className="lang-switcher relative">
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    setIsLangOpen(!isLangOpen);
                  }}
                  className={`inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold tracking-wide transition-all ${
                    isStuck
                      ? "bg-purple-900/10 border border-purple-900/20 text-gray-900"
                      : "bg-white/15 border border-white/30 text-white"
                  }`}
                  aria-label="Select language"
                >
                  <Globe className="w-3.5 h-3.5" />
                  <span>{isEs ? "ES" : "EN"}</span>
                  <ChevronDown className={`w-3 h-3 transition-transform ${isLangOpen ? "rotate-180" : ""}`} />
                </button>

                {isLangOpen && (
                  <div className="absolute top-full right-0 mt-2.5 w-48 bg-white border border-gray-100 rounded-2xl shadow-2xl p-2 z-50 animate-in fade-in slide-in-from-top-2 duration-150">
                    <Link
                      href={pathname.replace(/^\/es/, "") || "/"}
                      className={`flex items-center justify-between px-3.5 py-2.5 rounded-xl text-xs font-medium ${
                        !isEs ? "bg-purple-50 text-purple-900 font-bold" : "text-gray-700 hover:bg-gray-50"
                      }`}
                      onClick={() => setIsLangOpen(false)}
                    >
                      <span className="bg-purple-900/10 text-purple-900 px-1.5 py-0.5 rounded font-bold text-[10px]">EN</span>
                      <span className="flex-1 ml-2.5 text-left">English</span>
                      {!isEs && <span className="text-purple-900 text-sm">✓</span>}
                    </Link>
                    <Link
                      href={isEs ? pathname : `/es${pathname === "/" ? "" : pathname}`}
                      className={`flex items-center justify-between px-3.5 py-2.5 rounded-xl text-xs font-medium ${
                        isEs ? "bg-purple-50 text-purple-900 font-bold" : "text-gray-700 hover:bg-gray-50"
                      }`}
                      onClick={() => setIsLangOpen(false)}
                    >
                      <span className="bg-purple-900/10 text-purple-900 px-1.5 py-0.5 rounded font-bold text-[10px]">ES</span>
                      <span className="flex-1 ml-2.5 text-left">Español</span>
                      {isEs && <span className="text-purple-900 text-sm">✓</span>}
                    </Link>
                  </div>
                )}
              </li>
            </ul>

            {/* CTA Button */}
            <Link
              href={isEs ? "/es#contact" : "/#contact"}
              className="bg-purple-900 hover:bg-purple-800 text-white px-5 py-2.5 rounded-full text-xs font-semibold tracking-wide transition-all shadow-md hover:shadow-lg"
            >
              {isEs ? "Consulta Gratuita" : "Free Consultation"}
            </Link>
          </nav>

          {/* Mobile Hamburger Toggle Button */}
          <button
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            className="lg:hidden p-2 text-current focus:outline-none"
            aria-label="Toggle menu"
          >
            {isMobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
      </header>

      {/* Mobile Drawer Menu */}
      {isMobileMenuOpen && (
        <div className="fixed inset-0 z-40 bg-purple-950/95 backdrop-blur-xl text-white flex flex-col justify-between p-6 pt-24 lg:hidden animate-in fade-in duration-200">
          <nav className="flex flex-col gap-4">
            {navLinks.map((item, idx) => (
              <div key={idx} className="border-b border-white/10 pb-3">
                <Link
                  href={item.href}
                  className="text-lg font-semibold block hover:text-purple-300"
                  onClick={() => setIsMobileMenuOpen(false)}
                >
                  {item.label}
                </Link>
                {item.dropdown && (
                  <div className="pl-4 mt-2 flex flex-col gap-2">
                    {item.dropdown.map((sub, sIdx) => (
                      <Link
                        key={sIdx}
                        href={sub.href}
                        className="text-sm text-white/70 hover:text-white block py-1"
                        onClick={() => setIsMobileMenuOpen(false)}
                      >
                        {sub.label}
                      </Link>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </nav>

          {/* Mobile 2-Language Selector Row */}
          <div className="flex gap-2 pt-4 border-t border-white/10">
            <Link
              href={pathname.replace(/^\/es/, "") || "/"}
              className={`px-4 py-2 rounded-full text-xs font-bold tracking-wider ${
                !isEs ? "bg-purple-600 text-white" : "bg-white/10 text-white/70"
              }`}
              onClick={() => setIsMobileMenuOpen(false)}
            >
              EN (English)
            </Link>
            <Link
              href={isEs ? pathname : `/es${pathname === "/" ? "" : pathname}`}
              className={`px-4 py-2 rounded-full text-xs font-bold tracking-wider ${
                isEs ? "bg-purple-600 text-white" : "bg-white/10 text-white/70"
              }`}
              onClick={() => setIsMobileMenuOpen(false)}
            >
              ES (Español)
            </Link>
          </div>
        </div>
      )}
    </>
  );
}
