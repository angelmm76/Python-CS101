# Define a procedure, add_to_index, that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already in the index, add the url
# to the list of urls associated with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index2(index, keyword, url):
    keywords_list = []
    for i in range(len(index)):
        keywords_list.append(index[i][0])
    if keyword in keywords_list:
        key_ind = keywords_list.index(keyword)
        index[key_ind][1].append(url)
    else:
         index.append([keyword,[url]])
         
def add_to_index(index, keyword, url):         
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>>                      ['computing', ['http://acm.org']]]


# Define a procedure, add_page_to_index,that takes three inputs:
#   - index, url (String), content (String)

# It should update the index to include all of the word occurences found in the
# page content by adding the url to the word's associated url list.

index = []

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)


add_page_to_index(index,'fake.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>>                                               ['test',['fake.text']]]

def crawl_web(seed, max_pages):
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

# Modify add_to_index so that a given url is only
# included once in the url list for a keyword,
# no matter how many times that keyword appears. (L4 PS5)

def add_to_index3(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            if url not in entry[1]:
                entry[1].append(url)
            return
    # not found, add new keyword to index
    index.append([keyword, [url]])