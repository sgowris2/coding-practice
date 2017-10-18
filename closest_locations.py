def closestLocations(totalCrates, allLocations, truckCapacity):

    def calculate_distance_squared(location):
        x = location[0]
        y = location[1]
        return x ** 2 + y ** 2

    if totalCrates is None or totalCrates <= 0 or truckCapacity is None or truckCapacity <= 0:
        return []

    if truckCapacity >= totalCrates:
        return allLocations

    if len(allLocations) != totalCrates:
        print('Error: Number of crates and crate locations don\'t match.')
        return []

    # Clean up any locations that are invalid.
    allLocations = [x for x in allLocations
                    if x is not None and
                    len(x) == 2]

    distances = {calculate_distance_squared(location): location for location in allLocations}

    return distances


if __name__ == '__main__':

    closestLocations(3, [[1, -3], [1, 2], [3, 4]], 1)
