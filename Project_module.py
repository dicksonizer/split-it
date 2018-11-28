class Project:
  MINIMUM_NAME_LENGTH = 3     
  MAXIMUM_NAME_LENGTH = 10

  MINIMUM_TEAM_SIZE = 3
  MAXIMUM_TEAM_SIZE = 5 

  def __init__(self, projectTitle, projectTeamSize, projectMembers):
    self.title = projectTitle
    self.size = projectTeamSize
    self.members = projectMembers
    
  def __str__(self):
    return self.title
  
  @property
  def title(self):
    return self._title
   
    
  @title.setter
  def title(self, titleName):
    if isValidName(titleName):
      self._title = titleName
    else:
      raise ValueError('you are an idiot')
           
  def isValidName(theString) :

    return theString.isalpha() == True \
        and len(theString) >= Project.MINIMUM_NAME_LENGTH \
        and len(theString) <= Project.MAXIMUM_NAME_LENGTH   
   
    
  @property
  def members(self):
    return self._members
  
  @members.setter
  def members(self,memberName):
    members = []ı