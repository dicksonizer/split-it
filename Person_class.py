class Person:
  
  def __init__(self, name):
    self.name = name
    self.votes = {}
    
  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name

  def asdict(self):
    return {'Name': self.name, 'Votes': self.votes}

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, theName):
    #no empty names
    if theName.isalpha():
      self._name = theName
    else:
      raise ValueError('Wrong Input, try again')

  @property
  def votes(self):
    return self._votes

  @votes.setter
  def votes(self, points):
    self._votes = points

  def addVote(self, member, point):
    self._votes[member] = point

  def getVotes(self):
    return self._votes

