from test_data import Test_Data
import clusterer as cl
import matplotlib.pyplot as plt

def main_method():
    #variables for easy testing
    num_clusters = 5
    num_data_entries = 25
    spread = 400
    x_range = 1000
    y_range = 1000
    
    # Create test data
    # num_clusters, num_data_entries, spread, x_range, y_range
    tdata = Test_Data(num_clusters, num_data_entries, spread, x_range, y_range)
    data = tdata.data

    # Show initial data unclustered
    plt.scatter(*zip(*data))
    plt.show()

    # Cluster Data
    cluster = cl.Clusterer(num_clusters, data)
    cluster.findClusters()

    # Display clustered data
    cluster.display_clusters()



if __name__ == "__main__":
    main_method()