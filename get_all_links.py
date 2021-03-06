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

#seed = 'http://www.udacity.com/cs101x/index.html'
seed = 'http://xkcd.com/353'
#seed = 'http://www.google.com'
#print get_page(seed_url)
print get_all_links(get_page(seed))

