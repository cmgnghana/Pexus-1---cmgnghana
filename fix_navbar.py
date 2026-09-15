import re

with open('src/components/layout/NavBar.tsx', 'r') as f:
    content = f.read()

# Add imports for social icons if needed
import_line = "import { ChevronDown, Menu, X, Phone, Search as SearchIcon, Mail, MapPin, Clock, Facebook, Twitter, Instagram, Linkedin, ShoppingCart } from 'lucide-react';"
content = re.sub(r"import \{ ChevronDown, Menu, X, Phone, Search as SearchIcon \} from 'lucide-react';", import_line, content)

# Change header wrapper and add topbar
header_start = """  return (
    <header 
      className={cn(
        "fixed top-0 left-0 right-0 z-50 transition-all duration-300 ease-in-out",
        isScrolled || location.pathname !== '/' 
          ? "bg-white/95 backdrop-blur-md shadow-sm text-dark translate-y-0" 
          : "bg-[#111835]/95 backdrop-blur-md text-white translate-y-0 border-b border-white/10"
      )}
    >
      {/* Top Bar - Hidden on Mobile */}
      <div className={cn(
        "hidden lg:block w-full border-b transition-all duration-300 overflow-hidden",
        isScrolled || location.pathname !== '/' ? "border-gray-100 h-0 opacity-0" : "border-white/10 h-auto opacity-100"
      )}>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 flex justify-between items-center text-xs">
          <div className="flex items-center gap-6 text-white/80">
            <a href="tel:0597684860" className="flex items-center gap-1.5 hover:text-accent transition-colors">
              <Phone className="w-3.5 h-3.5 text-accent" />
              <span>0597684860</span>
            </a>
            <a href="mailto:official.pexus@gmail.com" className="flex items-center gap-1.5 hover:text-accent transition-colors">
              <Mail className="w-3.5 h-3.5 text-accent" />
              <span>official.pexus@gmail.com</span>
            </a>
            <div className="flex items-center gap-1.5">
              <MapPin className="w-3.5 h-3.5 text-accent" />
              <span>Tema, Ghana</span>
            </div>
          </div>
          <div className="flex items-center gap-6 text-white/80">
            <div className="flex items-center gap-1.5">
              <Clock className="w-3.5 h-3.5 text-accent" />
              <span>Mon - Sat: 08:00 - 18:00</span>
            </div>
            <div className="flex items-center gap-3">
              <a href="#" className="hover:text-accent transition-colors"><Facebook className="w-3.5 h-3.5" /></a>
              <a href="#" className="hover:text-accent transition-colors"><Twitter className="w-3.5 h-3.5" /></a>
              <a href="#" className="hover:text-accent transition-colors"><Instagram className="w-3.5 h-3.5" /></a>
              <a href="#" className="hover:text-accent transition-colors"><Linkedin className="w-3.5 h-3.5" /></a>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center py-4">"""

content = re.sub(r"  return \(\n    <header [^>]*>\n      <div className=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center\">", header_start, content, flags=re.DOTALL)

# Update logo logic
logo_find = """        <Link to="/" className="flex items-center gap-2 group">
          <img 
            src="https://i.ibb.co/rS4MyLS/Pexus-Logo-Dark-Version.png" 
            alt="Pexus Logo" 
            className="h-10 md:h-11 w-auto object-contain\""""

logo_replace = """        <Link to="/" className="flex items-center gap-2 group">
          <img 
            src={isScrolled || location.pathname !== '/' ? "https://i.ibb.co/rS4MyLS/Pexus-Logo-Dark-Version.png" : "https://i.ibb.co/jjG8ysr/Pexus-Logo-White-Version.png"} 
            alt="Pexus Logo" 
            className="h-10 md:h-11 w-auto object-contain\""""
content = content.replace(logo_find, logo_replace)

# Change padding to include `py-4` ? Wait, I added `py-4` to the flex container in `header_start`. Let's remove the `py-3.5` and `py-4` from the header className.
# Wait, I did replace the header className. 
# Let's ensure it handles correctly.

with open('src/components/layout/NavBar.tsx', 'w') as f:
    f.write(content)
