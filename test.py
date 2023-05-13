import pandas as pd
import math
import itertools
import random
import heapq

df = pd.read_csv("data.csv")
def calculate_distance(city1, city2):
    df1 = df[df["city"] == city1]
    df2 = df[df["city"] == city2]
    lat1 = df1["lat"].values[0]
    lon1 = df1["lng"].values[0]
    lat2 = df2["lat"].values[0]
    lon2 = df2["lng"].values[0]
    return haversine_distance(lat1, lon1, lat2, lon2)

def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    res = r * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))
    return round(res, 2)


def calculate_time(distance, speed):
    time = distance / speed
    return round(time, 2)



n = int(input("Enter the No. of cities which you want to visit: "))

def generate_random_cites(n):
        # Generate a list of citiee from the dataframe
    cities = list(df["city"])
    generated_cities = []
    for i in range(n):
        city = random.choice(cities)
        generated_cities.append(city)
        cities.remove(city)
    return generated_cities

def create_graph(distance_matrix, time_matrix):
    """
    Creates a graph represented as a dictionary from distance and time matrices.

    Args:
        distance_matrix (list of lists): A matrix representing the distances between
            nodes. distance_matrix[i][j] is the distance between nodes i and j. If there
            is no edge between nodes i and j, distance_matrix[i][j] should be set to None.
        time_matrix (list of lists): A matrix representing the travel times between
            nodes. time_matrix[i][j] is the travel time between nodes i and j. If there
            is no edge between nodes i and j, time_matrix[i][j] should be set to None.

    Returns:
        A dictionary representing the graph. Keys are nodes, values are dictionaries
        representing the edges from that node. Each edge dictionary has keys "node" (the
        destination node), "distance" (the distance between the nodes), and "time" (the
        travel time between the nodes).
    """
    graph = {}
    num_nodes = len(distance_matrix)

    # Create a dictionary for each node in the graph
    for i in range(num_nodes):
        graph[i] = []

    # Add edges to the graph based on the distance and time matrices
    for i in range(num_nodes):
        for j in range(num_nodes):
            if distance_matrix[i][j] is not None:
                graph[i].append({
                    "node": j,
                    "distance": distance_matrix[i][j],
                    "time": time_matrix[i][j]
                })

    return graph



def dijkstra(graph, source, dest):
    """
    Runs Dijkstra's algorithm on a graph to find the shortest path from a source node
    to a destination node.

    Args:
        graph (dict): A dictionary representing the graph. Keys are nodes, values are
            dictionaries representing the edges from that node. Each edge dictionary
            has keys "node" (the destination node), "distance" (the distance between
            the nodes), and "time" (the travel time between the nodes).
        source (int): The index of the source node.
        dest (int): The index of the destination node.

    Returns:
        A tuple containing the shortest path (as a list of node indices), the total
        distance of the path, the total time of the path, and the list of cities in
        the shortest path (including the source and destination cities) as indices. If no path
        exists between the source and destination nodes, the shortest path is an empty
        list and the distance, time, and cities are all None.
    """
    # Initialize distance and time dictionaries with infinity for all nodes except
    # the source node, which has a distance and time of 0
    distance = {node: float('inf') for node in graph}
    time = {node: float('inf') for node in graph}
    distance[source] = 0
    time[source] = 0

    # Initialize the heap with the source node and its distance
    heap = [(0, source)]

    # Initialize the path dictionary, which will be used to reconstruct the shortest path
    path = {}

    # Initialize the list of cities in the shortest path
    cities = {}

    while heap:
        # Pop the node with the smallest distance from the heap
        (dist, node) = heapq.heappop(heap)

        # If we've already visited this node with a shorter distance, skip it
        if dist > distance[node]:
            continue

        # Check each neighbor of the current node
        for edge in graph[node]:
            neighbor = edge["node"]
            new_distance = distance[node] + edge["distance"]
            new_time = time[node] + edge["time"]

            # If we've found a shorter path to the neighbor, update its distance, time,
            # path, and list of cities
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                time[neighbor] = new_time
                path[neighbor] = node
                cities[neighbor] = cities[node] + [neighbor] if node in cities else [source, neighbor]
                heapq.heappush(heap, (new_distance, neighbor))

    # If no path was found, return empty lists and None
    if distance[dest] == float('inf'):
        return [], None, None, None

    # Reconstruct the shortest path from the path dictionary
    node = dest
    path_nodes = [node]
    while node != source:
        node = path[node]
        path_nodes.append(node)
    path_nodes.reverse()

    # Return the shortest path, total distance, total time, and list of cities as indices
    city_indices = [source] + [node for node in cities[dest][1:]]
    return path_nodes, distance[dest], time[dest], city_indices



# Initialize empty matrix
distance_matrix = []
time_matrix =[]
cities=generate_random_cites(n)
print(cities)

print ("Enter distance for all cities ")
for i in range(len(cities)):
    # calculate distance between given cities

    row = []
    for j in range(n):
        if i==j:
            row.append(0)
        else:
            element = calculate_distance(cities[i], cities[j])
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
            element = calculate_time(distance_matrix[i][j], 80)
            row.append(element)
    time_matrix.append(row)

# Function to create a graph from the distance matrix

graph = create_graph(distance_matrix, time_matrix)
print(graph)

shortest_path, shortest_distance, shortest_time, city = dijkstra(graph,0 , 5 )
print("Shortest path:", [cities[i] for i in shortest_path])
print("Shortest distance:", shortest_distance)
print("cities:", city)
print("Shortest time:",shortest_time)
