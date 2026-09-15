import React, { useState } from 'react';
import SEO from '../components/seo/SEO';
import Breadcrumbs from '../components/ui/Breadcrumbs';
import { motion } from 'motion/react';
import { Truck, User, Phone, Mail, MapPin, CheckCircle, HelpCircle } from 'lucide-react';
import { cn } from '@/lib/utils';

export default function ContainerTruckRegistration() {
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [formData, setFormData] = useState({
    applicantType: 'Truck Owner',
    fullName: '',
    phoneNumber: '',
    whatsappNumber: '',
    emailAddress: '',
    location: '',
    truckRegistrationNumber: '',
    truckType: 'Flatbed',
    containerCapacity: '20ft',
    numberOfTrucks: '1',
    truckOwnership: 'Personally Owned',
    yearsExperience: '1',
    driverLicenseStatus: 'Valid',
    truckAvailability: 'Immediately Available',
    additionalInfo: ''
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Front-end simulation of submission
    setIsSubmitted(true);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <main className="min-h-screen bg-slate-50 pt-24 pb-20">
      <SEO 
        title="Container Truck Registration | Pexus"
        description="Register your container truck details with Pexus for available transportation opportunities around Tema."
        canonical="/container-truck-registration"
      />
      
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 max-w-4xl">
        <Breadcrumbs items={[{ label: 'Container Truck Registration' }]} />

        {isSubmitted ? (
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-white p-8 md:p-12 mt-8 text-center rounded-[1px] border border-slate-200 shadow-sm"
          >
            <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
              <CheckCircle className="w-10 h-10 text-green-600" />
            </div>
            <h2 className="text-3xl font-extrabold text-slate-900 mb-4">Registration Submitted Successfully</h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
              Thank you for registering your truck details. Your information has been received and will be reviewed. Selected applicants will be contacted using the information provided.
            </p>
            <button
              onClick={() => setIsSubmitted(false)}
              className="mt-8 bg-accent hover:bg-accent/90 text-white font-bold py-4 px-8 rounded-full transition-colors shadow-md"
            >
              Register Another Truck
            </button>
          </motion.div>
        ) : (
          <div className="bg-white mt-8 rounded-[1px] border border-slate-200 shadow-sm overflow-hidden">
            {/* Header Section */}
            <div className="bg-slate-900 text-white p-8 md:p-10 relative overflow-hidden">
              <div className="absolute top-0 right-0 w-64 h-64 bg-accent/20 rounded-full blur-3xl pointer-events-none" />
              <div className="relative z-10 flex flex-col sm:flex-row items-center sm:items-start gap-6 text-center sm:text-left">
                <div className="w-16 h-16 bg-accent rounded-full flex items-center justify-center shrink-0">
                  <Truck className="w-8 h-8 text-white" />
                </div>
                <div>
                  <h1 className="text-3xl md:text-4xl font-extrabold tracking-tight mb-3">Register Your Container Truck</h1>
                  <p className="text-white/80 text-base md:text-lg max-w-2xl leading-relaxed">
                    Are you a truck owner or driver operating container trucks around Tema? Register your details with us to be considered for available container transportation opportunities. Complete the short form below and submit your information for review.
                  </p>
                </div>
              </div>
            </div>

            {/* Form Section */}
            <form onSubmit={handleSubmit} className="p-6 sm:p-10">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                
                {/* Applicant Info */}
                <div className="md:col-span-2">
                  <h3 className="text-xl font-bold text-slate-900 border-b border-slate-100 pb-2 mb-6 flex items-center gap-2">
                    <User className="w-5 h-5 text-accent" /> Applicant Information
                  </h3>
                  
                  <div className="space-y-6">
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Applicant Type *</label>
                      <div className="flex flex-wrap gap-4">
                        {['Truck Owner', 'Driver', 'Truck Owner & Driver'].map(type => (
                          <label key={type} className="flex items-center gap-2 cursor-pointer">
                            <input 
                              type="radio" 
                              name="applicantType" 
                              value={type} 
                              checked={formData.applicantType === type}
                              onChange={handleChange}
                              className="w-4 h-4 text-accent focus:ring-accent border-slate-300"
                            />
                            <span className="text-slate-700 font-medium">{type}</span>
                          </label>
                        ))}
                      </div>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div>
                        <label className="block text-sm font-bold text-slate-700 mb-2">Full Name *</label>
                        <input 
                          type="text" 
                          name="fullName"
                          required
                          value={formData.fullName}
                          onChange={handleChange}
                          className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                          placeholder="Enter your full name"
                        />
                      </div>
                      <div>
                        <label className="block text-sm font-bold text-slate-700 mb-2">Location / Area *</label>
                        <input 
                          type="text" 
                          name="location"
                          required
                          value={formData.location}
                          onChange={handleChange}
                          className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                          placeholder="e.g. Tema, Ashaiman, Accra"
                        />
                      </div>
                    </div>
                  </div>
                </div>

                {/* Contact Info */}
                <div className="md:col-span-2">
                  <h3 className="text-xl font-bold text-slate-900 border-b border-slate-100 pb-2 mb-6 mt-4 flex items-center gap-2">
                    <Phone className="w-5 h-5 text-accent" /> Contact Details
                  </h3>
                  
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Phone Number *</label>
                      <input 
                        type="tel" 
                        name="phoneNumber"
                        required
                        value={formData.phoneNumber}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                        placeholder="e.g. 0244123456"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">WhatsApp Number *</label>
                      <input 
                        type="tel" 
                        name="whatsappNumber"
                        required
                        value={formData.whatsappNumber}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                        placeholder="e.g. 0244123456"
                      />
                    </div>
                    <div className="md:col-span-2">
                      <label className="block text-sm font-bold text-slate-700 mb-2">Email Address <span className="text-slate-400 font-normal">(Optional)</span></label>
                      <input 
                        type="email" 
                        name="emailAddress"
                        value={formData.emailAddress}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                        placeholder="you@example.com"
                      />
                    </div>
                  </div>
                </div>

                {/* Truck Info */}
                <div className="md:col-span-2">
                  <h3 className="text-xl font-bold text-slate-900 border-b border-slate-100 pb-2 mb-6 mt-4 flex items-center gap-2">
                    <Truck className="w-5 h-5 text-accent" /> Truck Information
                  </h3>
                  
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Truck Registration Number *</label>
                      <input 
                        type="text" 
                        name="truckRegistrationNumber"
                        required
                        value={formData.truckRegistrationNumber}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                        placeholder="e.g. GT 1234-21"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Truck Type *</label>
                      <select 
                        name="truckType"
                        required
                        value={formData.truckType}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                      >
                        <option value="Flatbed">Flatbed</option>
                        <option value="Other Container Truck">Other Container Truck</option>
                      </select>
                    </div>
                    
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Container Capacity *</label>
                      <select 
                        name="containerCapacity"
                        required
                        value={formData.containerCapacity}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                      >
                        <option value="20ft">20ft</option>
                        <option value="40ft">40ft</option>
                        <option value="Both 20ft & 40ft">Both 20ft & 40ft</option>
                      </select>
                    </div>
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Number of Trucks Available *</label>
                      <input 
                        type="number" 
                        name="numberOfTrucks"
                        min="1"
                        required
                        value={formData.numberOfTrucks}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                      />
                    </div>

                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Truck Ownership *</label>
                      <select 
                        name="truckOwnership"
                        required
                        value={formData.truckOwnership}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                      >
                        <option value="Personally Owned">Personally Owned</option>
                        <option value="Company Owned">Company Owned</option>
                        <option value="Other">Other</option>
                      </select>
                    </div>
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Years of Container Truck Experience *</label>
                      <input 
                        type="number" 
                        name="yearsExperience"
                        min="0"
                        required
                        value={formData.yearsExperience}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Driver's Licence Status *</label>
                      <select 
                        name="driverLicenseStatus"
                        required
                        value={formData.driverLicenseStatus}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                      >
                        <option value="Valid">Valid</option>
                        <option value="Expired">Expired</option>
                        <option value="Not Available">Not Available</option>
                      </select>
                    </div>
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Truck Availability *</label>
                      <select 
                        name="truckAvailability"
                        required
                        value={formData.truckAvailability}
                        onChange={handleChange}
                        className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none"
                      >
                        <option value="Immediately Available">Immediately Available</option>
                        <option value="Available Within 7 Days">Available Within 7 Days</option>
                        <option value="Available Later">Available Later</option>
                      </select>
                    </div>
                  </div>
                </div>

                {/* Additional Info */}
                <div className="md:col-span-2">
                  <h3 className="text-xl font-bold text-slate-900 border-b border-slate-100 pb-2 mb-6 mt-4 flex items-center gap-2">
                    <HelpCircle className="w-5 h-5 text-accent" /> Additional Information
                  </h3>
                  
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">Any other details we should know? <span className="text-slate-400 font-normal">(Optional)</span></label>
                    <textarea 
                      name="additionalInfo"
                      rows={4}
                      value={formData.additionalInfo}
                      onChange={handleChange}
                      className="w-full px-4 py-3 bg-slate-50 border border-slate-200 focus:border-accent focus:ring-2 focus:ring-accent/20 transition-all rounded-[1px] outline-none resize-y"
                      placeholder="Enter any additional information here..."
                    />
                  </div>
                </div>

                {/* Submit Button */}
                <div className="md:col-span-2 pt-6 border-t border-slate-100 mt-4">
                  <button 
                    type="submit" 
                    className="w-full md:w-auto min-w-[250px] bg-accent hover:bg-accent/90 text-white font-bold py-4 px-8 rounded-full transition-all shadow-lg hover:shadow-xl hover:-translate-y-1 text-lg flex justify-center items-center gap-2 mx-auto"
                  >
                    Submit Registration
                  </button>
                  <p className="text-center text-slate-500 text-sm mt-4">
                    By submitting this form, you agree to be contacted regarding available opportunities.
                  </p>
                </div>

              </div>
            </form>
          </div>
        )}
      </div>
    </main>  
  );
}
