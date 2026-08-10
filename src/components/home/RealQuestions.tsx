"use client";

import React, { useState } from "react";
import Link from "next/link";
import { ArrowRight } from "lucide-react";

interface RealQuestionsProps {
  lang: "en" | "es";
}

export default function RealQuestions({ lang }: RealQuestionsProps) {
  const [activeIdx, setActiveIdx] = useState(0);
  const isEs = lang === "es";

  const cardsEn = [
    {
      counter: "01 OF 06 • FAMILY PROTECTION",
      badge: "Guidance with care",
      category: "01 • Family Protection",
      shortQuestion: "“If my income stopped tomorrow...”",
      question: "“If my income stopped tomorrow, how long would my family be okay?”",
      desc: "Many families have some coverage through work, but they are not sure if it is enough — or if it would stay with them if life changed. A simple review can help identify possible gaps, explain available protection options, and help families understand what may fit their needs, budget, and responsibilities.",
    },
    {
      counter: "02 OF 06 • LIVING BENEFITS",
      badge: "Living benefits guidance",
      category: "02 • Living Benefits",
      shortQuestion: "“If illness stopped my income...”",
      question: "“What if I survive the illness — but my income does not?”",
      desc: "A serious illness can affect more than health. It can affect income, bills, and the whole household. Some life insurance policies may include living benefits that can help provide support if someone qualifies due to a covered critical, chronic, or terminal illness.",
    },
    {
      counter: "03 OF 06 • RETIREMENT PLANNING",
      badge: "Retirement guidance",
      category: "03 • Retirement Planning",
      shortQuestion: "“Preparing or just hoping?”",
      question: "“Am I preparing for retirement — or just hoping it works out?”",
      desc: "Many hardworking families save what they can, but still wonder if they are doing enough. Clear guidance can help them understand retirement options, possible risks, and steps that may support their long-term goals.",
    },
    {
      counter: "04 OF 06 • BUSINESS STRATEGIES",
      badge: "Business protection",
      category: "04 • Business Strategies",
      shortQuestion: "“What happens to my business?”",
      question: "“If something happened to me, what would happen to the business I built?”",
      desc: "Business owners carry responsibility for their family, employees, clients, and years of hard work. We help them understand protection options, including key-person coverage and business planning strategies that may strengthen their overall plan.",
    },
    {
      counter: "05 OF 06 • EDUCATION PLANNING",
      badge: "Education guidance",
      category: "05 • Education Planning",
      shortQuestion: "“Help my children with fewer limits?”",
      question: "“How can I help my children pursue education with fewer financial limits?”",
      desc: "Many parents want to support their children’s future, but they are not sure which education planning option gives the right balance of growth, flexibility, and control. Clear guidance can help families understand choices that may fit their goals.",
    },
    {
      counter: "06 OF 06 • LEGACY PLANNING",
      badge: "Legacy planning",
      category: "06 • Legacy Planning",
      shortQuestion: "“Will my family have clarity?”",
      question: "“Will my family receive clarity and support — or be left searching for help?”",
      desc: "Some families want to leave more than money. They want to leave direction, support, and a meaningful legacy for the people they love. A thoughtful plan can help reduce confusion and help loved ones know what to do next.",
    },
  ];

  const cardsEs = [
    {
      counter: "01 DE 06 • PROTECCIÓN FAMILIAR",
      badge: "Orientación con cuidado",
      category: "01 • Protección familiar",
      shortQuestion: "“Si mis ingresos se detuvieran mañana...”",
      question: "“Si mis ingresos se detuvieran mañana, ¿por cuánto tiempo estaría bien mi familia?”",
      desc: "Muchas familias tienen cierta cobertura a través del trabajo, pero no están seguras de si es suficiente o si permanecería con ellas si la vida cambiara. Una revisión sencilla puede ayudar a identificar posibles brechas, explicar opciones de protección disponibles y ayudar a las familias a entender qué puede ajustarse a sus necesidades, presupuesto y responsabilidades.",
    },
    {
      counter: "02 DE 06 • BENEFICIOS EN VIDA",
      badge: "Orientación sobre beneficios en vida",
      category: "02 • Beneficios en vida",
      shortQuestion: "“Si una enfermedad detuviera mis ingresos...”",
      question: "“¿Qué pasa si sobrevivo a la enfermedad, pero mis ingresos no?”",
      desc: "Una enfermedad grave puede afectar más que la salud. Puede afectar los ingresos, las facturas y todo el hogar. Algunas pólizas de seguro de vida pueden incluir beneficios en vida que pueden ayudar a brindar apoyo si alguien califica debido a una enfermedad crítica, crónica o terminal cubierta.",
    },
    {
      counter: "03 DE 06 • JUBILACIÓN",
      badge: "Orientación de jubilación",
      category: "03 • Planificación de jubilación",
      shortQuestion: "“¿Preparándome o solo esperando?”",
      question: "“¿Me estoy preparando para la jubilación, o solo espero que todo salga bien?”",
      desc: "Muchas familias trabajadoras ahorran lo que pueden, pero aún se preguntan si están haciendo lo suficiente. Una orientación clara puede ayudarles a entender opciones de jubilación, posibles riesgos y pasos que pueden apoyar sus metas a largo plazo.",
    },
    {
      counter: "04 DE 06 • ESTRATEGIAS PARA NEGOCIOS",
      badge: "Protección del negocio",
      category: "04 • Estrategias para negocios",
      shortQuestion: "“¿Qué pasa con mi negocio?”",
      question: "“Si algo me pasara, ¿qué ocurriría con el negocio que construí?”",
      desc: "Los dueños de negocios cargan responsabilidad por su familia, empleados, clientes y años de trabajo duro. Les ayudamos a entender opciones de protección, incluyendo cobertura para personas clave y estrategias de planificación empresarial que pueden fortalecer su plan general.",
    },
    {
      counter: "05 DE 06 • PLANIFICACIÓN EDUCATIVA",
      badge: "Orientación educativa",
      category: "05 • Planificación educativa",
      shortQuestion: "“¿Ayudar a mis hijos con menos límites?”",
      question: "“¿Cómo puedo ayudar a mis hijos a seguir su educación con menos límites financieros?”",
      desc: "Muchos padres quieren apoyar el futuro de sus hijos, pero no están seguros de qué opción de planificación educativa ofrece el equilibrio adecuado de crecimiento, flexibilidad y control. Una orientación clara puede ayudar a las familias a entender opciones que puedan ajustarse a sus metas.",
    },
    {
      counter: "06 DE 06 • PLANIFICACIÓN DE LEGADO",
      badge: "Planificación de legado",
      category: "06 • Planificación de legado",
      shortQuestion: "“¿Mi familia tendrá claridad?”",
      question: "“¿Mi familia recibirá claridad y apoyo, o quedará buscando ayuda?”",
      desc: "Algunas familias desean dejar más que dinero. Quieren dejar dirección, apoyo y un legado significativo para las personas que aman. Un plan bien pensado puede ayudar a reducir la confusión y ayudar a los seres queridos a saber qué hacer después.",
    },
  ];

  const cards = isEs ? cardsEs : cardsEn;
  const activeCard = cards[activeIdx];

  return (
    <section id="reviews" className="py-24 bg-[#F7F5F0] border-t border-b border-black/5 relative overflow-hidden">
      <div className="max-w-7xl mx-auto px-6 md:px-12 box-border">
        {/* Header Row */}
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 mb-12">
          <div>
            <span className="text-xs font-bold tracking-[3px] text-purple-900 uppercase flex items-center gap-2 mb-3">
              <span className="w-2 h-2 rounded-full bg-purple-900 inline-block" />
              {isEs ? "PREGUNTAS REALES" : "REAL QUESTIONS"}
            </span>
            <h2 className="text-4xl md:text-6xl font-extrabold text-gray-900 leading-tight">
              {isEs ? (
                <>Preguntas reales.<br /><span className="text-purple-900/60 font-serif italic">Orientación clara.</span></>
              ) : (
                <>Real Questions.<br /><span className="text-purple-900/60 font-serif italic">Clear Guidance.</span></>
              )}
            </h2>
          </div>
          <p className="max-w-xl text-gray-600 text-base font-light leading-relaxed">
            {isEs
              ? "Las familias no siempre llegan a nosotros con planes perfectos. Muchas vienen con preguntas, preocupaciones e incertidumbre. Nuestro papel es ayudarlas a entender sus opciones con claridad para que puedan tomar decisiones con confianza."
              : "Families do not always come to us with perfect plans. Many come with questions, concerns, and uncertainty. Our role is to help them understand their options clearly, so they can make decisions with confidence."}
          </p>
        </div>

        {/* Dashboard Grid (Left Tabs List + Right White Card Stage) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          {/* Left Column: 6 Clickable Selector Cards */}
          <div className="lg:col-span-5 flex flex-col gap-3">
            {cards.map((card, idx) => {
              const isActive = activeIdx === idx;
              return (
                <div
                  key={idx}
                  onClick={() => setActiveIdx(idx)}
                  className={`p-5 rounded-2xl cursor-pointer transition-all duration-200 border ${
                    isActive
                      ? "bg-purple-50/80 border-purple-900 shadow-sm border-l-4 border-l-purple-900"
                      : "bg-white border-gray-200/80 hover:border-purple-300"
                  }`}
                >
                  <div className="text-[11px] font-bold text-purple-900 tracking-wider uppercase mb-1.5">
                    {card.category}
                  </div>
                  <div className="text-sm md:text-base font-bold text-gray-900 leading-snug">
                    {card.shortQuestion}
                  </div>
                  <div className="flex items-center gap-2 mt-2.5">
                    <span className="w-1.5 h-1.5 rounded-full bg-purple-900 inline-block" />
                    <span className="text-[11px] font-semibold text-gray-500">
                      {card.badge}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Right Column: Display Stage (Large White Card) */}
          <div className="lg:col-span-7 bg-white border border-black/5 rounded-3xl p-8 md:p-12 shadow-lg relative min-h-[380px] flex flex-col justify-between">
            <div>
              <div className="flex flex-wrap justify-between items-center gap-2 mb-6">
                <span className="text-xs font-bold tracking-widest text-purple-900 uppercase">
                  {activeCard.counter}
                </span>
                <span className="bg-purple-900/10 text-purple-900 px-3.5 py-1 rounded-full text-xs font-semibold">
                  {activeCard.badge}
                </span>
              </div>

              <h3 className="text-2xl md:text-4xl font-extrabold text-gray-900 leading-snug mb-6">
                {activeCard.question}
              </h3>

              <p className="text-gray-600 text-base leading-relaxed font-light mb-8">
                {activeCard.desc}
              </p>
            </div>

            <div>
              <Link
                href={isEs ? "/es#contact" : "/#contact"}
                className="bg-purple-900 hover:bg-purple-800 text-white font-bold px-8 py-3.5 rounded-full text-xs inline-flex items-center gap-2 transition-all shadow-md"
              >
                {isEs ? "Comienza con una revisión sencilla" : "Start with a Simple Review"}
                <ArrowRight className="w-4 h-4" />
              </Link>
            </div>
          </div>
        </div>

        {/* Disclaimer Text */}
        <p className="text-xs text-gray-400 mt-10 text-center font-light">
          {isEs
            ? "Estos ejemplos son solo para fines educativos y muestran preocupaciones comunes que las familias pueden enfrentar. Las necesidades, elegibilidad y resultados individuales pueden variar."
            : "These examples are for educational purposes and show common concerns families may face. Individual needs, eligibility, and results may vary."}
        </p>
      </div>
    </section>
  );
}
