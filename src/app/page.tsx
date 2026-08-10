import React from "react";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import HeroSlider from "@/components/home/HeroSlider";
import WhoWeAre from "@/components/home/WhoWeAre";
import HowWeCanHelp from "@/components/home/HowWeCanHelp";
import RealQuestions from "@/components/home/RealQuestions";
import FourSteps from "@/components/home/FourSteps";
import FAQAccordion from "@/components/home/FAQAccordion";
import ContactForm from "@/components/home/ContactForm";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-white">
      <Navbar lang="en" />
      <HeroSlider lang="en" />
      <WhoWeAre lang="en" />
      <HowWeCanHelp lang="en" />
      <RealQuestions lang="en" />
      <FourSteps lang="en" />
      <FAQAccordion lang="en" />
      <ContactForm lang="en" />
      <Footer lang="en" />
    </main>
  );
}
