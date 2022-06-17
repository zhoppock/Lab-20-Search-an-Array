# MichiganCities.py - This program prints a message for invalid cities in Michigan.  
# Input:  Interactive
# Output:  Error message or nothing
cities = 0
answer = "N"
# Initialized list of cities
citiesInMichigan = ["Acme", "Albion", "Detroit", "Watervliet", "Coloma", "Saginaw", "Richland", "Glenn", "Midland", "Brooklyn"] 

# Get user input
inCity = input("Enter name of city: ")

# Write your test statement here to see if there is a match.
while cities < 10:
      if inCity == citiesInMichigan[cities]:
        answer = "Y"
      cities += 1
# If the city is found, print "City found."
if answer == "Y":
  print("City Found")
# Otherwise, "Not a city in Michigan" message should be printed. 
else:
  print("Not a city in Michigan")   