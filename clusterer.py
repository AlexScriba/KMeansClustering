import random
import matplotlib.pyplot as plt
import math

# Class to hold information about any point
class Point:

    def __init__(self, data):
        self.data = data
        self.cluster = -1

    def find_nearest_cluster(self, centers):
        
        shortest = 1000000000

        for i in range(len(centers)):
            dist = math.sqrt( (centers[i][0] - self.data[0])**2 + (centers[i][1] - self.data[1])**2 )

            if dist < shortest:
                shortest = dist
                self.cluster = i
        
        return self.cluster

# Class to handle the clustering of passed in data
class Clusterer:

    # Constructor
    def __init__(self, num_centers, data):
        self.data = data
        self.num_centers = num_centers

        self.points = []

        #convert all data to points
        for i in range(len(self.data)):
            self.points.append(Point(self.data[i]))
        
        # Initialize cluster centers and cluster array
        self.centers = []
        self.clusters = []
        randoms_taken = []

        for _ in range(self.num_centers):
            self.clusters.append([])

        for _ in range(num_centers):
            
            rand = 0

            while rand in randoms_taken:
                rand = random.randint(0, len(self.data))
            
            self.centers.append(self.data[rand])
            randoms_taken.append(rand)

    # Method to loop until all centers are found only stopping when no point changed cluster
    def findClusters(self):
        while True:

            changed = False

            for cluster in self.clusters:
                cluster.clear()

            for point in self.points: 
                temp = point.cluster

                self.clusters[point.find_nearest_cluster(self.centers)].append(point)

                if(point.cluster != temp):
                    changed = True

            for i in range(self.num_centers):
                self.centers[i] = self.Find_New_Pos(self.clusters[i])

            if not changed:
                break

    #method to find the new position of a given center
    def Find_New_Pos(self, points):
        num_points = len(points)

        x = 0
        y = 0

        for point in points:
            x += point.data[0]
            y += point.data[1]

        return (x/num_points, y/num_points)

    # Method to return point array as array of tuples for printing
    def List_from_Points(self, index):
        result = []

        for point in self.clusters[index]:
            result.append(point.data)

        return result