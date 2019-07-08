import unittest

def add(one, two):                                        #function for testing out
        return one + two

class TestCalc(unittest.TestCase):
        def test_add(self):                               #test_*(what we'll test)
            result = add(10, 5)
            self.assertEqual(result, 15)

                                                  # <__name__> equals to module name (unit_tests)
if __name__ == '__main__':                        #if scripts run directly (not imported and ran from the other <*.py>)
    unittest.main()                               #run the module unittest main() func
    
    
#start by using <python3 -m unittest unit_tests>. The -m parameter starts the module as a script with the option to accept the unit_tests program as a parameter.
