from Project_class import Project
from Person_class import Person

xr = Person('xr')
print(xr.asDict())

xr.votes('Abe',30)
print(xr.asDict())