from person import person

from french import french_user
from userperson import person_user
from spanish import spanish_user
from weather import weather


class user:

  def __init__(self, first, last):
    self.first = first
    self.last = last

  def full_name(self):
    print(f"{self.first} {self.last}")

  def change_first_name(self):
    self.first = "Fiona"


name = user("Sarah", "Ward")
second_name = user("Daniel", "Wood")
name.full_name()
second_name.full_name()
name.change_first_name()
name.full_name()

#Define a class User who receives 2 attributes in the initializer, a first name, and a last name.---
#Create a method called full_name, which returns the user's full name
#Create 2 users with 2 different names and print their full name
#Change the first name of the first object and print the full name again

person_one = person("Sarah", 1990)
person_two = person("Daniel", 2015)
person_one.welcome()
person_two.welcome()

#Define a class called User, which receives the first name and the year of birth
#Create a method called “Welcome” which should display “Welcome Name, you were born during the 20th century” or 21st if the user was born after 2000
#Welcome 2 users to test this out





user_call = french_user("Sarah")
user_call.french()
user_call_two = spanish_user("Sarah")
user_call_two.spanish()

city = weather("London")
city.set_weather(12, "Cloudy")
city.display_weather()

#Add a new class inheriting from User called FrenchUser and when greeting, it should say “Bonjour - Name”
#Add a new class inheriting from User called SpanishUser and when greeting, it should say “Hola! - Name”
#Test both classes
#Move each class into their files
