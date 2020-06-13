from test_data import Test_Data
from clusterer import Clusterer
import matplotlib.pyplot as plt

# Create test data
tdata = Test_Data(3, 20, 200, 1000, 1000)
data = tdata.data

# Show initial data unclustered
plt.scatter(*zip(*data))
plt.show()

# Cluster Data
cluster = Clusterer(3, data)
cluster.findClusters()

# Display clustered data
plt.scatter(*zip(*cluster.List_from_Points(0)), c='blue')
plt.scatter(*zip(*cluster.List_from_Points(1)) , c='green')
plt.scatter(*zip(*cluster.List_from_Points(2)) , c='pink')
plt.scatter(*zip(*cluster.centers), c='red')
plt.show()