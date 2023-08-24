import scaZone    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(scaZone.Zone.increment(3), 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(scaZone.Zone.decrement(3), 4)

if __name__ == '__main__':
    unittest.main()
