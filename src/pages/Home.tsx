import React from 'react';
import { HeroSlider, QuickActions } from '@/components/sections/HeroAndActions';
import { AboutSection, ServicesSection, TowingServicesHomeSection } from '@/components/sections/AboutAndServices';
import { HaulageHomeSection } from '@/components/sections/HaulageSection';
import { AutoParts, WhyChooseUs } from '@/components/sections/PartsAndWhyUs';
import { FAQ, BlogSection } from '@/components/sections/BottomSections';
import SEO from '@/components/seo/SEO';

export default function Home() {
  return (
    <main>
      <SEO title="Pexus | 24/7 Towing, Haulage & Repairs in Ghana" description="Expert 24/7 emergency towing, nationwide haulage & heavy machinery transport, professional auto repairs, and auto parts in Ghana." canonical="/" />
      <HeroSlider />
      <QuickActions />
      <AboutSection />
      <ServicesSection />
      <TowingServicesHomeSection />
      <HaulageHomeSection />
      <AutoParts />
      <WhyChooseUs />
      <BlogSection />
      <FAQ />
    </main>
  );
}
