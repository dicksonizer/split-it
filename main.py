"""
Split-it Deliverable 1
Group D
Github Link: https://github.com/dicksonizer/split-it
Adapted on Rae Harbird's code, Deliverable 1 Spliddit
"""

from Project_class import Project
from Person_class import Person

MENU_CHOICES = ['A', 'C', 'V', 'S', 'Q']
projectDict = {}

def about() :
		aboutString = ('\n\nWelcome to Split-it. '
									 'This application will allocate grades to '
									 'project participants based of the votes of their '
									 'peers.\n')
		print(aboutString)

def printMenu():
		menuString = ('Welcome to Split-it:\n\n'
								 '\tAbout \t\t(A)\n'
								 '\tCreate Project \t(C)\n'
								 '\tEnter Votes \t(V)\n'
								 '\tShow Project \t(S) \n'
								 '\tQuit \t\t(Q)')
		print(menuString)

#Function to validate user input for menu choices
def isValidOption(option):
		if len(option.strip()) == 0:
				return False
		elif option[0].upper() in MENU_CHOICES:
				return True
		else:
				return False
	
#Function to take input from user for menu choices. Returns user input to uppercase
def getOption():  
		option = '*'
		
		while isValidOption(option) == False:
				printMenu()
				option = input('\nEnter an option: ')
	 
		return option.upper()

#Function to create project. Project objects are constructed with title, team size and list of team members
#Project objects are then pushed in projectDict with its title being the key and object being the value
def createProject():
	projectTitle = input(str('Enter Project title: '))
	
	while Project.isValidName(projectTitle) == False:
		print(('\n\t\tThe project name must be more than {} characters long, '
							 'less than {} characters long and must contain only '
							 'alphabetic characters. Try again.\n').format(Project.MINIMUM_NAME_LENGTH - 1, Project.MAXIMUM_NAME_LENGTH + 1))
		projectTitle = input('\n\tEnter project title: ')
	
	
	teamSize = input('Enter the number of team members: ')
		
	while Project.isValidTeamSize(teamSize) == False :
		print(('\n\t\tThe team size must be more than {} and less than {}. '
							 'Try again.').format(Project.MINIMUM_TEAM_SIZE - 1, Project.MAXIMUM_TEAM_SIZE + 1))
		teamSize = input('Enter the number of team members: ')

	print()

	#Create team list to append Person objects. This list will be used to construct Project object
	#Created tempTeam list to append personName for validation: reprompt for user input if name is repeated
	team = []
	tempTeam = []
	for i in range(int(teamSize)):
		personName = input('\tEnter name of team member {}: '.format(i+1))

		while Project.isValidName(personName) == False or Project.isInTeam(personName, tempTeam) == True:
			print(('\n\t\tThe name must be more than {} but less than {} characters long,'
						 ' alphabetic and cannot be repeated.').format(Project.MINIMUM_NAME_LENGTH - 1,
																						Project.MAXIMUM_NAME_LENGTH + 1))
			personName = input('\tEnter name of team member {}: '.format(i+1))
	 
		tempTeam.append(personName)
		person = Person(personName)
		team.append(person)
		#The line of code below was used during testing to compare the ID of person objects 
		#before and after adding votes
		# print('This is the id of person created in Option C', id(person),person.asDict())
			
	project = Project(projectTitle, teamSize, team) 
	projectDict[project.title] = project
	print('Project created:',projectDict,'\n')


#Prompt user to enter project name and allocate votes to members
def setVotes():
	if not projectDict:
		print('No project objects exist!\n')
	else:
		projectName = input('Choose a project name from the following list: ' + 
							str(','.join('{}'.format(k)for k in projectDict.keys())) + '\nEnter Project Title: ')

		while projectName not in projectDict.keys():
			print('\n\t\tThe project you have entered is not found, please try again.')

			projectName = input('Choose a project name from the following list: ' + 
								str(', '.join('{}'.format(k)for k in projectDict.keys())) + '\nEnter Project Title: ')
		print('There are ' + projectDict[projectName].size + ' team members.\n')
		addPoints(projectName)

#Add points for each member
def addPoints(projectName):
	#Create a list that contains the list of Person objects in the corresponding project
	names = projectDict[projectName].team
	newDict = {}
	#This for loop adds Person instance with the votes they given
	for i in range(len(names)):
		#Created variable exclude so that people can't vote for themselves
		exclude = names[i]
		#Created tempDict to store the votes given to one's teammates. 
		tempDict = {}
		flagDict = {}
		print('Enter ' + str(names[i]) + '\'s votes, points must add up to 100:\n')

		successful = False
		while not successful:
			for j in names:
				if j == exclude:
					pass
				else:
					#Prompt user to input point for his/her team members and add to tempDict
					point = input('Enter ' + str(names[i]) + '\'s points for ' + str(j) + ': ')

					while Project.isInteger(point) == False:
						print('Please input a number')
						point = input('Enter ' + str(names[i]) + '\'s points for ' + str(j) + ': ')

					tempDict[str(j)] = int(point)

			#If all votes are assigned and the sum of votes is equal to 100, then move on to next person
			if len(tempDict) == ((len(names)) - 1) and (sum(tempDict.values()) == 100):
					for key, values in tempDict.items():
						names[i].addVote(key,values)
						flagDict[key] = values
					successful = True
					newDict[names[i]] = flagDict
					print(newDict)
			else:					
				print('\nPoints you entered do not add up to 100, try again!\n')
		print()	
	
	#This for loop creates a dictionary of {Person instance : Votes Received}
	finalDict = {}
	for key,value in newDict.items():
		for name,votes in value.items():
			try:
				finalDict[str(name)].append(int(votes))
			except:
				temparr = [int(votes)]
				finalDict[str(name)]= temparr
	print(finalDict)

	#This for loop uses the above dictionary to assign Person instance --> Votes Received
	for personInstance in names:
		for key, values in finalDict.items():
			if key == str(personInstance):
				print(key,values)
				personInstance.addVoteReceived(key,values)

	#For testing; Check that every person objects are assigned votes (and the person who voted)
	print('Person object in project now contain votes:')
	for personInstance in names:
		print('' + personInstance.name + '\'s object is: ', end = '')
		print(personInstance.asDict())

def showVotes():
	if not projectDict:
		print('No project objects exist!\n')
	else:
		projectName = input('Choose a project name from the following list: ' + 
							str(','.join('{}'.format(k)for k in projectDict.keys())) + '\nEnter Project Title: ')

		while projectName not in projectDict.keys():
			print('\n\t\tThe project you have entered is not found, please try again.')

			projectName = input('Choose a project name from the following list: ' + 
								str(', '.join('{}'.format(k)for k in projectDict.keys())) + '\nEnter Project Title: ')
		print('\nThere are ' + projectDict[projectName].size + ' team members.\n')

	print('The point allocation based on votes is:\n')

	names = projectDict[projectName].team
	#This for loop calculates score of each person Instance
	for personInstance in names:
		personInstance.calculateScore()
		print("\t" + str(personInstance) + ":" + "\t\t" + str(personInstance.score))
	





def main() :

		option = '*'
		
		while option != 'Q':
				option = getOption()        
				if option == 'A':
						about()
				elif option == 'C':
						createProject()
				elif option == 'V':
						setVotes()
				elif option == 'S':
					showVotes()

		#Read File

		print('\n\nBye, bye.')

				
# Start the program
if __name__ == '__main__':
		main()

