import React from "react";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import ContactForm from "@/components/home/ContactForm";

export default function BusinessStrategiesPage() {
  return (
    <main className="min-h-screen bg-white pt-24">
      <Navbar lang="en" />
      <div className="max-w-7xl mx-auto px-6 md:px-12 py-16">
        <span className="text-xs font-bold tracking-[3px] text-purple-900 uppercase block mb-3">
          BUSINESS STRATEGIES
        </span>
        <h1 className="text-4xl md:text-6xl font-extrabold text-gray-900 leading-tight mb-6">
          Protect the Business You Built
        </h1>
        <p className="text-lg text-gray-600 font-light leading-relaxed max-w-3xl mb-12">
          You worked hard to build your business. From key-person coverage and buy-sell planning to executive benefits and succession strategies, we help business owners explore ways to protect what they have created.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 my-12">
          <div className="bg-purple-50 p-8 rounded-3xl border border-purple-100">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">Key-Person Protection</h3>
            <p className="text-gray-600 leading-relaxed font-light">
              Help protect your business against the financial impact of losing a critical leader or key income producer.
            </p>
          </div>
          <div className="bg-purple-50 p-8 rounded-3xl border border-purple-100">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">Buy-Sell & Succession Planning</h3>
            <p className="text-gray-600 leading-relaxed font-light">
              Ensure a smooth transition of ownership and protect business continuity if a partner steps down, retires, or passes away.
            </p>
          </div>
        </div>
      </div>
      <ContactForm lang="en" />
      <Footer lang="en" />
    </main>
  );
}
