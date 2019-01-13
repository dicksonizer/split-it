class Person:
  
  def __init__(self, name):
    self.name = name
    self.votes = {}
    self.votesForMe = {}
    self.score = 0
    
  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name

  def asDict(self):
    return {'Name': self.name, 'Votes': self.votes, 'Votes Received': self.votesForMe, 'Score': self.score}

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
    if len(points) == 0:
      self._votes = points
    else:
      raise ValueError("Wrong input, try again")

  def votesForMe(self):
    return self._votesForMe

  def scores(self):
    return self._score

  def calculateScore(self):
    #VALIDATE IF ADDVOTES NOT USED / NO VOTES
    for key,value in self.votesForMe.items():
      tempPoint = round((1 / (1 + ((100-value[0])/value[0]) + ((100-value[1]))/value[1])) * 100)
    self.score = tempPoint


    # for key,value in self.asDict().items():
    #   if key == 'Votes':
    #     for name,votes in value.items():
    #       try:
    #         self._score[str(name)].append(int(votes))
    #       except:
    #         temparr = [int(votes)]
    #         self.score[str(name)]= temparr
    # print(self.score)

  def addVote(self, member, point):
    self._votes[member] = point

  def addVoteReceived(self, member, point):
    self.votesForMe[member] = point

  def getVotes(self):
    return self._votes


