class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        return node.is_end
    
    def search(self, word):

        def dfs(node, i):

            if i == len(word):
                return node.is_end
            
            ch = word[i]

            if ch != ".":
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)
            else:
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            
        return dfs(self.root, 0)