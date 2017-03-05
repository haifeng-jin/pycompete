class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.is_end = False
        self.leaves = {}

    # Inserts a word into the trie.
    def insert(self, word):
        cur = self
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_end = True


    def search(self,word):
        cur = self
        for c in word:
            if not c in cur.leaves:
                return False
            cur = cur.leaves[c]
        return cur.is_end

    def startsWith(self,prefix):
        cur = self
        for c in word:
            if not c in cur.leaves:
                return False
            cur = cur.leaves[c]
        return True
