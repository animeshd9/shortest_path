import itertools
import random
#m = int(input("Enter number of rows: "))
n = int(input("Enter the No. of cities which you want to visit: "))

def generate_random_cites(n):
	cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "San Francisco", "Charlotte", "Indianapolis", "Seattle", "Denver", "Washington DC"]
	generated_cities = []
	for i in range(n):
		city = random.choice(cities)
		generated_cities.append(city)
		cities.remove(city)
	return generated_cities
		
# Initialize empty matrix
distance_matrix = []
time_matrix =[]
cities=generate_random_cites(n)
print(cities)

# Iterate over rows and columns to get user input for each element
#for loop of cities
# for i in range(n):
#     city_Name = input("Enter the name of cities ")
#     cities.append(city_Name)
# m=len(cities)
# print(cities)
#for loop of distance_matrix

# if there are two city then distance_matrix will be 2*2 matrix and take only one input

print ("Enter distance for all cities ")
for i in range(len(cities)):
    row = []
    for j in range(n):
        if i==j:
            row.append(0)
        else:
            element = int(input("Enter distance between " + cities[i] + " and " + cities[j] + " in KM " + " "))
            row.append(element)
    distance_matrix.append(row)
print(distance_matrix)
#for loop of time_matrix
print("Enter the value for time matrix ")
for i in range(len(cities)):
    row = []
    for j in range(n):
        if i==j:
            row.append(0)
        else:
            element = int(input("Enter time between " + cities[i] + " and " + cities[j] + " in Hour " + " "))
            row.append(element)
    time_matrix.append(row)
#brute force permutation
def motsp_brute_force(cities, time_matrix, distance_matrix):
    # Generate all possible permutations of the cities
    all_permutations = list(itertools.permutations(cities))

    # Calculate the total distance and time of each permutation and return the shortest one
    shortest_distance = float('inf')
    shortest_time = float('inf')
    shortest_path = None
    for path in all_permutations:
        distance = 0
        time = 0
        for i in range(len(path)-1):
            distance += distance_matrix[i][i+1]
            time += time_matrix[i][i+1]
        if distance < shortest_distance and time < shortest_time:
            shortest_distance = distance
            shortest_time = time
            shortest_path = path

    return shortest_path, shortest_distance, shortest_time

# Example usage
    #time_matrix = [[0, 1, 2, 3],              
      #          [1, 0, 3, 2],
              #  [2, 3, 0, 1],
               # [3, 2, 1, 0]]
shortest_path, shortest_distance, shortest_time = motsp_brute_force(cities, time_matrix, distance_matrix)
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)
print("Shortest time:",shortest_time)