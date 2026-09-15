import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add import
import_stmt = "import Contact from './pages/Contact';\nimport ContainerTruckRegistration from './pages/TruckRegistration';"
content = content.replace("import Contact from './pages/Contact';", import_stmt)

# Add route
route_stmt = '<Route path="/contact" element={<Contact />} />\n            <Route path="/container-truck-registration" element={<ContainerTruckRegistration />} />'
content = content.replace('<Route path="/contact" element={<Contact />} />', route_stmt)

with open('src/App.tsx', 'w') as f:
    f.write(content)
