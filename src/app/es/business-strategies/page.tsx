import React from "react";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import ContactForm from "@/components/home/ContactForm";

export default function SpanishBusinessStrategiesPage() {
  return (
    <main className="min-h-screen bg-white pt-24">
      <Navbar lang="es" />
      <div className="max-w-7xl mx-auto px-6 md:px-12 py-16">
        <span className="text-xs font-bold tracking-[3px] text-purple-900 uppercase block mb-3">
          ESTRATEGIAS PARA NEGOCIOS
        </span>
        <h1 className="text-4xl md:text-6xl font-extrabold text-gray-900 leading-tight mb-6">
          Protege el negocio que construiste
        </h1>
        <p className="text-lg text-gray-600 font-light leading-relaxed max-w-3xl mb-12">
          Trabajaste con esfuerzo para construir tu negocio. Desde cobertura para personas clave y planificación buy-sell hasta beneficios ejecutivos y estrategias de sucesión, ayudamos a dueños de negocios a explorar formas de proteger lo que han construido.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 my-12">
          <div className="bg-purple-50 p-8 rounded-3xl border border-purple-100">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">Protección para Personas Clave</h3>
            <p className="text-gray-600 leading-relaxed font-light">
              Ayuda a proteger tu negocio contra el impacto financiero de perder a un líder crítico o un generador clave de ingresos.
            </p>
          </div>
          <div className="bg-purple-50 p-8 rounded-3xl border border-purple-100">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">Planificación Buy-Sell y Sucesión</h3>
            <p className="text-gray-600 leading-relaxed font-light">
              Garantiza una transición fluida de propiedad y protege la continuidad del negocio si un socio se retira o fallece.
            </p>
          </div>
        </div>
      </div>
      <ContactForm lang="es" />
      <Footer lang="es" />
    </main>
  );
}
