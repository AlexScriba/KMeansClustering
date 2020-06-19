from test_data import Test_Data
import clusterer as cl
import matplotlib.pyplot as plt

def main_method():
    # Create test data
    # num_clusters, num_data_entries, spread, x_range, y_range
    tdata = Test_Data(3, 25, 250, 1000, 1000)
    data = tdata.data

    # Show initial data unclustered
    plt.scatter(*zip(*data))
    plt.show()

    # Cluster Data
    cluster = cl.Clusterer(3, data)
    cluster.findClusters()

    # Display clustered data
    cluster.display_clusters(['purple', 'black', 'grey'])

if __name__ == "__main__":
    main_method()