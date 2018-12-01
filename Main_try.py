from Project_class import Project
from Person_class import Person

MENU_CHOICES = ['A', 'C', 'V', 'S', 'Q']
projectDict = {}

def about() :
		aboutString = ("\n\nWelcome to Spliddit. "
									 "This application will allocate grades to "
									 "project participants based of the votes of their "
									 "peers.\n")
		print(aboutString)

def printMenu():
		menuString = ("\nWelcome to Spliddit:\n\n"
								 "\tAbout (A)\n"
								 "\tCreate Project (C)\n"
								 "\tEnter Votes (V)\n"
								 "\tShow Project (S) \n"
								 "\tQuit (Q)")
		print(menuString)

#Function to validate user input for menu choices
def isValidOption(option):
		if len(option.strip()) == 0:
				return False
		elif option[0].upper() in MENU_CHOICES:
				return True
		else:
				return False
	
#Function to take input from user for menu choices
def getOption():  
		option = '*'
		
		while isValidOption(option) == False:
				printMenu()
				option = input("\nEnter an option: ")
	 
		return option.upper()

#Function to create project. Project objects are pushed in projectDict with its title being the key and object being the value
def createProject():
	projectTitle = input(str('Enter Project title: '))
	
	while Project.isValidName(projectTitle) == False:
		print(("\n\t\tThe project name must be more than {} characters long, "
							 "less than {} characters long and must contain only "
							 "alphabetic characters. Try again.\n").format(Project.MINIMUM_NAME_LENGTH - 1, Project.MAXIMUM_NAME_LENGTH + 1))
		projectTitle = input("\n\tEnter project title: ")
	
	
	teamSize = input('Enter the number of team members: ')
		
	while Project.isValidTeamSize(teamSize) == False :
		print(("\n\t\tThe team size must be more than {} and less than {}. "
							 "Try again.").format(Project.MINIMUM_TEAM_SIZE - 1, Project.MAXIMUM_TEAM_SIZE + 1))
		teamSize = input('Enter the number of team members: ')
	
	team = []
	for i in range(int(teamSize)):
		personName = input("\tEnter name of team member {}: ".format(i+1))

		while Project.isValidName(personName) == False or Project.isInTeam(personName, team) == True:
			print(("\n\t\tThe name must be more than {} characters long,"
						 " less than {} characters long and cannot contain "
						 "numbers or punctuation characters and cannot be repeated").format(Project.MINIMUM_NAME_LENGTH - 1,
																													Project.MAXIMUM_NAME_LENGTH + 1))
			personName = input("\tEnter name of team member {}: ".format(i+1))
	 
		person = Person(personName)
		print("This is the id of person created in Option_C", id(person),person.asdict())
		team.append(person)
	
	project = Project(projectTitle, teamSize, team) 
	#Make a method in project for getTitle
	#Then append {Title: Project Object}
	projectDict[project.title] = project
	print(project)
	print(projectDict)

def setVotes():
	#while len(projectDict) > 0
	projectName = input("Enter the project name from the following list: " + str(",".join("{}".format(k)for k in projectDict.keys())) + "\nEnter Project Title: ")

	while projectName not in projectDict.keys():
		print("\n\t\tThe project you have entered is not found, please try again.")

		projectName = input("Enter the project name from the following list: " + str(",".join("{}".format(k)for k in projectDict.keys())) + "\nEnter Project Title: ")

		
	names = projectDict[projectName].team
	for i in range(len(names)):
		exclude = names[i]
		tempDict = {}
		for j in names:
			if j == exclude:
				pass
			else:
				point = int(input("Enter " + str(names[i]) + "\'s points for " + str(j) + ": "))
				tempDict[str(j)] = point
		if sum(tempDict.values()) == 100:
			for key, values in tempDict.items():
				names[i].addVote(key,values)
	for k in names:
		print("This is the id of person after votes is added",id(k),k.asdict())

	print("Unfortunately, the dict of member isn't shown here, but we can modify it",projectDict)

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
					print("Not implemented yet")
		print("\n\nBye, bye.")

				
# Start the program
if __name__ == "__main__":
		main()
