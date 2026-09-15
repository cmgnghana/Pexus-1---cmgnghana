import os

new_home_content = """import React, { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Link } from 'react-router-dom';
import { ChevronRight, ArrowRight, Play, CheckCircle, Quote, Star, Phone, MapPin, Truck, Wrench, Battery, ShieldCheck, HelpCircle, ChevronDown, Calendar, User } from 'lucide-react';
import { cn } from '@/lib/utils';
import SEO from '@/components/seo/SEO';

// Data
const SERVICES = [
  { title: 'Emergency Towing', desc: '24/7 rapid response for breakdowns and accidents.', icon: Truck, img: 'https://i.ibb.co/gZh5x06r/Image-1-Towing-Vehicle.jpg' },
  { title: 'Heavy Duty Haulage', desc: 'Safe transport for industrial equipment and containers.', icon: Truck, img: 'https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&w=800&q=80' },
  { title: 'Auto Repairs', desc: 'Comprehensive mechanical repairs and diagnostics.', icon: Wrench, img: 'https://i.ibb.co/WpNkptMZ/Image-4-Van-Hyundai-H1-2022.jpg' },
  { title: 'Genuine Parts', desc: 'OEM replacement parts and quality accessories.', icon: Battery, img: 'https://i.ibb.co/3998gkTG/Image-16-Accessories.jpg' }
];

const SKILLS = [
  { name: 'Emergency Towing', percent: 98 },
  { name: 'Auto Body Works', percent: 95 },
  { name: 'Heavy Duty Haulage', percent: 90 },
  { name: 'Customer Satisfaction', percent: 99 }
];

const PROCESS = [
  { id: 1, title: 'Initial Call', desc: 'Contact our 24/7 dispatch center with your location.' },
  { id: 2, title: 'Rapid Dispatch', desc: 'The nearest appropriate vehicle is immediately dispatched.' },
  { id: 3, title: 'Professional Service', desc: 'Our experts handle the recovery or repair safely.' },
  { id: 4, title: 'Back on the Road', desc: 'You are safely on your way to your destination.' }
];

const TEAM = [
  { name: 'David Mensah', role: 'Chief Mechanic', img: 'https://images.unsplash.com/photo-1530268729831-4b0b9e170218?auto=format&fit=crop&w=400&q=80' },
  { name: 'Kwesi Appiah', role: 'Lead Recovery Expert', img: 'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=400&q=80' },
  { name: 'Sarah Osei', role: 'Dispatch Manager', img: 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80' },
  { name: 'Michael Addo', role: 'Haulage Specialist', img: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80' }
];

const BLOGS = [
  { title: 'What to Do When Your Car Overheats in Traffic', date: 'May 15, 2024', author: 'David Mensah', img: 'https://images.unsplash.com/photo-1486495371522-87ff8178d052?auto=format&fit=crop&w=600&q=80' },
  { title: 'The Importance of Regular Brake Maintenance', date: 'May 02, 2024', author: 'Kwesi Appiah', img: 'https://images.unsplash.com/photo-1503376712351-1f5be669d660?auto=format&fit=crop&w=600&q=80' },
  { title: 'Choosing the Right Battery for Your Vehicle', date: 'April 18, 2024', author: 'Sarah Osei', img: 'https://i.ibb.co/3998gkTG/Image-16-Accessories.jpg' }
];

const FAQS = [
  { q: 'How quickly can you respond to an emergency?', a: 'We guarantee a response time of 30-45 minutes within the Greater Accra region, depending on traffic conditions.' },
  { q: 'Do you offer 24/7 towing services?', a: 'Yes, our emergency towing and roadside assistance teams operate 24 hours a day, 7 days a week, 365 days a year.' },
  { q: 'What types of vehicles can you tow?', a: 'We have a diverse fleet capable of towing everything from motorcycles and sedans to SUVs, commercial vans, and heavy-duty trucks.' },
  { q: 'Do you provide warranties on repairs?', a: 'Yes, all our mechanical repairs and body works come with a standard 90-day warranty on labor and parts.' }
];

export default function Home() {
  const [openFaq, setOpenFaq] = useState<number | null>(0);

  return (
    <main className="bg-white overflow-hidden">
      <SEO title="Pexus | 24/7 Towing, Haulage & Repairs in Ghana" description="Expert 24/7 emergency towing, nationwide haulage & heavy machinery transport, professional auto repairs, and auto parts in Ghana." canonical="/" />

      {/* 1. HERO SECTION */}
      <section className="relative min-h-[90vh] flex items-center pt-24 pb-16 lg:pt-32">
        <div className="absolute inset-0 z-0">
          <img src="https://images.unsplash.com/photo-1519003722824-194d4455a60c?auto=format&fit=crop&w=1920&q=80" alt="Hero Background" className="w-full h-full object-cover" />
          <div className="absolute inset-0 bg-gradient-to-r from-[#111835]/95 via-[#111835]/80 to-transparent" />
        </div>
        
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full flex flex-col lg:flex-row items-center justify-between">
          <div className="w-full lg:w-3/5 text-white">
            <div className="inline-flex items-center gap-2 px-3 py-1 bg-accent/20 border border-accent/30 rounded-full text-accent text-xs font-bold uppercase tracking-wider mb-6">
              <span className="w-2 h-2 rounded-full bg-accent animate-pulse" />
              Delivering Smarter Logistics Solutions
            </div>
            <h1 className="text-4xl md:text-5xl lg:text-7xl font-extrabold leading-[1.1] mb-6">
              Moving Made Easy,<br />Wherever Life<br />Takes You!
            </h1>
            <p className="text-lg text-white/80 max-w-xl mb-8 leading-relaxed">
              We handle home relocations, office moves, and specialty transport with care and efficiency making your move simple, safe, and stress-free.
            </p>
            <div className="flex flex-wrap items-center gap-6">
              <Link to="/contact" className="bg-accent hover:bg-accent/90 text-white px-8 py-4 font-bold rounded-[1px] transition-all flex items-center gap-2">
                Contact Us <ArrowRight className="w-5 h-5" />
              </Link>
              <div className="flex items-center gap-4">
                <div className="flex -space-x-3">
                  <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=100&q=80" className="w-12 h-12 rounded-full border-2 border-[#111835] object-cover" alt="Customer" />
                  <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=100&q=80" className="w-12 h-12 rounded-full border-2 border-[#111835] object-cover" alt="Customer" />
                  <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=100&q=80" className="w-12 h-12 rounded-full border-2 border-[#111835] object-cover" alt="Customer" />
                  <div className="w-12 h-12 rounded-full border-2 border-[#111835] bg-accent flex items-center justify-center text-white font-bold text-xs">4.9+</div>
                </div>
                <div className="flex flex-col">
                  <span className="font-bold text-white">Satisfied Customers</span>
                  <span className="text-white/70 text-sm">4.9/5 (10k+ Reviews)</span>
                </div>
              </div>
            </div>
          </div>
          
          <div className="hidden lg:block w-full lg:w-2/5 relative h-full min-h-[500px]">
            <div className="absolute bottom-10 right-0 bg-white p-6 rounded-[1px] shadow-2xl max-w-xs flex items-center gap-4 animate-bounce-slow">
              <div className="w-16 h-16 bg-slate-100 rounded flex items-center justify-center shrink-0">
                <Truck className="w-8 h-8 text-accent" />
              </div>
              <div>
                <h4 className="font-bold text-slate-900 text-lg leading-tight mb-1">Global shipment<br />made easy.</h4>
                <a href="/contact" className="text-accent text-sm font-bold flex items-center gap-1 hover:underline">Track Shipment <ChevronRight className="w-4 h-4" /></a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 2. ABOUT SECTION */}
      <section className="py-20 lg:py-28 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col lg:flex-row items-center gap-16">
            <div className="w-full lg:w-1/2">
              <div className="inline-flex items-center gap-2 text-accent font-bold uppercase tracking-wider text-sm mb-4">
                <span className="w-8 h-0.5 bg-accent" /> About Us <span className="w-8 h-0.5 bg-accent" />
              </div>
              <h2 className="text-3xl md:text-5xl font-extrabold text-slate-900 mb-6 leading-[1.2]">
                Driven by Trust, Powered<br />by Experience.
              </h2>
              <p className="text-slate-600 mb-8 leading-relaxed text-lg">
                We deliver reliable logistics solutions that connect businesses and individuals across the globe, ensuring efficiency, safety, and trust in every move.
              </p>
              
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-8 mb-10">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center shrink-0">
                    <MapPin className="w-6 h-6 text-accent" />
                  </div>
                  <div>
                    <h4 className="font-bold text-slate-900 mb-1">Worldwide Service</h4>
                    <p className="text-slate-500 text-sm">Seamless logistics coverage across countries and continents.</p>
                  </div>
                </div>
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center shrink-0">
                    <Phone className="w-6 h-6 text-accent" />
                  </div>
                  <div>
                    <h4 className="font-bold text-slate-900 mb-1">24/7 Online Support</h4>
                    <p className="text-slate-500 text-sm">Always available to assist you, day or night.</p>
                  </div>
                </div>
              </div>
              
              <div className="flex items-center gap-8">
                <Link to="/about" className="bg-accent hover:bg-accent/90 text-white px-8 py-4 font-bold rounded-[1px] transition-all flex items-center gap-2">
                  Read More <ArrowRight className="w-5 h-5" />
                </Link>
                <div className="flex items-center gap-4">
                  <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=100&q=80" className="w-14 h-14 rounded-full object-cover" alt="Founder" />
                  <div>
                    <h5 className="font-bold text-slate-900">Chris Vlasek</h5>
                    <p className="text-slate-500 text-sm">Co Founder</p>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="w-full lg:w-1/2 relative">
              <div className="relative rounded-[1px] overflow-hidden">
                <img src="https://images.unsplash.com/photo-1581092334651-ddf26d9a09d0?auto=format&fit=crop&w=800&q=80" alt="About Us" className="w-full h-auto object-cover" />
              </div>
              <div className="absolute top-1/2 -left-10 -translate-y-1/2 w-32 h-32 bg-white rounded-full flex items-center justify-center shadow-2xl p-2 z-10 hidden sm:flex border border-slate-100">
                <div className="w-full h-full border-2 border-dashed border-accent rounded-full flex items-center justify-center flex-col text-accent">
                  <ArrowRight className="w-6 h-6 -rotate-45" />
                  <span className="text-[10px] font-bold uppercase tracking-widest mt-1">Explore</span>
                  <span className="text-[10px] font-bold uppercase tracking-widest">More</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 3. SERVICES SECTION */}
      <section className="py-20 lg:py-28 bg-slate-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <div className="inline-flex items-center justify-center gap-2 text-accent font-bold uppercase tracking-wider text-sm mb-4">
              <span className="w-8 h-0.5 bg-accent" /> Services <span className="w-8 h-0.5 bg-accent" />
            </div>
            <h2 className="text-3xl md:text-4xl font-extrabold text-slate-900 mb-6">
              Our Trusted<br />Logistics Services
            </h2>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {SERVICES.map((srv, idx) => (
              <div key={idx} className="bg-white rounded-[1px] shadow-sm hover:shadow-xl transition-all group overflow-hidden border border-slate-100">
                <div className="h-48 overflow-hidden relative">
                  <img src={srv.img} alt={srv.title} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />
                  <div className="absolute top-4 left-4 w-12 h-12 bg-white flex items-center justify-center rounded-[1px] shadow-md z-10 text-accent group-hover:bg-accent group-hover:text-white transition-colors">
                    <srv.icon className="w-6 h-6" />
                  </div>
                </div>
                <div className="p-6">
                  <h3 className="font-bold text-slate-900 text-xl mb-3 group-hover:text-accent transition-colors">{srv.title}</h3>
                  <p className="text-slate-500 text-sm mb-6 leading-relaxed">{srv.desc}</p>
                  <Link to="/services" className="inline-flex items-center gap-2 text-accent font-bold text-sm uppercase tracking-wider hover:text-slate-900 transition-colors">
                    Read More <ArrowRight className="w-4 h-4" />
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 4. SKILLS SECTION */}
      <section className="py-20 lg:py-28 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col lg:flex-row items-center gap-16">
            <div className="w-full lg:w-1/2">
              <div className="inline-flex items-center gap-2 text-accent font-bold uppercase tracking-wider text-sm mb-4">
                <span className="w-8 h-0.5 bg-accent" /> Our Skills <span className="w-8 h-0.5 bg-accent" />
              </div>
              <h2 className="text-3xl md:text-4xl font-extrabold text-slate-900 mb-6">
                Skills That Keep Your<br />Business Moving.
              </h2>
              <p className="text-slate-600 mb-8 leading-relaxed">
                At Pexus, we bring together proven expertise and modern technology to ensure every move is seamless. From planning and tracking to storage and customer care.
              </p>
              
              <div className="space-y-6">
                {SKILLS.map((skill, idx) => (
                  <div key={idx}>
                    <div className="flex justify-between items-end mb-2">
                      <span className="font-bold text-slate-900">{skill.name}</span>
                      <span className="font-bold text-slate-900">{skill.percent}%</span>
                    </div>
                    <div className="h-2.5 w-full bg-slate-100 rounded-full overflow-hidden">
                      <motion.div 
                        initial={{ width: 0 }}
                        whileInView={{ width: `${skill.percent}%` }}
                        viewport={{ once: true }}
                        transition={{ duration: 1.5, delay: 0.2 }}
                        className="h-full bg-accent rounded-full"
                      />
                    </div>
                  </div>
                ))}
              </div>
              
              <div className="mt-10">
                <Link to="/about" className="bg-accent hover:bg-accent/90 text-white px-8 py-4 font-bold rounded-[1px] transition-all inline-flex items-center gap-2">
                  Read More <ArrowRight className="w-5 h-5" />
                </Link>
              </div>
            </div>
            
            <div className="w-full lg:w-1/2">
              <img src="https://i.ibb.co/gZh5x06r/Image-1-Towing-Vehicle.jpg" alt="Skills" className="w-full h-auto rounded-[1px] shadow-2xl" />
            </div>
          </div>
        </div>
      </section>

      {/* 5. PROCESS SECTION */}
      <section className="py-20 bg-slate-50 border-y border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <div className="inline-flex items-center justify-center gap-2 text-accent font-bold uppercase tracking-wider text-sm mb-4">
              <span className="w-8 h-0.5 bg-accent" /> Working Process <span className="w-8 h-0.5 bg-accent" />
            </div>
            <h2 className="text-3xl md:text-4xl font-extrabold text-slate-900 mb-6">
              Our Seamless Moving<br />Process.
            </h2>
          </div>
          
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 relative">
            <div className="hidden lg:block absolute top-12 left-[10%] right-[10%] h-0.5 border-t-2 border-dashed border-slate-300 z-0" />
            {PROCESS.map((proc, idx) => (
              <div key={idx} className="relative z-10 flex flex-col items-center text-center group">
                <div className="w-24 h-24 bg-white border-4 border-slate-50 rounded-full flex items-center justify-center text-accent shadow-xl mb-6 group-hover:bg-accent group-hover:text-white transition-colors duration-300">
                  <span className="text-2xl font-black">{proc.id}</span>
                </div>
                <h3 className="font-bold text-slate-900 text-xl mb-3">{proc.title}</h3>
                <p className="text-slate-500 text-sm leading-relaxed">{proc.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 6. TESTIMONIALS SECTION */}
      <section className="py-20 lg:py-28 bg-[#111835] text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col lg:flex-row gap-16">
            <div className="w-full lg:w-1/3">
              <div className="inline-flex items-center gap-2 text-accent font-bold uppercase tracking-wider text-sm mb-4">
                <span className="w-8 h-0.5 bg-accent" /> Testimonial <span className="w-8 h-0.5 bg-accent" />
              </div>
              <h2 className="text-3xl md:text-4xl font-extrabold mb-6">
                Hear From Our Happy<br />Clients
              </h2>
              <p className="text-white/70 mb-8 leading-relaxed">
                Don't just take our word for it. See what our satisfied customers have to say about our logistics and towing services.
              </p>
              <div className="flex items-center gap-4">
                <button className="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center hover:bg-accent hover:border-accent transition-colors">
                  <ChevronRight className="w-5 h-5 rotate-180" />
                </button>
                <button className="w-12 h-12 rounded-full bg-accent flex items-center justify-center text-white hover:bg-white hover:text-accent transition-colors">
                  <ChevronRight className="w-5 h-5" />
                </button>
              </div>
            </div>
            
            <div className="w-full lg:w-2/3 grid grid-cols-1 md:grid-cols-2 gap-6">
              {[1, 2].map((i) => (
                <div key={i} className="bg-white/5 border border-white/10 p-8 rounded-[1px] relative">
                  <Quote className="absolute top-6 right-6 w-12 h-12 text-white/10" />
                  <div className="flex items-center gap-1 mb-6 text-accent">
                    <Star className="w-4 h-4 fill-current" /><Star className="w-4 h-4 fill-current" /><Star className="w-4 h-4 fill-current" /><Star className="w-4 h-4 fill-current" /><Star className="w-4 h-4 fill-current" />
                  </div>
                  <p className="text-white/80 leading-relaxed mb-8 italic">
                    "The service was incredibly fast and professional. When my truck broke down on the highway, their recovery team arrived within 30 minutes. Highly recommended!"
                  </p>
                  <div className="flex items-center gap-4">
                    <div className="w-12 h-12 rounded-full bg-slate-300"></div>
                    <div>
                      <h5 className="font-bold text-white">John Doe</h5>
                      <span className="text-accent text-sm">Transport Manager</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* 7. TEAM SECTION */}
      <section className="py-20 lg:py-28 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <div className="inline-flex items-center justify-center gap-2 text-accent font-bold uppercase tracking-wider text-sm mb-4">
              <span className="w-8 h-0.5 bg-accent" /> Our Team Members <span className="w-8 h-0.5 bg-accent" />
            </div>
            <h2 className="text-3xl md:text-4xl font-extrabold text-slate-900 mb-6">
              Meet the Experts Behind<br />Pexus
            </h2>
          </div>
          
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            {TEAM.map((member, idx) => (
              <div key={idx} className="group">
                <div className="relative overflow-hidden rounded-[1px] mb-4">
                  <img src={member.img} alt={member.name} className="w-full h-[300px] object-cover group-hover:scale-105 transition-transform duration-500" />
                  <div className="absolute bottom-4 right-4 bg-white p-2 flex flex-col gap-2 rounded-[1px] opacity-0 group-hover:opacity-100 transition-opacity duration-300 translate-y-4 group-hover:translate-y-0">
                    <a href="#" className="w-8 h-8 flex items-center justify-center bg-slate-100 hover:bg-accent hover:text-white rounded text-slate-600 transition-colors"><Facebook className="w-4 h-4" /></a>
                    <a href="#" className="w-8 h-8 flex items-center justify-center bg-slate-100 hover:bg-accent hover:text-white rounded text-slate-600 transition-colors"><Twitter className="w-4 h-4" /></a>
                    <a href="#" className="w-8 h-8 flex items-center justify-center bg-slate-100 hover:bg-accent hover:text-white rounded text-slate-600 transition-colors"><Linkedin className="w-4 h-4" /></a>
                  </div>
                </div>
                <div className="bg-white border-b-2 border-slate-100 group-hover:border-accent transition-colors pb-4 flex justify-between items-end">
                  <div>
                    <h3 className="font-bold text-slate-900 text-lg">{member.name}</h3>
                    <p className="text-slate-500 text-sm">{member.role}</p>
                  </div>
                  <div className="w-8 h-8 rounded-full bg-accent/10 flex items-center justify-center text-accent">
                    <div className="w-2 h-2 rounded-full bg-accent" />
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 8. FAQ SECTION */}
      <section className="py-20 lg:py-28 bg-slate-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col lg:flex-row gap-16 items-center">
            <div className="w-full lg:w-1/2">
              <div className="inline-flex items-center gap-2 text-accent font-bold uppercase tracking-wider text-sm mb-4">
                <span className="w-8 h-0.5 bg-accent" /> Our Faqs <span className="w-8 h-0.5 bg-accent" />
              </div>
              <h2 className="text-3xl md:text-4xl font-extrabold text-slate-900 mb-8">
                Frequently Asked Questions
              </h2>
              <div className="space-y-4">
                {FAQS.map((faq, idx) => (
                  <div key={idx} className="border border-slate-200 bg-white rounded-[1px] overflow-hidden">
                    <button 
                      onClick={() => setOpenFaq(openFaq === idx ? null : idx)}
                      className="w-full text-left px-6 py-4 font-bold text-slate-900 flex justify-between items-center"
                    >
                      {faq.q}
                      <div className={cn("w-8 h-8 rounded-full flex items-center justify-center shrink-0 transition-colors", openFaq === idx ? "bg-accent text-white" : "bg-slate-100 text-slate-500")}>
                        <ChevronRight className={cn("w-4 h-4 transition-transform", openFaq === idx && "rotate-90")} />
                      </div>
                    </button>
                    <AnimatePresence>
                      {openFaq === idx && (
                        <motion.div initial={{ height: 0 }} animate={{ height: 'auto' }} exit={{ height: 0 }} className="overflow-hidden">
                          <div className="px-6 pb-4 pt-2 text-slate-600 border-t border-slate-100">
                            {faq.a}
                          </div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                ))}
              </div>
            </div>
            <div className="w-full lg:w-1/2">
              <img src="https://i.ibb.co/DH19ffJd/Image-6-Luxury-Mercedes-Benz.jpg" alt="FAQ" className="w-full h-auto rounded-[1px] shadow-xl" />
            </div>
          </div>
        </div>
      </section>

      {/* 9. BLOG SECTION */}
      <section className="py-20 lg:py-28 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <div className="inline-flex items-center justify-center gap-2 text-accent font-bold uppercase tracking-wider text-sm mb-4">
              <span className="w-8 h-0.5 bg-accent" /> Blog & News <span className="w-8 h-0.5 bg-accent" />
            </div>
            <h2 className="text-3xl md:text-4xl font-extrabold text-slate-900 mb-6">
              Latest News Directly<br />From Our Blog
            </h2>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {BLOGS.map((blog, idx) => (
              <div key={idx} className="bg-white border border-slate-100 shadow-sm rounded-[1px] overflow-hidden group">
                <div className="h-64 overflow-hidden relative">
                  <img src={blog.img} alt={blog.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                  <div className="absolute top-4 left-4 bg-accent text-white px-3 py-1 text-xs font-bold uppercase tracking-wider rounded-[1px]">
                    Logistics
                  </div>
                </div>
                <div className="p-6">
                  <div className="flex items-center gap-4 text-xs font-bold text-slate-500 uppercase tracking-wider mb-4">
                    <span className="flex items-center gap-1"><Calendar className="w-4 h-4 text-accent" /> {blog.date}</span>
                    <span className="flex items-center gap-1"><User className="w-4 h-4 text-accent" /> {blog.author}</span>
                  </div>
                  <h3 className="font-bold text-xl text-slate-900 mb-4 group-hover:text-accent transition-colors leading-tight">
                    <Link to="/blog">{blog.title}</Link>
                  </h3>
                  <Link to="/blog" className="inline-flex items-center gap-2 text-slate-900 font-bold hover:text-accent transition-colors text-sm uppercase tracking-wider">
                    Read More <ArrowRight className="w-4 h-4" />
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 10. REQUEST QUOTE FORM */}
      <section className="bg-[#111835] text-white">
        <div className="flex flex-col lg:flex-row">
          <div className="w-full lg:w-1/2 relative min-h-[400px]">
            <img src="https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&w=1200&q=80" alt="Request Quote" className="absolute inset-0 w-full h-full object-cover" />
            <div className="absolute inset-y-0 left-0 w-24 bg-accent flex items-center justify-center">
              <span className="text-white font-extrabold text-2xl tracking-[0.5em] -rotate-90 whitespace-nowrap">REQUEST QUOTE</span>
            </div>
          </div>
          <div className="w-full lg:w-1/2 p-12 lg:p-24 bg-[#111835]">
            <h2 className="text-3xl font-extrabold mb-8">Request Quote Form</h2>
            <form className="space-y-6">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <div>
                  <input type="text" placeholder="Full Name" className="w-full bg-white/5 border border-white/10 px-4 py-3 text-white focus:outline-none focus:border-accent transition-colors" />
                </div>
                <div>
                  <input type="tel" placeholder="Phone Number" className="w-full bg-white/5 border border-white/10 px-4 py-3 text-white focus:outline-none focus:border-accent transition-colors" />
                </div>
                <div>
                  <input type="email" placeholder="Email Address" className="w-full bg-white/5 border border-white/10 px-4 py-3 text-white focus:outline-none focus:border-accent transition-colors" />
                </div>
                <div>
                  <input type="text" placeholder="Service Type" className="w-full bg-white/5 border border-white/10 px-4 py-3 text-white focus:outline-none focus:border-accent transition-colors" />
                </div>
              </div>
              <div>
                <label className="block text-sm font-bold text-white/70 mb-2">Freight Type / Size</label>
                <input type="range" className="w-full accent-accent" />
              </div>
              <div>
                <input type="text" placeholder="Weight" className="w-full bg-white/5 border border-white/10 px-4 py-3 text-white focus:outline-none focus:border-accent transition-colors" />
              </div>
              <button type="button" className="w-full bg-accent hover:bg-white hover:text-[#111835] text-white font-bold py-4 transition-colors rounded-[1px] uppercase tracking-wider text-sm">
                Request A Quote <ArrowRight className="w-4 h-4 inline-block ml-2" />
              </button>
            </form>
          </div>
        </div>
      </section>

    </main>
  );
}
"""

with open('src/pages/Home.tsx', 'w') as f:
    f.write(new_home_content)
