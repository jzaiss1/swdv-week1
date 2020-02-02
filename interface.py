# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Week 1 Assignment - In your Interface 

class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)

  def __contains__(self,classmate):
    return classmate in self.__myTeam

  def __iter__(self):
      self.__iter = 0
      return self

  def __next__(self):
      if self.__iter < len(self.__myTeam):
          classmate = self.__myTeam[self.__iter]
          self.__iter += 1
          return classmate
      else:
          raise StopIteration

  def checkClassmate(self,name):
    if name in self.__myTeam:
        answer = 'Yes'
    else:
        answer = 'No'

    print('Is {} in the class? {}\n'.format(name, answer))
    
def main():
  classmates = Teams(['John', 'Steve', 'Tim'])

  # Requirement 1
  people = [ 'John', 'Jenny', 'Jim', 'Tim' ]
  for person in people:
      classmates.checkClassmate(person)

  # Requirement 2
  name = iter(classmates)
  x = 0
  while x != len(classmates):
      print('{} is a classmate'.format(next(name)))
      x += 1

  # Requirement 3
  print('\nThere are {} classmates\n'.format(len(classmates)))

main()

# Question 4
# The interface is how the user will interact with the class.
# The inplementation is how the class operates.
# In this class the interface contains the checkClassmate() method, which
# uses the __contains__ protocol which is part of the inplementation

