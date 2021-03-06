def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]
    
def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table
    
#print make_hashtable(14)

def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable,key).append([key, value]) 
    return htable
    
def hashtable_lookup(htable,key):
    for entry in hashtable_get_bucket(htable,key):
        if entry[0] == key:
            return entry[1]
    return None
    
def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
         if entry[0] == key:
              entry[1] = value
              return htable
    hashtable_add(htable,key,value)
    return htable
