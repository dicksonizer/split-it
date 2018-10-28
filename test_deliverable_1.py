import unittest
import deliverable_1

class testDeliverable_1(unittest.Testcase):
    
    def test_menu(self):
        option = str(input('\tPlease choose and option and press <Enter>: '))
        
        self.assertEqual(option('A','a'),option_a())
        self.assertEqual(option('C','c'),option_c())
        self.assertEqual(option('V','v'),option_v())
        self.assertEqual(option('S','s'),option_s())
        self.assertEqual(option('Q','q'),option_q())
        self.assertEqual(option('w','E',')','3','#',''),menu())
    
    def test_option_c(self):
        teamNumber = int(input('Enter the number of team members: '))
        self.assertTrue(teamNumber(0, 1, 2),break)
        self.assertRaise(teamNumber(ValueError),pass)
        
        teamNumber_1 = input('Enter the name of team member ' + str(i) + ': ')
        self.assertEqual(deliverable_1.option_c(self)return_to_menu()
        
        
        
if __name__ == '__main__':
    unittest.main()
