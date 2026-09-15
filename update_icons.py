import re

with open('src/components/layout/NavBar.tsx', 'r') as f:
    content = f.read()

# Replace the search icon block
search_block = """          <Link 
            to="/search" 
            className="hidden sm:flex items-center justify-center p-2.5 rounded-xl hover:bg-white/10 transition-colors text-inherit rounded-full"
            aria-label="Search"
          >
            <SearchIcon className="w-5 h-5" />
          </Link>"""

new_search_block = """          <Link 
            to="/search" 
            className="hidden sm:flex items-center justify-center p-2.5 hover:bg-black/5 transition-colors text-inherit rounded-full"
            aria-label="Search"
          >
            <SearchIcon className="w-5 h-5" />
          </Link>
          <Link 
            to="/parts" 
            className="hidden sm:flex items-center justify-center p-2.5 hover:bg-black/5 transition-colors text-inherit rounded-full"
            aria-label="Cart"
          >
            <ShoppingCart className="w-5 h-5" />
          </Link>"""

content = content.replace(search_block, new_search_block)

# change "Call Now: ..." button to match "Track Your Order" style in mockup (just the layout reference, text can be 'Request Quote' or 'Call Now'). The mockup has an orange button on the far right.
# Let's keep it 'Call Now: 0597684860' but it acts as the primary CTA.

with open('src/components/layout/NavBar.tsx', 'w') as f:
    f.write(content)
