import unittest
import deliverable_2

class TestDeliverable_2(unittest.TestCase):

	def test_getOption(self, option):
		self.assertEqual(option('A'), 'A')
		self.assertEqual(option('a'), 'A')
		
	def isValidOption(self, option):
		self.assertTrue(option('A', 'C', 'V', 'S', 'Q'))
		self.assertFalse(option('', 'Z'))
    
    def test_main(self):
        option = str(input('\tPlease choose and option and press <Enter>: ')) 
      	self.assertEqual(option('A','a'),about())
        self.assertEqual(option('C','c'),createProject())
        self.assertEqual(option('V','v'),setVotes())
        self.assertEqual(option('w','E',')','3','#',''),main())
    
    def test_createProject(self):
        projectTitle = input(str('Enter Project title: '))
        self.assertFalse(projectTitle('N',' ', ',', 4))
        self.assertTrue(projectTitle('Title', 'TITLE','Project'))

        teamSize = input('Enter the number of team members: ')
        self.assertTrue(teamSize(3, 4, 5))
        self.assertFalse(teamSize(0, 1, 2, 6))

        personName = input("\tEnter name of team member {}: ".format(i+1))
        self.assertTrue(personName('Lance','Jack'))
        self.assertFalse(personName('3', 3, ' '))
        	team = list()
		  	team.append(personName)
		    self.assertEqual(team[0],personName)
		    team.count = 5
		    self.assertRaises(IndexError,team.append(personName))

    def test_setVotes(self):
    	projectName = input("Enter the project name from the following list: " + str(",".join("{}".format(k)for k in projectDict.keys())) + "\nEnter Project Title: ")
    	self.assertEqual(projectName(k in projectDict.keys()), addPoints())

    def test_addVotes(self, projectName):
    	point = int(input("Enter " + str(names[i]) + "\'s points for " + str(j) + ": "))
    	self.assertTrue(point(4, 5, 3))
    	self.assertFalse(point('r', ' '))
    	tempDict = dict()
		  	tempDict.[projectName] = point
		    self.assertEqual(team[0],point)
		    team.count = 5
		    self.assertRaises(IndexError,tempDict[point])

    def test_readFile(self, first, second, msg=None):
        """Assert that two multi-line strings are equal.

        If they aren't, show a nice diff.

        """
        self.assertTrue(isinstance(first, str),
                'First argument is not a string')
        self.assertTrue(isinstance(second, str),
                'Second argument is not a string')

        if first != second:
            message = ''.join(difflib.ndiff(first.splitlines(True),
                                                second.splitlines(True)))
            if msg:
                message += " : " + msg
            self.fail("Multi-line strings are unequal:\n" + message)

if __name__ == '__main__':
    unittest.main()
