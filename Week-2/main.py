import csv

file = open("TODO.txt", "r")
todo_list = file.readlines()
print("To do list:")
for tasks in todo_list:
  print (f"-{tasks.strip()}")
  
file.close()
#Create a new TODO.txt file with some tasks you need to do
#Display each item in a nice readable way using Python
print("")
with open ("Temperature.csv", "r") as file:
    reader = csv.reader(file)
    for temp in reader:
      print (f"It is {temp[2]} and {temp[1]}ºC in {temp[0]}")
#Read temperatures.csv and display the temperatures following this format:
#“It is cloudy and 12ºC in Toronto”

file = open("Cities.csv", "w")
file.write("Lisbon,12,sunny\n")
file.write("Paris,15,cloudy\n")
file.write("Tokyo,20,rainy\n")
file.close()
file = open("Cities.csv", "a")
file.write("London,10,Cloudy\n")
file.write("New York,20,Sunny\n")
#Add 2 more cities with temperatures, and condition
#Ensure the file is well formatted after you run your script

#try:
with open ("CitiesTwo.csv", "r") as file:
  reader = csv.reader(file)
  
  for city in reader: 
    try:
      print(f"It is {city[1]} in {city[0]}")
    except IndexError:
      print ("It is not possible to read the data")

 
    
#except Exception:
  #print ("It is not possible to read the data")
  
#Display each line of the CSV file as follows 
#“It is 24 in Lisbon.”
#Use exception handling when it’s not possible to read the data
with open ("customers.csv", "r") as file:
  customer_reader = csv.reader(file)
  for customer in customer_reader:
    print(f"\nCustomer #{customer[0]}, {customer[2]} {customer[3]}, {customer[9]}")
      
      
      
      #Display each customer from the CSV in this format:
#“Customer #53, Patricia Goodwin, vaughanchristy@lara.biz”