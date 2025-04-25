
class weather:

  def __init__(self, city):
    self.city = city

  def set_weather(self, temperature, condition):
    self.temperature = temperature
    self.condition = condition

  def display_weather(self):
    print(
        f"The weather in {self.city} is {self.temperature}°C and the condition is {self.condition}"
    )


#- Create a new Weather Class
#- Create a method called set_weather that sets the weather temperature and condition
#- Create a method called display_weather(), which will display the weather information of a class object
#- Test it with some fake data such as Paris, 27, sunny
