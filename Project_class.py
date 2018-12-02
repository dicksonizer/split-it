from Person_class import Person

class Project:
	MINIMUM_NAME_LENGTH = 3
	MAXIMUM_NAME_LENGTH = 10

	MINIMUM_TEAM_SIZE = 3
	MAXIMUM_TEAM_SIZE = 5

	def __init__(self, projectTitle, projectTeamSize, projectTeam):
		self.title = projectTitle
		self.size = projectTeamSize
		#Issue 
		self._team = projectTeam


	def __str__(self):
		return 'Title: ' + self.title + '\nSize: ' + self.size + '\nMembers: ' + str(self._team)

	def __repr__(self):
		return '{\'Title\': ' + '\'' + self.title + '\'' + ', \'Size\': ' + self.size + ', \'Members\': ' + str(self._team) +'}'

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, titleName):
		if Project.isValidName(titleName):
			self._title = titleName
		else:
			raise ValueError('you are an idiot')

	def isValidName(theString):
		return theString.isalpha() == True and len(theString) >= Project.MINIMUM_NAME_LENGTH and len(theString) <= Project.MAXIMUM_NAME_LENGTH

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, teamSize):
		if Project.isValidTeamSize(teamSize):
			self._size = teamSize
		else:
			raise ValueError('Wrong Input')

	def isValidTeamSize(theSize):
		return Project.isInteger(theSize) and int(theSize) >= Project.MINIMUM_TEAM_SIZE and int(theSize) <= Project.MAXIMUM_TEAM_SIZE

	def isInteger(number):
		try:
			int(number)
			return True
		except ValueError:
			return False

	@property
	def team(self):
		return self._team

	@team.setter
	def team(self, members):
		if len(members) == self.size:
			self._team = members

	
	def isInTeam(name, theList):
		if name in theList:
			return True
		else:
			return False

