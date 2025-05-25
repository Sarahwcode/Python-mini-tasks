import csv

weather_data = [{
    "City": "Paris",
    "Temperature": 25,
    "Country": "France"
}, {
    "City": "New York",
    "Temperature": 23,
    "Country": "USA"
}, {
    "City": "Berlin",
    "Temperature": 22,
    "Country": "Germany"
}, {
    "City": "Bangkok",
    "Temperature": 35,
    "Country": "Thailand"
}]

field_names = ["City", "Temperature", "Country"]

file_name = "weather.csv"

with open(file_name, "w") as weather:
  writer = csv.DictWriter(weather, fieldnames=field_names)
  writer.writeheader()
  writer.writerows(weather_data)

with open("weather.csv", "r") as weather:
  reader = csv.reader(weather)
  next(reader)
  for row in reader:
    print(f"It is currently {row[1]} degrees in {row[0]}, {row[2]}")

#Fork the repl
#Print each line of the CSV file provided following this format:
#“It is currently 25 degrees in Paris, France”

temperatures = [10, 12, 14, 15]

# Print the list
print(temperatures)

# Modify an existing temperature
temperatures[2] = 17

# Print the modified item
print(temperatures[2])

# Add a temperature to the list
temperatures.append(20)
# Print the the newly added item
print(temperatures[4])

forecast = {
    "Monday": {
        "temperature": 21,
        "condition": "Rainy"
    },
    "Tuesday": {
        "temperature": 20,
        "condition": "Sunny"
    },
    "Wednesday": {
        "temperature": 23,
        "condition": "Cloudy"
    },
    "Thursday": {
        "temperature": 24,
        "condition": "Sunny"
    },
}

# Print the dictionary
print(forecast)

# Modify Wednesdays temperature to 25 and Sunny
forecast["Wednesday"]["temperature"] = 25
forecast["Wednesday"]["condition"] = "Sunny"

# Print Wednedays temperature
print(forecast["Wednesday"]["temperature"])

# Add forecast for Friday, 27, Cloudy
forecast["Friday"] = {"temperature": 27, "condition": "Cloudy"}

# Print Friday temperature such as "Friday's temperature will be 27 degrees and cloudy
print(
    f"Friday's temperature will be {forecast['Friday']['temperature']} degrees and {forecast['Friday']['condition']}"
)

temperatures = [{
    'city': "Paris",
    'continent': "Europe",
    "temperature": "12"
}, {
    'city': "Los Angeles",
    'continent': "North America",
    "temperature": "22"
}, {
    'city': "Paris",
    'continent': "Asia",
    "temperature": "18"
}, {
    'city': "New York",
    'continent': "North America",
    "temperature": "14"
}, {
    'city': "Sao Paulo",
    'continent': "South America",
    "temperature": "25"
}, {
    'city': "Toronto",
    'continent': "North America",
    "temperature": "2"
}]

# Given the list of temperatures, calculate and print the average temperature of north American cities

north_america_temp = 0
north_america_city = 0

for temp in temperatures:
  if temp["continent"] == "North America":
    north_america_temp += int(temp['temperature'])
    north_america_city += 1

if north_america_city > 0:
  average_temp = north_america_temp / north_america_city
  print(f"Average temperature in north america is: {round(average_temp, 2)}")


def customer_information(customer):
  """
  Extract the data from the customer and display it
  """
  customer_id = customer[0]
  first_name = customer[2]
  last_name = customer[3]
  email_address = customer[9]
  print(f"Customer #{customer_id}, {first_name} {last_name}, {email_address}")


def organise_customer_information():
  """
  Loop through each line from the customer file 
  Diplay each customer's id, first name, last name, email and company
  """
  with open('customers.csv', 'r') as file:
    customers = csv.reader(file)

    for customer in customers:
      customer_information(customer)


print(organise_customer_information())


def calculate_population(populations):
  """
  Loop through each population dictionary and sum up the population
  """
  total_population = 0
  for population in populations:
    total_population += int(population["population"])
  return total_population


"""
Display the total population in millions
"""


def display_population_million(total_population):
  total_in_millions = round(total_population / 1000000)
  print(f"The total population is {total_in_millions} million people")


"""
Given the list of populations, calculate and print the total populations of the countries
"""

populations = [
    {
        'country': "France",
        "population": "60000000"
    },
    {
        'country': "Spain",
        "population": "50000000"
    },
    {
        'country': "USA",
        "population": "30000000"
    },
    {
        'country': "Australia",
        "population": "25000000"
    },
    {
        'country': "Canada",
        "population": "38000000"
    },
]
"""
Result of total population
"""

total_population = calculate_population(populations)
display_population_million(total_population)

# Display the total population such as, the total population is 203 million people
