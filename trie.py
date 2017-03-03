class TrieNode:
    def __init__(self):
        self.isEnd=False
        self.children=[None]*26 #we can judge wheather there is a children node

class Trie:
    def __init__(self, alpha='A'):
        self.root=TrieNode()
        self.alpha = alpha

    def insert(self,word):
        cur=self.root
        for i in range(len(word)):
            if not cur.children[ord(word[i])-ord(self.alpha)]:
                cur.children[ord(word[i])-ord(self.alpha)]=TrieNode()
            cur=cur.children[ord(word[i])-ord(self.alpha)]
        cur.isEnd=True

    def search(self,word):
        cur=self.root
        for i in range(len(word)):
            if not cur.children[ord(word[i])-ord(self.alpha)]:
                return False
            cur=cur.children[ord(word[i])-ord(self.alpha)]
        return cur.isEnd

    def startsWith(self,prefix):
        cur = self.root
        for i in range(len(prefix)):
            if not cur.children[ord(prefix[i]) - ord(self.alpha)]:
                return False
            cur = cur.children[ord(prefix[i]) - ord(self.alpha)]
        return True
