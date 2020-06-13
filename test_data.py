import random

# Class to create test data to test the clustering algorythm
class Test_Data:

    def __init__(self, num_clusters, num_data_entries, spread, x_range, y_range):
        self.data = []
        self.centers = []

        for _ in range(num_clusters):
            self.centers.append((random.randrange(0, x_range), random.randrange(0, y_range)))

        for cluster in self.centers:
            for _ in range(num_data_entries):
                self.data.append((cluster[0] + random.randrange(0, spread) - spread/2, cluster[1] + random.randrange(0, spread) - spread/2))
            