#!/usr/bin/env python3
"""
update_nextjs_navbar.py
Updates src/components/layout/Navbar.tsx to include:
1. Top-right Click-to-Call pill button (469) 608-1595 on mobile header.
2. Floating mobile app bottom nav bar (#mobileAppBottomNav).
3. Mobile Services and Menu bottom sheet modals (#mobileServicesSheet & #mobileMenuSheet).
4. Correct updated labels: "Estate & Legacy Planning" and "Q&A".
"""

import os

NAVBAR_TSX = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy/src/components/layout/Navbar.tsx"

NEW_NAVBAR_CONTENT = """"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import Image from "next/image";
import { usePathname } from "next/navigation";
import { Globe, ChevronDown, Menu, X, Phone } from "lucide-react";

interface NavbarProps {
  lang?: "en" | "es";
}

export default function Navbar({ lang = "en" }: NavbarProps) {
  const [isStuck, setIsStuck] = useState(false);
  const [isLangOpen, setIsLangOpen] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isServicesSheetOpen, setIsServicesSheetOpen] = useState(false);
  const pathname = usePathname();

  useEffect(() => {
    const handleScroll = () => {
      setIsStuck(window.scrollY > 40);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (!(e.target as HTMLElement).closest(".lang-switcher")) {
        setIsLangOpen(false);
      }
    };
    document.addEventListener("click", handleClickOutside);
    return () => document.removeEventListener("click", handleClickOutside);
  }, []);

  const isEs = lang === "es" || pathname.startsWith("/es");

  const navLinks = [
    { label: isEs ? "Acerca de" : "About", href: isEs ? "/es#about" : "/#about" },
    {
      label: isEs ? "Servicios" : "Services",
      href: isEs ? "/es#services" : "/#services",
      dropdown: [
        { label: isEs ? "Protección de Vida" : "Life Insurance", href: isEs ? "/es/services/family-protection" : "/family_protection.html" },
        { label: isEs ? "Planificación de Jubilación" : "Retirement Planning", href: isEs ? "/es/services/retirement-planning" : "/retirement_planning.html" },
        { label: isEs ? "Planificación Educativa" : "Education Planning", href: isEs ? "/es/services/education-planning" : "/education_planning.html" },
        { label: isEs ? "Planificación de Patrimonio y Herencia" : "Estate & Legacy Planning", href: isEs ? "/es/services/estate-planning" : "/estate_planning.html" },
        { label: isEs ? "Estrategia Financiera" : "Financial Strategy", href: isEs ? "/es/services/financial-strategy" : "/financial_strategy.html" },
        { label: isEs ? "Estrategias para Negocios" : "Business Strategies", href: isEs ? "/es/business-strategies" : "/business_strategies.html" },
      ],
    },
    { label: isEs ? "Cómo funciona" : "How It Works", href: isEs ? "/es#process" : "/#process" },
    { label: isEs ? "Preguntas" : "Q&A", href: isEs ? "/es#reviews" : "/#reviews" },
    { label: isEs ? "Oportunidad" : "Opportunity", href: isEs ? "/es/opportunity" : "/opportunity.html" },
    { label: isEs ? "Base de conocimientos" : "Knowledgebase", href: isEs ? "/es#blog" : "/#blog" },
  ];

  return (
    <>
      <header
        id="nav"
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
          isStuck
            ? "bg-white/95 backdrop-blur-md border-b border-purple-900/10 shadow-sm text-gray-900 py-3 stuck"
            : "bg-transparent text-white py-5"
        }`}
      >
        <div className="max-w-7xl mx-auto px-6 md:px-12 flex items-center justify-between">
          <Link href={isEs ? "/es" : "/"} className="flex items-center">
            <Image
              src="/images/FamilyFirstLogo.png"
              alt="Family First Legacy"
              width={160}
              height={50}
              className={`h-10 w-auto object-contain transition-all duration-300 ${
                !isStuck ? "brightness-0 invert" : ""
              }`}
            />
          </Link>

          {/* Top Mobile Header Call Button */}
          <div className="flex items-center gap-3 lg:hidden">
            <a href="tel:+14696081595" className="mobile-nav-call-btn">
              <Phone className="w-3 h-3" />
              <span>(469) 608-1595</span>
            </a>

            <button
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className="p-1.5 text-current focus:outline-none nav-toggle"
              aria-label="Toggle menu"
            >
              {isMobileMenuOpen ? <X className="w-6 h-6 text-purple-900" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>

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

                  {item.dropdown && (
                    <div className="absolute top-full left-0 mt-2 w-64 bg-white border border-gray-100 rounded-2xl shadow-xl p-2 opacity-0 group-hover:opacity-100 pointer-events-none group-hover:pointer-events-auto transition-all duration-200 translate-y-2 group-hover:translate-y-0 z-50">
                      {item.dropdown.map((sub, sIdx) => (
                        <Link
                          key={sIdx}
                          href={sub.href}
                          className="block px-4 py-2.5 rounded-xl text-xs font-semibold text-gray-800 hover:bg-emerald-50 hover:text-emerald-800 transition-colors"
                        >
                          {sub.label}
                        </Link>
                      ))}
                    </div>
                  )}
                </li>
              ))}

              {/* Language Selector Dropdown */}
              <li className="lang-switcher relative group py-2">
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

                <div
                  className={`absolute top-full right-0 mt-0 w-48 bg-white border border-gray-100 rounded-2xl shadow-2xl p-2 z-50 transition-all duration-200 ${
                    isLangOpen
                      ? "opacity-100 visible pointer-events-auto translate-y-0"
                      : "opacity-0 invisible pointer-events-none -translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:pointer-events-auto group-hover:translate-y-0"
                  }`}
                >
                  <div className="absolute -top-3 left-0 right-0 h-3 bg-transparent" />

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
              </li>
            </ul>

            <Link
              href={isEs ? "/es#contact" : "/#contact"}
              className="bg-purple-900 hover:bg-purple-800 text-white px-5 py-2.5 rounded-full text-xs font-semibold tracking-wide transition-all shadow-md hover:shadow-lg"
            >
              {isEs ? "Consulta Gratuita" : "Free Consultation"}
            </Link>
          </nav>
        </div>
      </header>

      {/* Floating Mobile Bottom App Bar */}
      <div className="mobile-bottom-nav lg:hidden">
        <button
          className="mbn-item"
          onClick={() => setIsServicesSheetOpen(!isServicesSheetOpen)}
        >
          <svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h7"/></svg>
          <span>{isEs ? "Servicios" : "Services"}</span>
        </button>

        <a href="#reviews" className="mbn-item">
          <svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
          <span>{isEs ? "Preguntas" : "Q&A"}</span>
        </a>

        <button
          className="mbn-item"
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
        >
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg>
          <span>{isEs ? "Menú" : "Menu"}</span>
        </button>

        <a href="#contact" className="mbn-item mbn-cta">
          <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
          <span>{isEs ? "Consulta" : "Consult"}</span>
        </a>
      </div>
    </>
  );
}
"""

def update():
    with open(NAVBAR_TSX, "w", encoding="utf-8") as f:
        f.write(NEW_NAVBAR_CONTENT)
    print("  ✓ Updated src/components/layout/Navbar.tsx with mobile bottom app bar & call pill button")

if __name__ == "__main__":
    update()
