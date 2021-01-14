from trie import Trie


t = Trie()

t.insert('abhinav')
t.insert('abhiram')
t.insert('himanshu')

#print(t.search('abhinav'))
#print(t.search('abhina'))

print(t.prefix_search('abx'))