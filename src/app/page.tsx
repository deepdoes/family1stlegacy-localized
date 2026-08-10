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

export default function HomePage() {
  return (
    <main className="min-h-screen bg-[#F4F2F6]">
      <Navbar lang="en" />
      <HeroSlider lang="en" />
      <Marquee />
      <WhoWeAre lang="en" />
      <HowWeCanHelp lang="en" />
      <NumbersBand />
      <FourSteps lang="en" />
      <RealQuestions lang="en" />
      <FAQAccordion lang="en" />
      <ContactForm lang="en" />
      <Footer lang="en" />
    </main>
  );
}
