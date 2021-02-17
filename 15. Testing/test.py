import unittest
import main 

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')


    def test_do_stuff(self):
        '''Ho;oooo'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'ergfesg'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    
    def tearDown(self):
        print('cleaning up')


if __name__ == "__main__":
    unittest.main()