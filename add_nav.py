import re

with open('src/components/layout/NavBar.tsx', 'r') as f:
    content = f.read()

# For Desktop Nav (Large Screens)
# Find: <Link to="/contact" className="hover:text-accent transition-colors">Contact</Link>
# Append: <Link to="/container-truck-registration" className="hover:text-accent transition-colors font-semibold text-accent">Container Truck Registration</Link>

content = content.replace('<Link to="/contact" className="hover:text-accent transition-colors">Contact</Link>', '<Link to="/contact" className="hover:text-accent transition-colors">Contact</Link>\n          <Link to="/container-truck-registration" className="hover:text-accent transition-colors font-semibold text-accent">Container Truck Registration</Link>')

# For Medium Nav (Tablet/Laptop)
# Find: <Link to="/contact" className="hover:text-accent transition-colors">Contact</Link>
# Wait, let's see how many times it exists.
# We will do a regex replacement on all `<Link to="/contact" ...>Contact</Link>` in `<nav ...>` 

# But the mobile menu also needs it.

with open('src/components/layout/NavBar.tsx', 'w') as f:
    f.write(content)
