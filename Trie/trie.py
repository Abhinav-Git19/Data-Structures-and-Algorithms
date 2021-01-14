from typing import Optional
from trie_node import TrieNode

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode('\0')

    def insert(self,key):
        cur = self.root

        
        for c in key:
            found = False
            for node in cur.children:
                if node.data == c:
                    cur=node
                    found = True
            if not found:  
                new_node = TrieNode(c)
                cur.children.append(new_node)
                cur = new_node

        cur.is_end=True
    
    def delete(self,key):
        pass


    def print_all_words(self,root,key):

        if root.is_end:
            print(key)

        for node in root.children:
            self.print_all_words(node,key+node.data)
        
        



    def prefix_search(self,key):
        cur = self.root
        for c in key:
            found = False
            for node in cur.children:
                if node.data == c:
                    cur = node
                    found = True
            if not found:
                return False
        self.print_all_words(cur,key)
        return True

    def search(self,key):
        cur = self.root
        for c in key:
            found = False
            for node in cur.children:
                if node.data == c:
                    cur = node
                    found = True
            if not found:
                return False
        return True if cur.is_end == True else False
            
