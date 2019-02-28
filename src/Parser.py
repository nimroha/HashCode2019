import numpy as np


def parseIn(path):
    with open(path, 'r') as fp:
        rows, cols, numCars, numRides, bonus, maxTime = fp.readline().strip().split()
        rides = []
        for line in fp:
            a, b, x, y, s, f = line.strip().split()
            rides.append({'startPoint' : (int(a), int(b)),
                          'endPoint'   : (int(x), int(y)),
                          'startTime'  : int(s),
                          'endTime'    : int(f),
                          'rideNum'    : len(rides)})

    return rides, int(rows), int(cols), int(numCars), int(numRides), int(bonus), int(maxTime)

def parseOut(path, schedule):
    with open(path, 'w') as fp:
        for car in schedule:
            fp.write('{numRides} {rideIds}\n'.format(numRides=len(car), rideIds=' '.join(str(id) for id in car)))
