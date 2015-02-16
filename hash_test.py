import urllib

def get_page(url):
	try:
	   return str(urllib.urlopen(url).read())
	except:
	   return ""
	 
def bad_hash_string(keyword, buckets):
    return ord(keyword[0]) % buckets

def better_hash_string(keyword,buckets):
    h = 0
    for c in keyword:
        h += ord(c)
    return h % buckets
    
def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
    return results
    
content = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt')
words = content.split()
print len(words)
counts = test_hash_function(bad_hash_string, words, 12)
print counts
counts = test_hash_function(better_hash_string, words, 12)
print counts