import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All cities in Germany:")
temps = []
for city in cities:
    if city['country'] == 'Germany':
        temps.append(city)
print(temps)
print()

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C:")
spain = []
for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) > 12:
        spain.append(city)
print(spain)
print()

# Count the number of unique countries
print("the number of unique countries:")
count = []
for city in cities:
    if city['country'] not in count:
        count.append(city['country'])
    else:
        pass
print(len(count))
print()
# Print the average temperature for all the cities in Germany
print("the average temperature for all the cities in Germany:")
temps = []
for city in cities:
    if city['country'] == 'Germany':
        temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the max temperature for all the cities in Italy
print("the max temperature for all the cities in Italy")
Italy = []
for city in cities:
    if city['country'] == 'Italy':
        Italy.append(float(city['temperature']))
print(max(Italy))
print()
