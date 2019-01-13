import unittest
import unittest.mock
import Person_class

class TestPerson_class(unittest.TestCase):

	def test_name_setter(self, theName):
        self.assertTrue(theName.isalpha())
        self.assertRaise(ValueError)


    def test_votes_setter(self, points):
    	self.assertTrue(points(1, 2, 3))
    	self.assertRaise(points('e', ' ')ValueError)

    def test_calculateScore(self):
    	self.assertType(int)

    def test_votesForMe(self, member, points)
	    votes = dict()
		votes.[member] = point
		self.assertEqual(team[0],point)
		votes.count = 5
		self.assertRaises(IndexError,votes[point])


    def test_addVotes(self, member, points)
	    votes = dict()
			  	votes.[member] = point
			    self.assertEqual(team[0],point)
			    votes.count = 5
			    self.assertRaises(IndexError,votes[point])

if __name__ == '__main__':
    unittest.main()
