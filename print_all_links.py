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

def print_all_links(page):
	while True:
	   url, endpos = get_next_target(page)
	   if url:
	       print url
	       page = page[endpos:]
	   else:
	       break

url = 'http://www.udacity.com/cs101x/index.html'
#url = 'http://xkcd.com/353'
#url = 'http://www.google.com'
#print get_page(url)
print_all_links(get_page(url))

