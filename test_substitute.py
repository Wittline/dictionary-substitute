import unittest
from substitute import substitute

class DictionarySubstitutionTestCase(unittest.TestCase):
    def test_substitute_depth_1(self):
        data = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': {
                'key4': 'value4',
                'key5': 'value5'
            }
        }
        expected_output = {
            'key1': {'_content': 'value1', '_type': "<class 'str'>"},
            'key2': {'_content': 'value2', '_type': "<class 'str'>"},
            'key3': {
                'key4': {'_content': 'value4', '_type': "<class 'str'>"},
                'key5': {'_content': 'value5', '_type': "<class 'str'>"}
            }
        }
        substitute(data, depth=1)
        self.assertEqual(data, expected_output)

    def test_substitute_depth_2(self):
        data = {
            'key1': 'value1',
            'key2': 'value2',
            'key22': ['valuex', 'valuey', 'valuez'],
            'key3': {
                'key4': 'value4',
                'key5': 'value5',
                'key6': 'value6'
            }
        }
        expected_output = {
            'key1': {'_content': 'value1', '_type': "<class 'str'>"},
            'key2': {'_content': 'value2', '_type': "<class 'str'>"},
            'key22': {'_content': ['valuex', 'valuey', 'valuez'], '_type': "<class 'list'>"},
            'key3': {
                'key4': {'_content': 'value4', '_type': "<class 'str'>"},
                'key5': {'_content': 'value5', '_type': "<class 'str'>"},
                'key6': {'_content': 'value6', '_type': "<class 'str'>"}
            }
        }
        substitute(data, depth=2)
        self.assertEqual(data, expected_output)

    def test_substitute_depth_0(self):
        data = {
            'key1': 'value1',
            'key2': 'value2',
            'hobbies': ['valuex', 'valuey'],
            'key3': {
                'key4': 'value4',
                'key5': 'value5',
                'key6': 'value6'
            },
            'key7': False
        }
        expected_output = {
            'key1': 'value1',
            'key2': 'value2',
            'hobbies': ['valuex', 'valuey'],
            'key3': {
                'key4': 'value4',
                'key5': 'value5',
                'key6': 'value6'
            },
            'key7': False
        }
        substitute(data, depth=0)
        self.assertEqual(data, expected_output)

if __name__ == '__main__':
    unittest.main()