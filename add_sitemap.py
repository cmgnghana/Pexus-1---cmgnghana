import re

with open('src/data/sitemapData.ts', 'r') as f:
    content = f.read()

# Add to MAIN_PAGES
main_pages_str = "export const MAIN_PAGES: SitemapLink[] = [\n"
new_main_pages_str = "export const MAIN_PAGES: SitemapLink[] = [\n  { label: 'Container Truck Registration', path: '/container-truck-registration' },\n"
content = content.replace(main_pages_str, new_main_pages_str)

with open('src/data/sitemapData.ts', 'w') as f:
    f.write(content)
