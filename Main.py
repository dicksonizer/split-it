from try_module import Project
MENU_CHOICES = ['A', 'C', 'V', 'S', 'Q']
def printMenu():
    menuString = ("Welcome to Spliddit:\n"
                 "\tAbout (A)\n"
                 "\tCreate Project (C)\n"
                 "\tEnter Votes (V)\n"
                 "\tShow Project (S) \n"
                 "\tQuit (Q)")
    print(menuString)

def about() :
    aboutString = ("\n\nWelcome to Spliddit. "
                   "This application will allocate grades to "
                   "project participants based of the votes of their "
                   "peers.\n")
    print(aboutString)

def isValidOption(option):
    if len(option.strip()) == 0:
        return False
    elif option[0].upper() in MENU_CHOICES:
        return True
    else:
        return False
      
def getOption():  
    option = '*'
    
    while isValidOption(option) == False:
        printMenu()
        option = input("\nEnter an option: ")
   
    return option.upper()

def option_c():
  projectTitle = input(str('Enter Project title: '))
  
  while Project.isValidName(projectTitle) == False:
    print(("\n\t\tThe project name must be more than {} characters long, "
               "less than {} characters long and must contain only "
               "alphabetic characters. Try again.\n").format(Project.MINIMUM_NAME_LENGTH - 1, Project.MAXIMUM_NAME_LENGTH + 1))
    projectTitle = input("\n\tEnter project title: ")
  return projectTitle

    
def main() :
    option = '*'
    
    while option != 'Q':
        option = getOption()        
        if option == 'A':
            about()
        elif option =='C':
            option_c()
        elif option == 'S':
          print(project)
    print("\n\nBye, bye.")

        
# Start the program
if __name__ == "__main__":
    main()
