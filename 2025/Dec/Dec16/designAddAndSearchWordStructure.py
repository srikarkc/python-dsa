class TrieNode:
    def __init__(self):
        self.children, self.is_end = {}, False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        def dfs(i, node):
            if i == len(word):
                return node.is_end

            ch = word[i]

            if ch != ".":
                if ch not in node.children:
                    return False
                return dfs(i + 1, node.children[ch])

            # If ch == '.' - check all roots
            for child in node.children.values():
                if dfs(i+1, child):
                    return True
            return False

        dfs(0, self.root)