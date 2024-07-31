# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1

print(our_routes.intersection(competitor_routes))

# 2

print(our_routes.difference(competitor_routes))

# 3

print(our_routes.symmetric_difference(competitor_routes))