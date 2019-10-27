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
    
class Solution(object):
    def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans
