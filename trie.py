class TrieNode:
    def __init__(self):
        self.isEnd=False
        self.children=['*']*26 #we can judge wheather there is a children node
        self.word='' # every node store string from root to this node

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        cur=self.root
        for i in range(0,len(word)):
            if cur.children[ord(word[i])-97]=='*':
                cur.children[ord(word[i])-97]=TrieNode()
                cur.children[ord(word[i])-97].word=cur.word+word[i]
            cur=cur.children[ord(word[i])-97]
        cur.isEnd=True

    def search(self,word):
        cur=self.root
        for i in range(0,len(word)):
            if cur.children[ord(word[i])-97]=='*':
                return False
            cur=cur.children[ord(word[i])-97]
        return cur.isEnd

    def startsWith(self,prefix):
        cur = self.root
        for i in range(0, len(prefix)):
            if cur.children[ord(prefix[i]) - 97] == '*':
                return False
            cur = cur.children[ord(prefix[i]) - 97]
        return True
