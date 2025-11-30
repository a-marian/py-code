import itertools

# Define cities and distances between them
# distances[i][j] = distance from city i to city j
cities = ['A', 'B', 'C', 'D']

# Distance matrix (symmetric - distance A to B = distance B to A)
distances = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

def calculate_route_distance(route, distances):
    """Calculate total distance for a given route"""
    total_distance = 0

    # Add distances between consecutive cities
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]

    # Add distance back to starting city
    total_distance += distances[route[-1]][route[0]]

    return total_distance

def solve_tsp_bruteforce(cities, distances):
    """Solve TSP by checking all possible routes (brute force)"""

    # Start from first city, permute the rest
    start_city = cities[0]
    other_cities = cities[1:]

    # Generate all possible routes
    all_routes = itertools.permutations(other_cities)

    best_route = None
    best_distance = float('inf')

    print("Checking all possible routes:\n")

    # Check each route
    for route in all_routes:
        # Add starting city at the beginning
        full_route = [start_city] + list(route)

        # Calculate distance
        distance = calculate_route_distance(full_route, distances)

        # Format route for display
        route_str = ' -> '.join(full_route) + ' -> ' + start_city
        print(f"{route_str}: {distance} km")

        # Update best route if this one is shorter
        if distance < best_distance:
            best_distance = distance
            best_route = full_route

    return best_route, best_distance

# Solve the problem
print("=" * 50)
print("TRAVELING SALESMAN PROBLEM")
print("=" * 50)
print(f"Cities to visit: {cities}\n")

best_route, best_distance = solve_tsp_bruteforce(cities, distances)

print("\n" + "=" * 50)
print("BEST ROUTE FOUND:")
print("=" * 50)
route_display = ' → '.join(best_route) + ' → ' + best_route[0]
print(f"Route: {route_display}")
print(f"Total Distance: {best_distance} km")

## Run with python3