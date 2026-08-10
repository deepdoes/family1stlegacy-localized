"use client";

import React, { useState } from "react";
import Link from "next/link";
import { ArrowRight, CheckCircle2 } from "lucide-react";

interface RealQuestionsProps {
  lang: "en" | "es";
}

export default function RealQuestions({ lang }: RealQuestionsProps) {
  const [activeIdx, setActiveIdx] = useState(0);
  const isEs = lang === "es";

  const cardsEn = [
    {
      counter: "01 of 06 - Family Protection",
      badge: "Guidance with care",
      category: "Family Protection",
      shortQuestion: "“If my income stopped tomorrow...”",
      question: "“If my income stopped tomorrow, how long would my family be okay?”",
      desc: "Many families have some coverage through work, but they are not sure if it is enough — or if it would stay with them if life changed. A simple review can help identify possible gaps, explain available protection options, and help families understand what may fit their needs, budget, and responsibilities.",
    },
    {
      counter: "02 of 06 - Living Benefits",
      badge: "Living benefits guidance",
      category: "Living Benefits",
      shortQuestion: "“If illness stopped my income...”",
      question: "“What if I survive the illness — but my income does not?”",
      desc: "A serious illness can affect more than health. It can affect income, bills, and the whole household. Some life insurance policies may include living benefits that can help provide support if someone qualifies due to a covered critical, chronic, or terminal illness.",
    },
    {
      counter: "03 of 06 - Retirement Planning",
      badge: "Retirement guidance with care",
      category: "Retirement Planning",
      shortQuestion: "“Preparing or just hoping?”",
      question: "“Am I preparing for retirement — or just hoping it works out?”",
      desc: "Many hardworking families save what they can, but still wonder if they are doing enough. Clear guidance can help them understand retirement options, possible risks, and steps that may support their long-term goals.",
    },
    {
      counter: "04 of 06 - Business Strategies",
      badge: "Business protection guidance",
      category: "Business Strategies",
      shortQuestion: "“What happens to my business?”",
      question: "“If something happened to me, what would happen to the business I built?”",
      desc: "Business owners carry responsibility for their family, employees, clients, and years of hard work. We help them understand protection options, including key-person coverage and business planning strategies that may strengthen their overall plan.",
    },
    {
      counter: "05 of 06 - Education Planning",
      badge: "Education planning guidance",
      category: "Education Planning",
      shortQuestion: "“Help my children with fewer limits?”",
      question: "“How can I help my children pursue education with fewer financial limits?”",
      desc: "Many parents want to support their children’s future, but they are not sure which education planning option gives the right balance of growth, flexibility, and control. Clear guidance can help families understand choices that may fit their goals.",
    },
    {
      counter: "06 of 06 - Legacy Planning",
      badge: "Legacy planning guidance",
      category: "Legacy Planning",
      shortQuestion: "“Will my family have clarity?”",
      question: "“Will my family receive clarity and support — or be left searching for help?”",
      desc: "Some families want to leave more than money. They want to leave direction, support, and a meaningful legacy for the people they love. A thoughtful plan can help reduce confusion and help loved ones know what to do next.",
    },
  ];

  const cardsEs = [
    {
      counter: "01 de 06 - Protección familiar",
      badge: "Orientación con cuidado",
      category: "Protección familiar",
      shortQuestion: "“Si mis ingresos se detuvieran mañana...”",
      question: "“Si mis ingresos se detuvieran mañana, ¿por cuánto tiempo estaría bien mi familia?”",
      desc: "Muchas familias tienen cierta cobertura a través del trabajo, pero no están seguras de si es suficiente o si permanecería con ellas si la vida cambiara. Una revisión sencilla puede ayudar a identificar posibles brechas, explicar opciones de protección disponibles y ayudar a las familias a entender qué puede ajustarse a sus necesidades, presupuesto y responsabilidades.",
    },
    {
      counter: "02 de 06 - Beneficios en vida",
      badge: "Orientación sobre beneficios en vida",
      category: "Beneficios en vida",
      shortQuestion: "“Si una enfermedad detuviera mis ingresos...”",
      question: "“¿Qué pasa si sobrevivo a la enfermedad, pero mis ingresos no?”",
      desc: "Una enfermedad grave puede afectar más que la salud. Puede afectar los ingresos, las facturas y todo el hogar. Algunas pólizas de seguro de vida pueden incluir beneficios en vida que pueden ayudar a brindar apoyo si alguien califica debido a una enfermedad crítica, crónica o terminal cubierta.",
    },
    {
      counter: "03 de 06 - Planificación para la jubilación",
      badge: "Orientación de jubilación con cuidado",
      category: "Planificación para la jubilación",
      shortQuestion: "“¿Preparándome o solo esperando?”",
      question: "“¿Me estoy preparando para la jubilación, o solo espero que todo salga bien?”",
      desc: "Muchas familias trabajadoras ahorran lo que pueden, pero aún se preguntan si están haciendo lo suficiente. Una orientación clara puede ayudarles a entender opciones de jubilación, posibles riesgos y pasos que pueden apoyar sus metas a largo plazo.",
    },
    {
      counter: "04 de 06 - Estrategias para negocios",
      badge: "Orientación para proteger el negocio",
      category: "Estrategias para negocios",
      shortQuestion: "“¿Qué pasa con mi negocio?”",
      question: "“Si algo me pasara, ¿qué ocurriría con el negocio que construí?”",
      desc: "Los dueños de negocios cargan responsabilidad por su familia, empleados, clientes y años de trabajo duro. Les ayudamos a entender opciones de protección, incluyendo cobertura para personas clave y estrategias de planificación empresarial que pueden fortalecer su plan general.",
    },
    {
      counter: "05 de 06 - Planificación educativa",
      badge: "Orientación de planificación educativa",
      category: "Planificación educativa",
      shortQuestion: "“¿Ayudar a mis hijos con menos límites?”",
      question: "“¿Cómo puedo ayudar a mis hijos a seguir su educación con menos límites financieros?”",
      desc: "Muchos padres quieren apoyar el futuro de sus hijos, pero no están seguros de qué opción de planificación educativa ofrece el equilibrio adecuado de crecimiento, flexibilidad y control. Una orientación clara puede ayudar a las familias a entender opciones que puedan ajustarse a sus metas.",
    },
    {
      counter: "06 de 06 - Planificación de legado",
      badge: "Orientación de planificación de legado",
      category: "Planificación de legado",
      shortQuestion: "“¿Mi familia tendrá claridad?”",
      question: "“¿Mi familia recibirá claridad y apoyo, o quedará buscando ayuda?”",
      desc: "Algunas familias desean dejar más que dinero. Quieren dejar dirección, apoyo y un legado significativo para las personas que aman. Un plan bien pensado puede ayudar a reducir la confusión y ayudar a los seres queridos a saber qué hacer después.",
    },
  ];

  const cards = isEs ? cardsEs : cardsEn;
  const activeCard = cards[activeIdx];

  return (
    <section id="reviews" className="py-24 bg-[#F4F2F6] relative">
      <div className="max-w-7xl mx-auto px-6 md:px-12 box-border">
        {/* Top Purple Featured Box */}
        <div className="bg-gradient-to-br from-[#3A2060] to-[#201238] rounded-3xl p-8 md:p-14 text-white relative overflow-hidden shadow-2xl mb-10">
          <div className="absolute -top-24 -right-24 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl pointer-events-none" />

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start relative z-10">
            {/* Left Column Intro */}
            <div className="lg:col-span-5">
              <span className="text-xs font-bold tracking-[3px] text-purple-300 uppercase block mb-3">
                {isEs ? "PREGUNTAS REALES" : "REAL QUESTIONS"}
              </span>
              <h2 className="text-3xl md:text-5xl font-extrabold text-white leading-tight mb-5">
                {isEs ? (
                  <>Preguntas reales.<br />Orientación clara.</>
                ) : (
                  <>Real Questions.<br />Clear Guidance.</>
                )}
              </h2>
              <p className="text-white/80 text-base leading-relaxed font-light">
                {isEs
                  ? "Las familias no siempre llegan a nosotros con planes perfectos. Muchas vienen con preguntas, preocupaciones e incertidumbre. Nuestro papel es ayudarlas a entender sus opciones con claridad para que puedan tomar decisiones con confianza."
                  : "Families do not always come to us with perfect plans. Many come with questions, concerns, and uncertainty. Our role is to help them understand their options clearly, so they can make decisions with confidence."}
              </p>
            </div>

            {/* Right Column Featured Card Display */}
            <div className="lg:col-span-7 bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-6 md:p-10 flex flex-col justify-between min-h-[320px] transition-all duration-300">
              <div>
                <div className="flex justify-between items-center mb-4">
                  <span className="text-xs font-bold text-amber-300 tracking-wider">
                    {activeCard.counter}
                  </span>
                  <span className="bg-white/10 border border-white/20 px-3 py-1 rounded-full text-xs font-medium text-white">
                    {activeCard.badge}
                  </span>
                </div>
                <h3 className="text-xl md:text-2xl font-bold text-white leading-snug mb-4">
                  {activeCard.question}
                </h3>
                <p className="text-white/80 text-sm md:text-base leading-relaxed font-light mb-8">
                  {activeCard.desc}
                </p>
              </div>

              <div>
                <Link
                  href={isEs ? "/es#contact" : "/#contact"}
                  className="bg-white hover:bg-purple-50 text-gray-900 font-bold px-6 py-3 rounded-full text-sm inline-flex items-center gap-2 transition-all shadow-md"
                >
                  {isEs ? "Comienza con una revisión sencilla" : "Start with a Simple Review"}
                  <ArrowRight className="w-4 h-4" />
                </Link>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom 6 Clickable Preview Cards */}
        <div className="bg-white border border-gray-200 rounded-3xl p-6 md:p-12 shadow-sm">
          <div className="text-center mb-8">
            <span className="text-xs font-bold tracking-widest text-purple-900 uppercase block mb-2">
              {isEs ? "PREOCUPACIONES COMUNES" : "COMMON CONCERNS"}
            </span>
            <h3 className="text-2xl font-bold text-gray-900">
              {isEs ? "Preocupaciones que las familias nos traen" : "Concerns Families Bring to Us"}
            </h3>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {cards.map((card, idx) => (
              <div
                key={idx}
                onClick={() => setActiveIdx(idx)}
                className={`p-6 rounded-2xl cursor-pointer transition-all duration-200 border ${
                  activeIdx === idx
                    ? "bg-purple-50 border-purple-900 border-2 shadow-sm"
                    : "bg-gray-50/50 border-gray-200 hover:border-purple-300"
                }`}
              >
                <div className="text-xs font-bold text-purple-900 uppercase tracking-wide mb-1">
                  {card.category}
                </div>
                <div className="text-sm font-semibold text-gray-900 mb-3 line-clamp-2">
                  {card.shortQuestion}
                </div>
                <span className="text-[11px] bg-purple-900/10 text-purple-900 px-2.5 py-1 rounded-md font-semibold">
                  {card.badge}
                </span>
              </div>
            ))}
          </div>

          <p className="text-xs text-gray-400 mt-8 text-center italic">
            {isEs
              ? "Estos ejemplos son solo para fines educativos y muestran preocupaciones comunes que las familias pueden enfrentar. Las necesidades, elegibilidad y resultados individuales pueden variar."
              : "These examples are for educational purposes and show common concerns families may face. Individual needs, eligibility, and results may vary."}
          </p>
        </div>
      </div>
    </section>
  );
}
