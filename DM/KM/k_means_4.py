import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

style.use('ggplot')


class K_Means:
    def __init__(self, k=3, tolerance=0.0001, max_iterations=500):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def fit(self, data):

        self.centroids = {}

        # initialize the centroids, the first 'k' elements in the
        # dataset will be our initial centroids
        for i in range(self.k):
            self.centroids[i] = data[i]

        # begin iterations
        for i in range(self.max_iterations):
            self.classes = {}
            for i in range(self.k):
                self.classes[i] = []

            # Finding the L2 distance between the point and cluster
            # choose the nearest centroid
            for features in data:
                distances = [
                    np.linalg.norm(features - self.centroids[centroid])
                    for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classes[classification].append(features)

            previous = dict(self.centroids)

            # Re-calculate the centroids
            for classification in self.classes:
                self.centroids[classification] = np.average(
                    self.classes[classification], axis=0)

            is_optimal = True

            for centroid in self.centroids:

                original_centroid = previous[centroid]
                curr = self.centroids[centroid]
                error = np.sum((curr - original_centroid) / original_centroid * 100.0)

                if error > self.tolerance:
                    is_optimal = False

            # Break out if the centroids don't change their positions much
            if is_optimal:
                break


if __name__ == "__main__":
    df = pd.read_csv('dataKMeans.csv')
    k = 3
    X = df.values
    km = K_Means(k)
    km.fit(X)

    # Two visualize via 2-d plots, we'll have to select only 2 dimensions,
    # the distinction b/w cluster might not be clear in 2 dimensions (
    # because we're missing the "Shoe size" dimension while visualizing)
    df = df[['Height', 'Age']]

    # Plotting starts here
    colors = 10 * ["r", "g", "c", "b", "k"]

    for centroid in km.centroids:
        plt.scatter(km.centroids[centroid][0],
                    km.centroids[centroid][1],
                    s=130,
                    marker="x")

    for classification in km.classes:
        color = colors[classification]
        for features in km.classes[classification]:
            plt.scatter(features[0],
                        features[1],
                        color=color,
                        s=30)
    plt.show()
