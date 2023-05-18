def find_closest_points(points):
    # Parse the input points string
    parsed_points = [tuple(map(int, point.split(','))) for point in points.split(';')]

    # Find the closest points
    closest_points = []
    min_distance = float('inf')
    for i in range(len(parsed_points)):
        for j in range(i + 1, len(parsed_points)):
            distance = calculate_distance(parsed_points[i], parsed_points[j])
            if distance < min_distance:
                closest_points = [parsed_points[i], parsed_points[j]]
                min_distance = distance
    return ';'.join([','.join(map(str, point)) for point in closest_points])

def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
