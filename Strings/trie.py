"""
Given a list of words, and a search query, find all
the words with the given prefix.
The code below efficiently solves the problem using the trie data structure
https://wikipedia.org/wiki/Trie

"""
class Node(object):
    def __init__(self):
        self.children = dict()
        self.isWord = False
        self.word = None
    def set_word(self, word: str) -> None:
        #Set the word at the current node
        # if the node doesn't contain complete a full
        # word just set word to None
        self.word = word
    def insert(self, word: str, current_word: list = []) -> None:
        # Insert a word into the Trie
        # Once all characters are exhausted return
        # and set the end of a word at this node
        # set current word to the original word to keep it for use
        # in the node
        if len(word) == 0:
            self.isWord = True
            self.set_word("".join(current_word))
            return
        # The node to which the character should fit
        node = word[0]
        current_word.append(node)
        if not node in self.children:
            self.children[node] = Node()
        self.children[node].insert(word[1:], current_word)
    def print_words(self):
        if self.isWord:
            print(self.word)
        for child in self.children.keys():
            self.children[child].print_words()
    def collect(self, result: list = []) -> list:
        # Collect all words from the current node
        if self.isWord:
            result.append(self.word)
            return []
        for child in self.children.keys():
            self.children[child].collect(result)
        return result
    def search_with_prefix(self, prefix: str) -> list:
        """ Get all words in the trie with a given prefix"""
        if len(prefix) == 0:
            return self.collect([])
        child = prefix[0]
        if child not in self.children:
            return []
        return self.children[child].search_with_prefix(prefix[1:])



class Trie(object):
    def __init__(self):
        self.root = None
    def insert(self, word: str) -> None:
        if self.root is None:
            self.root = Node()
        self.root.insert(word, [])
    def print_words(self) -> None:
        self.root.print_words()
    def search_with_prefix(self, prefix: str) -> list:
        return self.root.search_with_prefix(prefix)

# root = Trie()

# root.insert('silas')
# root.insert('silos')
# root.insert('silas')
# root.insert('james')
# root.insert('jakes')
# root.insert('june')
# root.insert('lazarus')

# root.print_words()

# print(root.search_with_prefix('ju'))


