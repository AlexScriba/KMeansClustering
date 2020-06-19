import random
import math
import matplotlib.pyplot as plt
import main
from numpy.random import choice

# Function to determine the euclidian distance between two points
def Distance(point_a, point_b):
    return math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)


# Class to hold information about any point
class Point:

    # Constructor
    def __init__(self, data):
        self.data = data
        self.cluster = -1

    # Finds nearest center
    def find_nearest_cluster(self, centers):
        
        shortest = math.inf

        for i in range(len(centers)):
            dist = Distance(centers[i], self.data)

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
        self.clusters = []

        self.select_centroids()

        for _ in range(self.num_centers):
            self.clusters.append([])

    # Class to choose initial centers using k means ++ method
    def select_centroids(self):
        
        self.centers = []
        probabilities = [1]*len(self.data)

        for i in range(self.num_centers):
                        
            self.centers.append(choice(self.points, 1, probabilities)[0].data)

            for i in range(len(self.points)):
                probabilities[i] = Distance(self.centers[self.points[i].find_nearest_cluster(self.centers)], self.points[i].data)**2


    # Method to loop until all centers are found only stopping when no point changed cluster
    def findClusters(self):
        
        counter = 0

        for point in self.points: point.cluster = -1
        
        while True:

            changed = False
            counter += 1

            for cluster in self.clusters:
                cluster.clear()

            for point in self.points: 
                temp = point.cluster

                self.clusters[point.find_nearest_cluster(self.centers)].append(point)

                if(point.cluster != temp):
                    changed = True

            for i in range(self.num_centers):
                self.centers[i] = self.Find_New_Pos(i)

            if not changed:
                print(counter)
                break

    # Method to find the new position of a given center
    def Find_New_Pos(self, index):

        points = self.clusters[index]
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

    # Method to display the clusters after clustering
    def display_clusters(self, colours = None):

        if colours == None:
            colours = [
                'lightblue',
                'green',
                'purple',
                'yellow',
                'grey',
                'black',
                'blue',
                'pink'
            ]            

        for i in range(self.num_centers):

            if len(self.List_from_Points(i)) != 0:
                plt.scatter(*zip(*self.List_from_Points(i)), c = colours[i])

        plt.scatter(*zip(*self.centers), c = 'red')

        plt.show()



if __name__ == "__main__":
    main.main_method()


# IDEAS

# https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/
# https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/?utm_source=blog&utm_medium=comprehensive-guide-k-means-clustering#LeaderBoard - hackathon

# Inertia = sum of intra cluster distance - keep going until minimized
# Dunn index = min(inter cluster distance)/max(intra cluster distance) - keep going until minimized

# get dataset from site