class Person:
  
  def __init__(self, name):
    self.name = name
    
  def __str__(self):
    return self.name
    
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, theName):
    self