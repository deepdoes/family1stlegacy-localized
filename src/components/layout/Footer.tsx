"use client";

import React from "react";
import Link from "next/link";

interface FooterProps {
  lang: "en" | "es";
}

export default function Footer({ lang }: FooterProps) {
  const isEs = lang === "es";

  return (
    <footer className="bg-[#0A0A0F] color-white text-gray-400 py-16 text-sm border-t border-white/10">
      <div className="max-w-7xl mx-auto px-6 md:px-12 text-center">
        {/* Core Mission Line */}
        <p className="text-base text-gray-300 max-w-3xl mx-auto mb-6 leading-relaxed">
          {isEs
            ? "Ayudamos a las familias a construir un futuro financiero más sólido, ayudar a proteger a sus seres queridos y crear un legado significativo para las generaciones futuras."
            : "Empowering families to build a stronger financial future, help protect their loved ones, and create a meaningful legacy for generations to come."}
        </p>

        {/* Serving Families Nationwide Badge */}
        <div className="inline-block bg-white/10 border border-white/15 px-4 py-1.5 rounded-full text-xs font-semibold text-white mb-8 tracking-wide">
          {isEs ? "Sirviendo a familias en todo el país" : "Serving Families Nationwide"}
        </div>

        {/* Footer Legal Links */}
        <div className="flex justify-center gap-6 mb-8 text-xs font-medium">
          <Link href={isEs ? "/es/privacy" : "/privacy"} className="hover:text-white transition-colors">
            {isEs ? "Política de Privacidad" : "Privacy Policy"}
          </Link>
          <span className="text-white/20">•</span>
          <Link href={isEs ? "/es/terms" : "/terms"} className="hover:text-white transition-colors">
            {isEs ? "Términos de Servicio" : "Terms of Service"}
          </Link>
        </div>

        {/* Full Compliance Disclaimer */}
        <p className="text-xs text-gray-500 max-w-4xl mx-auto leading-relaxed border-t border-white/5 pt-6">
          {isEs
            ? "Family First Legacy es una agencia independiente de servicios financieros que sirve a familias en todo Estados Unidos. Los productos de seguros y financieros se ofrecen a través de profesionales debidamente licenciados y están sujetos a aprobación de la compañía, disponibilidad de productos, evaluación de suscripción y requisitos estatales aplicables. No ofrecemos asesoría legal ni fiscal; consulta con un profesional calificado para esos asuntos. La elegibilidad individual, disponibilidad de productos, características de la póliza y resultados pueden variar."
            : "Family First Legacy is an independent financial services agency serving families across the United States. Insurance and financial products are offered through properly licensed professionals and are subject to carrier approval, product availability, underwriting, and applicable state requirements. We do not provide tax or legal advice; please consult a qualified professional for those matters. Individual eligibility, product availability, policy features, and results may vary."}
        </p>
      </div>
    </footer>
  );
}
