import unittest
from rison import dumps


class TestEncoder(unittest.TestCase):

    def test_dict(self):
        self.assertEqual('()', dumps({}))
        self.assertEqual('(a:0,b:1)', dumps({
            'a': 0,
            'b': 1
        }))
        self.assertEqual("(a:0,b:foo,c:'23skidoo')", dumps({
            'a': 0,
            'c': '23skidoo',
            'b': 'foo'
        }))
        self.assertEqual('(id:!n,type:/common/document)', dumps({
            'type': '/common/document',
            'id': None
        }))
        self.assertEqual("(a:0)", dumps({
            'a': 0
        }))

    def test_bool(self):
        self.assertEqual('!t', dumps(True))
        self.assertEqual('!f', dumps(False))

    def test_none(self):
        self.assertEqual('!n', dumps(None))

    def test_list(self):
        self.assertEqual('!(1,2,3)', dumps([1, 2, 3]))
        self.assertEqual('!()', dumps([]))
        self.assertEqual("!(!t,!f,!n,'')", dumps([True, False, None, '']))

    def test_number(self):
        self.assertEqual('0', dumps(0))
        self.assertEqual('1.5', dumps(1.5))
        self.assertEqual('-3', dumps(-3))
        self.assertEqual('1e30', dumps(1e+30))
        self.assertEqual('1e-30', dumps(1.0000000000000001e-30))

    def test_string(self):
        self.assertEqual("''", dumps(''))
        self.assertEqual('G.', dumps('G.'))
        self.assertEqual('a', dumps('a'))
        self.assertEqual("'0a'", dumps('0a'))
        self.assertEqual("'abc def'", dumps('abc def'))
        self.assertEqual("'-h'", dumps('-h'))
        self.assertEqual('a-z', dumps('a-z'))
        self.assertEqual("'wow!!'", dumps('wow!'))
        self.assertEqual('domain.com', dumps('domain.com'))
        self.assertEqual("'user@domain.com'", dumps('user@domain.com'))
        self.assertEqual("'US $10'", dumps('US $10'))
        self.assertEqual("'can!'t'", dumps("can't"))

