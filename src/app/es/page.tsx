import Navbar from "@/components/layout/Navbar";
import HeroSlider from "@/components/home/HeroSlider";
import Marquee from "@/components/home/Marquee";
import WhoWeAre from "@/components/home/WhoWeAre";
import HowWeCanHelp from "@/components/home/HowWeCanHelp";
import NumbersBand from "@/components/home/NumbersBand";
import FourSteps from "@/components/home/FourSteps";
import RealQuestions from "@/components/home/RealQuestions";
import ContactForm from "@/components/home/ContactForm";
import FAQAccordion from "@/components/home/FAQAccordion";
import Footer from "@/components/layout/Footer";

export default function SpanishHomePage() {
  return (
    <main className="min-h-screen bg-[#F4F2F6]">
      <Navbar lang="es" />
      <HeroSlider lang="es" />
      <Marquee />
      <WhoWeAre lang="es" />
      <HowWeCanHelp lang="es" />
      <NumbersBand />
      <FourSteps lang="es" />
      <RealQuestions lang="es" />
      <FAQAccordion lang="es" />
      <ContactForm lang="es" />
      <Footer lang="es" />
    </main>
  );
}
