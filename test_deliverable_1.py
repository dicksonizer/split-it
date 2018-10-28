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
        self.assertEqual(option('w','E',')','3','#','')menu())
    
    def test_option_c(self):
        teamNumber = int(input('Enter the number of team members: '))
        with self.assertRaises(ValueError):
            deliverable_1.option_c()
        
if __name__ == '__main__':
    unittest.main()
    projectTitle = str(input('Enter the project name: \033[4m\0'))

  