import argparse, requests, bs4
import urllib.request

parser = argparse.ArgumentParser(description='Google Search Web Scraping.')
parser.add_argument('--num', default=5, type=int, help='Number.')
parser.add_argument('--query', help='Search Query.')
args = parser.parse_args()
 
res = requests.get('http://google.com/search?q=a')
res.raise_for_status()
 
soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.r a')
num_open = min(args.num, len(link_elems))
print("a")
for i in range(num_open):
    rank = i + 1
    url = link_elems[i]['href']
    title = link_elems[i].get_text()
 
    print_line = '{rank}, {url}, {title}'.format(rank=rank, url=url, title=title)
    print(print_line)
    print("a")