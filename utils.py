import re

def clean_website_list(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        websites = [line.strip() for line in f]

    cleaned = []
    for site in websites:
        if not site:
            continue
        if not site.startswith('http'):
            site = 'http://' + site
        if re.match(r'https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+', site):
            cleaned.append(site)
    return cleaned
