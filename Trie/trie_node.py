class TrieNode:
    def __init__(self,data):
        self.data = data
        self.children : TrieNode = []
        self.is_end = False
        