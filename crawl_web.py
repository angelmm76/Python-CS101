import urllib

def get_page(url):
	try:
	   return str(urllib.urlopen(url).read())
	except:
	   return ""

def get_next_target(page):
	start = page.find('<a href=')
	if start ==-1:
	   return None, 0
	start_quote = page.find('"',start)
	end_quote = page.find('"',start_quote + 1)
	url= page[start_quote+1:end_quote]
	return url, end_quote

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
	links = []
	while True:
	   url, endpos = get_next_target(page)
	   if url:
	       links.append(url)
	       page = page[endpos:]
	   else:
	       break
        return links  	

def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
            if len(crawled) == max_pages:
                break
    return crawled

def crawl_web2(seed,max_depth):
    tocrawl, crawled = [], []
    tocrawl.append([seed])
    for i in range(max_depth + 1):
        next_tocrawl = []
        for page in tocrawl[i]:
            if page not in crawled:
                links = get_all_links(get_page(page))
                union(next_tocrawl, links)
                crawled.append(page)
        tocrawl.append(next_tocrawl)
    return crawled
    
    
seed = 'http://www.udacity.com/cs101x/index.html'
#seed = 'http://www.nytimes.com'
#print crawl_web(seed, 5)
#print crawl_web2(seed, 5)


print crawl_web2("http://www.udacity.com/cs101x/index.html",0)
#>>> ['http://www.udacity.com/cs101x/index.html']

print crawl_web2("http://www.udacity.com/cs101x/index.html",1)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html']

print crawl_web2("http://www.udacity.com/cs101x/index.html",50)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html',
#>>> 'http://www.udacity.com/cs101x/kicking.html']

print crawl_web2("http://top.contributors/forbiddenvoid.html",2)
#>>> ['http://top.contributors/forbiddenvoid.html',
#>>> 'http://top.contributors/graemeblake.html',
#>>> 'http://top.contributors/angel.html',
#>>> 'http://top.contributors/dreyescat.html',
#>>> 'http://top.contributors/johang.html',
#>>> 'http://top.contributors/charlzz.html']

print crawl_web2("A1",3)
#>>> ['A1', 'C1', 'B1', 'E1', 'D1', 'F1']
# (May be in any order)


def add_to_index(index, keyword, url):         
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])
    
def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def crawl_web_index(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
            if len(crawled) == max_pages:
                break
    return index