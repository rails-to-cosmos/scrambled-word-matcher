import unittest
from matcher import ScrambledWordMatcher


class TestScrambledWordMatcher(unittest.TestCase):
    def test_definition(self):
        "Test case from the task definition."

        matcher = ScrambledWordMatcher()
        matcher.add_word('axpaj')
        matcher.add_word('apxaj')
        matcher.add_word('dnrbt')
        matcher.add_word('pjxdn')
        matcher.add_word('abd')

        self.assertEqual(matcher.scan('aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt'), 4)

    def test_carry(self):
        "Checks scrambled matching."

        matcher = ScrambledWordMatcher()
        matcher.add_word('abez')
        matcher.add_word('abfy')
        self.assertEqual(matcher.scan('aebz'), 1)

    def test_finish_on_carry(self):
        "Checks if matcher handles sliding windows properly."
        matcher = ScrambledWordMatcher()
        matcher.add_word('abeaz')
        matcher.add_word('abfy')
        self.assertEqual(matcher.scan('abeaz'), 1)

    def test_miss(self):
        "No false positives should arise."
        matcher = ScrambledWordMatcher()
        matcher.add_word('abeaz')
        matcher.add_word('abfy')
        self.assertEqual(matcher.scan('abyf'), 0)

    def test_simple(self):
        matcher = ScrambledWordMatcher()
        matcher.add_word('star')
        matcher.add_word('loop')
        matcher.add_word('part')
        self.assertEqual(matcher.scan('wtsartsatroplopratlopostar'), 2)

    def test_multi_scan(self):
        matcher = ScrambledWordMatcher()
        matcher.add_word('axpaj')
        matcher.add_word('apxaj')
        matcher.add_word('dnrbt')
        matcher.add_word('pjxdn')
        matcher.add_word('abd')
        self.assertEqual(matcher.scan('aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt'), 4)
        self.assertEqual(matcher.scan('aapxj'), 2)
        self.assertEqual(matcher.scan('adb'), 0)
        self.assertEqual(matcher.scan('adbtpdxjn'), 1)

if __name__ == '__main__':
    unittest.main()