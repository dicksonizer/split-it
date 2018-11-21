"""
Split-it Deliverable 1
Group D
Github Link: https://github.com/dicksonizer/split-it
comment
"""

def option_a():
  #Option A prints the description of the app
  print('\nSplit-it is a Fair Grade Allocator that determines the grade of each individual to a' 
        ' group project. The purpose of the application is to help teams allocate the credit for'
        ' a project so that all parties are satisfied with the outcome.\n')
  return_to_menu()

def option_c():
  #Option C creates a new project
  #Project Title variable takes in alphanumeric characters
  projectTitle = str(input('\nEnter the project name: '))

  #Only accept integers (more than 2) for teamNumber
  while True:
    try:
      teamNumber = int(input('Enter the number of team members: '))
      if teamNumber < 3:
        print('Try again: only teams of more than 2 are allowed')
      else:
        break
    except ValueError:
      print('Try again: you must input a number')
  print('\n')  

  #Accept alphanumeric characters for team member names
  for i in range(1,teamNumber+1):
    input('\tEnter the name of team member ' + str(i) + ': ')
  print('\n')
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
  #Return to menu function used in option_a and option_c
  while True:
    back = input('Press <Enter> to return to the main menu: ')
    if back != '':
      print('Wrong input, try again')
    else:
      menu()
  
def menu():
  #The function for menu
  print('\nWelcome to Split-it\n'
        '\n\tAbout\t\t(A)'
        '\n\tCreate Project\t(C)'
        '\n\tEnter Votes\t(V)'
        '\n\tShow Project\t(S)'
        '\n\tQuit\t\t(Q)\n')
  
  option = str(input('\tPlease choose an option and press <Enter>: '))

  # Accept either lowercase or uppercase variants
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
