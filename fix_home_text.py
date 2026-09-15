import re

with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

# Fix Hero Text
content = content.replace("Moving Made Easy,<br />Wherever Life<br />Takes You!", "Reliable Towing,<br />Haulage & Auto<br />Repairs in Ghana!")
content = content.replace("We handle home relocations, office moves, and specialty transport with care and efficiency making your move simple, safe, and stress-free.", "We provide 24/7 emergency towing, heavy-duty haulage, and professional auto repair services across Ghana. Your safety is our priority.")
content = content.replace("Delivering Smarter Logistics Solutions", "24/7 Emergency Roadside Assistance")

# Fix floating card text
content = content.replace("Global shipment<br />made easy.", "Rapid emergency<br />response.")
content = content.replace("Track Shipment", "Request Assistance")
content = content.replace("href=\"/contact\"", "href=\"/towing\"")

# Fix About Text
content = content.replace("Driven by Trust, Powered<br />by Experience.", "Expert Recovery,<br />Powered by Experience.")

# Fix Contact form -> Request Quote form
content = content.replace("Request Quote Form", "Request Assistance or Quote")

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)
