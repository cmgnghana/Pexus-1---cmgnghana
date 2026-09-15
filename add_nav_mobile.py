import re

with open('src/components/layout/NavBar.tsx', 'r') as f:
    content = f.read()

# Add to mobile menu
content = content.replace(
    '<Link to="/contact" onClick={() => setMobileMenuOpen(false)} className="py-3 px-4 hover:text-accent hover:bg-slate-50 transition-colors shrink-0 rounded-full">Contact</Link>',
    '<Link to="/contact" onClick={() => setMobileMenuOpen(false)} className="py-3 px-4 hover:text-accent hover:bg-slate-50 transition-colors shrink-0 rounded-full">Contact</Link>\n              <Link to="/container-truck-registration" onClick={() => setMobileMenuOpen(false)} className="py-3 px-4 text-accent font-bold hover:bg-slate-50 transition-colors shrink-0 rounded-full">Container Truck Registration</Link>'
)

with open('src/components/layout/NavBar.tsx', 'w') as f:
    f.write(content)
