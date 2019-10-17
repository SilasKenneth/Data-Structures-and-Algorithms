from Strings.trie import Trie
import unittest


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = ['silas', 'james', 'sales', 'skales']
    def insertWords(self, number: int) -> None:
        words = self.words[:number]
        for word in words:
            self.trie.insert(word)
    def test_can_insert(self):
        self.insertWords(1)
        self.assertEqual(len(self.trie.search_with_prefix(self.words[0][:-2])), 1)
    def test_can_detect_duplicates(self):
        self.insertWords(1)
        self.insertWords(1)
        self.assertEqual(len(self.trie.search_with_prefix(self.words[0][:-2])), 1)
    def test_can_add_more_than_one_word(self):
        self.insertWords(4)
        self.assertEqual(len(self.trie.search_with_prefix('s')), 3)
    def test_can_return_empty_no_prefix(self):
        self.insertWords(4)
        self.assertEqual(len(self.trie.search_with_prefix('fakaklajakjakj')), 0)