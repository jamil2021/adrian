import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371000 * c  # Radius of Earth in meters
    return distance

def bearing(lat1, lon1, lat2, lon2):
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Calculate bearing
    dlon = lon2 - lon1
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    initial_bearing = math.atan2(y, x)
    bearing_degrees = math.degrees(initial_bearing)
    compass_bearing = (bearing_degrees + 360) % 360
    return compass_bearing

def elevation(lat1, lon1, alt1, lat2, lon2, alt2):
    # Calculate elevation angle
    distance = haversine(lat1, lon1, lat2, lon2)
    elevation_angle = math.atan2(alt2 - alt1, distance)
    elevation_degrees = math.degrees(elevation_angle)
    return elevation_degrees

def slant_range(lat1, lon1, alt1, lat2, lon2, alt2):
    # Calculate slant range distance
    ground_distance = haversine(lat1, lon1, lat2, lon2)
    altitude_difference = alt2 - alt1
    slant_range_distance = math.sqrt(ground_distance**2 + altitude_difference**2)
    return slant_range_distance

# Input data
lat1 = float(input("Location 1 - Enter Lat: "))
lon1 = float(input("Location 1 - Enter Long: "))
alt1 = float(input("Location 1 - Enter Elevation in Meters: "))
lat2 = float(input("Location 2 - Enter Lat: "))
lon2 = float(input("Location 2 - Enter Long: "))
alt2 = float(input("Location 2 - Enter Elevation in Meters: "))

# Calculations
ground_distance = haversine(lat1, lon1, lat2, lon2)
bearing_degrees = bearing(lat1, lon1, lat2, lon2)
elevation_degrees = elevation(lat1, lon1, alt1, lat2, lon2, alt2)
slant_range_distance = slant_range(lat1, lon1, alt1, lat2, lon2, alt2)

# Output
print("\nFrom Location 1 to Location 2:")
print(f"Bearing Degrees (True North): {bearing_degrees:.4f}")
print(f"Elevation in Degrees: {elevation_degrees:.4f}")
print(f"Down Range in Meters: {ground_distance:.0f}")
print(f"Slant Range in Meters: {slant_range_distance:.0f}")
