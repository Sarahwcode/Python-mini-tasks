class person:

  def __init__(self, first_name, year_of_birth):
    self.first_name = first_name
    self.year_of_birth = year_of_birth

  def welcome(self):
    if self.year_of_birth < 2000:
      print(
          f"Welcome {self.first_name}, you were born during the 20th century")
    else:
      print(
          f"Welcome {self.first_name}, you were born during the 21st century")
