# Implement a trie with insert, search, and startsWith methods.
#
# Example:
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
#
# Note:
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
#



#--------- Trie representation in form of nested dictionary------------#:

# ball, bat, do, doll, dork, dorm, send, sense
# {   'b': {   'a': {   'l': {   'l': {   '$': True}},
#                       't': {   '$': True}}},
#     'd': {   'o': {   '$': True,
#                       'l': {   'l': {   '$': True}},
#                       'r': {   'k': {   '$': True},
#                                'm': {   '$': True}}}},
#     's': {   'e': {   'n': {   'd': {   '$': True},
#                                's': {   'e': {   '$': True}}}}}}

#Code:

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        start = self.root
        for i in word:
            if i not in start:
                start[i] = {}
            start = start[i]
        start['$'] = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        start = self.root
        for i in word:
            if i not in start:
                return False
            start = start[i]
        return '$' in start


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        start = self.root
        for i in prefix:
            if i not in start:
                return False
            start = start[i]
        return True


obj = Trie()
obj.insert("apple")
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
