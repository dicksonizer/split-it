"""
Split-it Deliverable 1
Group D
Github Link: https://github.com/dicksonizer/split-it

"""

from Project_class import Project
from Person_class import Person

MENU_CHOICES = ['A', 'C', 'V', 'S', 'Q']
projectDict = {}

def about() :
		aboutString = ("\n\nWelcome to Split-it. "
									 "This application will allocate grades to "
									 "project participants based of the votes of their "
									 "peers.\n")
		print(aboutString)
		return_to_menu()

def printMenu():
		menuString = ("Welcome to Split-it:\n\n"
								 "\tAbout \t\t(A)\n"
								 "\tCreate Project \t(C)\n"
								 "\tEnter Votes \t(V)\n"
								 "\tShow Project \t(S) \n"
								 "\tQuit \t\t(Q)")
		print(menuString)

def return_to_menu():
  #Return to menu function used in option_a and option_c
  while True:
    back = input('Press <Enter> to return to the main menu: ')
    if back != '':
      print('Wrong input, try again')
    else:
      main()

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
				option = input("\nEnter an option: ")
	 
		return option.upper()

"""Function to create project. Project objects are constructed with title, team size and list of team members.
Project objects are then pushed in projectDict with its title being the key and object being the value. """
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
	print()

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
		# print("This is the id of person created in Option_C", id(person),person.asdict())
		team.append(person)
	
	project = Project(projectTitle, teamSize, team) 
	projectDict[project.title] = project
	print("Project created:",projectDict,"\n")
	return_to_menu()

#Prompt user to enter project name and allocate votes to members
def setVotes():
	if not projectDict:
		print("No project objects exist!\n")
		return_to_menu()
	projectName = input("Choose a project name from the following list: " + str(",".join("{}".format(k)for k in projectDict.keys())) + "\nEnter Project Title: ")

	while projectName not in projectDict.keys():
		print("\n\t\tThe project you have entered is not found, please try again.")

		projectName = input("Choose a project name from the following list: " + str(", ".join("{}".format(k)for k in projectDict.keys())) + "\nEnter Project Title: ")
	print("There are " + projectDict[projectName].size + " team members.\n")
	addPoints(projectName)

#Add points for each member
def addPoints(projectName):
	#Create a list that contains the array of Person objects in the corresponding project
	names = projectDict[projectName].team

	for i in range(len(names)):
		#Created variable exclude so that people can't vote for themselves
		exclude = names[i]
		#Created tempDict to store 
		tempDict = {}
		print("Enter " + str(names[i]) + "\'s votes, points must add up to 100:\n")

		successful = False
		while not successful:
			for j in names:
				if j == exclude:
					pass
				else:
					#Prompt user to input point for his/her team members and add to tempDict
					point = input("Enter " + str(names[i]) + "\'s points for " + str(j) + ": ")

					while Project.isInteger(point) == False:
						print("Please input a number")
						point = input("Enter " + str(names[i]) + "\'s points for " + str(j) + ": ")

					tempDict[str(j)] = int(point)

				
			if len(tempDict) == ((len(names)) - 1) and (sum(tempDict.values()) == 100):
					for key, values in tempDict.items():
						names[i].addVote(key,values)
					successful = True
			else:					
				print("\nPoints you entered do not add up to 100, try again!\n")
		print()	
	
	#Check that person objects are assigned votes and the person who gave the vote
	for personObject in names:
		print("Person object in project now contain votes:",personObject.asdict())

	return_to_menu()


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
