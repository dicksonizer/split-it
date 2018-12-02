import unittest
import unittest.mock
import Project_class

class TestProject_class(unittest.TestCase):

	def test_title_setter(self, titleName):
		self.assertTrue(titleName(Project.isValidName())True)
		self.assertFalse(titleName(ValueError))

	def test_isValidName(self, name):
		self.assertTrue(name('thename'))
		self.assertFlse(name(4, ' ', '12'))

	def test_isInTeam(self, name, theList):
		a = list()
		  	team.append(name)
		    self.assertEqual(theList[0],name)
		    team.count = 5
		    self.assertNotIn(name, theList)

	def test_size_setter(self, teamSize):
		self.assertTrue(teamSize(Project.isValidTeamSize())True)
		self.assertFalse(teamsize(6, 7, 'n')(ValueError))

	def test_isValidTeamSize(self, theSize):
		assertTrue(theSize(4, 5, 1, 2))
		assertFalse(theSize(' ', '4'))

	def test_isInteger(self, number):
		assertTrue(number(4, 3, 2))
		assertFalse(number('', ' ', '4'))
