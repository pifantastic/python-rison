import unittest
from rison import loads


class TestDecoder(unittest.TestCase):

    def test_dict(self):
        self.assertEqual(loads('()'), {})
        self.assertEqual(loads('(a:0,b:1)'), {
            'a': 0,
            'b': 1
        })
        self.assertEqual(loads("(a:0,b:foo,c:'23skidoo')"), {
            'a': 0,
            'c': '23skidoo',
            'b': 'foo'
        })
        self.assertEqual(loads('(id:!n,type:/common/document)'), {
            'type': '/common/document',
            'id': None
        })
        self.assertEqual(loads("(a:0)"), {
            'a': 0
        })

    def test_bool(self):
        self.assertEqual(loads('!t'), True)
        self.assertEqual(loads('!f'), False)

    def test_none(self):
        self.assertEqual(loads('!n'), None)

    def test_list(self):
        self.assertEqual(loads('!(1,2,3)'), [1, 2, 3])
        self.assertEqual(loads('!()'), [])
        self.assertEqual(loads("!(!t,!f,!n,'')"), [True, False, None, ''])

    def test_number(self):
        self.assertEqual(loads('0'), 0)
        self.assertEqual(loads('1.5'), 1.5)
        self.assertEqual(loads('-3'), -3)
        self.assertEqual(loads('1e30'), 1e+30)
        self.assertEqual(loads('1e-30'), 1.0000000000000001e-30)

    def test_string(self):
        self.assertEqual(loads("''"), '')
        self.assertEqual(loads('G.'), 'G.')
        self.assertEqual(loads('a'), 'a')
        self.assertEqual(loads("'0a'"), '0a')
        self.assertEqual(loads("'abc def'"), 'abc def')
        self.assertEqual(loads("'-h'"), '-h')
        self.assertEqual(loads('a-z'), 'a-z')
        self.assertEqual(loads("'wow!!'"), 'wow!')
        self.assertEqual(loads('domain.com'), 'domain.com')
        self.assertEqual(loads("'user@domain.com'"), 'user@domain.com')
        self.assertEqual(loads("'US $10'"), 'US $10')
        self.assertEqual(loads("'can!'t'"), "can't")
