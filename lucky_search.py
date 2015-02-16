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

def crawl_web(seed): 
    tocrawl = [seed] 
    crawled = [] 
    index = {}
    graph ={}
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled: 
            content = get_page(page) 
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks) 
            crawled.append(page) 
    return index, graph

def add_page_to_index(index, url, content): 
    words = content.split() 
    for word in words: 
        add_to_index(index, word, url) 

def add_to_index(index, keyword, url): 
    if keyword in index:
        index[keyword].append(url) 
    else:
        index[keyword] = [url] 

def lookup(index, keyword): 
    if keyword in index:
        return index[keyword] 
    else:
        return None 
        
def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            rank_sum = 0
            for p in graph:
                if page in graph[p]:
                    rank_sum = rank_sum + ranks[p] / len(graph[p])
            newrank = (1 - d) / npages + d * rank_sum
            newranks[page] = newrank
        ranks = newranks
    return ranks
    
def lucky_search2(index, ranks, keyword):
    max_rank = 0.0
    result_page = None
    if keyword in index:
        for page in lookup(index, keyword):
            if ranks[page] > max_rank:
                max_rank = ranks[page]
                result_page = page
    return result_page 
    
def lucky_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
        return None
    best_page = pages[0]
    for candidate in pages:
        if ranks[candidate] >ranks[best_page]:
            best_page = candidate
    return best_page 
    
index, graph = crawl_web("https://www.udacity.com/cs101x/urank/index.html")
print graph
ranks = compute_ranks(graph)
print ranks
print lucky_search(index, ranks, 'the')