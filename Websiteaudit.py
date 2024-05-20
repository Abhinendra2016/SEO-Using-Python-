import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_meta_tags(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    meta_tags = {meta.get('name'): meta.get('content') for meta in soup.find_all('meta') if meta.get('name')}
    title = soup.find('title').text if soup.find('title') else 'No title found'
    
    return {
        'title': title,
        'meta_tags': meta_tags
    }

def fetch_alt_tags(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    images = soup.find_all('img')
    alt_tags = [img.get('alt') for img in images if img.get('alt')]
    
    return alt_tags

def check_broken_links(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    full_links = [urljoin(base_url, link) for link in links]
    
    broken_links = []
    for link in full_links:
        try:
            res = requests.head(link, allow_redirects=True)
            if res.status_code >= 400:
                broken_links.append(link)
        except requests.RequestException as e:
            broken_links.append(link)
    
    return broken_links

def seo_audit(url):
    print(f"Starting SEO audit for {url}...\n")
    
    # Meta Tags
    meta_data = fetch_meta_tags(url)
    print(f"Title: {meta_data['title']}")
    print("Meta Tags:")
    for name, content in meta_data['meta_tags'].items():
        print(f"  - {name}: {content}")
    
    # Image Alt Tags
    alt_tags = fetch_alt_tags(url)
    if alt_tags:
        print("\nImage Alt Tags:")
        for alt in alt_tags:
            print(f"  - {alt}")
    else:
        print("\nNo image alt tags found.")
    
    # Broken Links
    broken_links = check_broken_links(url)
    if broken_links:
        print("\nBroken Links:")
        for link in broken_links:
            print(f"  - {link}")
    else:
        print("\nNo broken links found.")

if __name__ == "__main__":
    website_url = input("Enter the URL of the website to audit: ")
    seo_audit(website_url)
