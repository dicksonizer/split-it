"""
Split-it Deliverable 1
"""

def option_a():
  #Option A prints the description of the app
  print("\nSplit-it is a Fair Grade Allocator that determines the grade of each individual to a group project. The purpose of" 
  	    "the application is to help teams allocate the credit for a project so that all parties are satisfied with the outcome.\n")
  return_to_menu()

def option_c():
  #Option C creates a new project
  #Project Title variable takes in alphanumeric characters
  projectTitle = str(input('Enter the project name: \033[4m\0'))

  #Only accept numbers (more than 2) for teamNumber
  while True:
    try:
      teamNumber = int(input('\033[0mEnter the number of team members: \033[4m\0'))
      if teamNumber < 0:
        raise ValueError
      elif teamNumber < 3:
      	print('Try again; only teams of more than 2 are allowed')
      else:
        print('\033[0m \n')
        break
    except ValueError:
      print('Try again')

  #Accept alphanumeric characters for team member names
  for i in range(1,teamNumber+1):
    input('Enter the name of team member ' + str(i) + ': ' + '\033[4m\0')
    print('\033[0m', end='')
  return_to_menu()

def option_s():
  #Option S brings the user back to the menu for deliverable 1
  menu()
  
def option_v():
  #Option V brings the user back to the menu for deliverable 1
  menu()
  
def option_q():
  #Option Q exits the application
  exit()

def return_to_menu():
  back = input('Press <Enter> to return to the main menu: _')
  if back == '':
    menu()
  
def menu():
  #The function for menu
  print("\nWelcome to Split-it\n"
    	"\n\tAbout\t\t\t(A)"
    	"\n\tCreate Project\t\t(C)"
  		"\n\tEnter Votes\t\t(V)"
  		"\n\tShow Project\t\t(S)"
  		"\n\tQuit\t\t\t(Q)\n")
  
  option = str(input('\tPlease choose and option and press <Enter>: '))

  # Accept lowercase and uppercase variants
  if option == 'A' or option == 'a':
    option_a()
  elif option == 'C' or option == 'c':
    option_c()
  elif option == 'V' or option == 'v':
    option_v()
  elif option == 'S' or option == 's':
    option_s()
  elif option == 'Q' or option == 'q':
    option_q()
  else:
    print('\nWrong input, try again')
    menu()
    
def main():
  menu()
  
if __name__ == '__main__':
  main()