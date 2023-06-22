"""

"""
#** 1) Building a simple neural network
# import numpy as np


# class NeuralNetwork:
#     def __init__(self):
#         ## Initialize weights for the hidden and output layers
#         self.hidden_weights = np.random.rand(3, 4)
#         self.output_weights = np.random.rand(4, 2)


#     def sigmoid(self, x):
#         return 1 / (1 + np.exp(-x))


#     def forward_propagation(self, inputs):
#         ## Perform forward propagation through the network
#         hidden_layer_activation = self.sigmoid(np.dot(inputs, self.hidden_weights))
#         output_layer_activation = self.sigmoid(np.dot(hidden_layer_activation, self.output_weights))
#         return output_layer_activation

# ## Test the NeuralNetwork class
# nn = NeuralNetwork()
# inputs = np.array([1, 2, 3])
# outputs = nn.forward_propagation(inputs)
# print(outputs)

#** 2) Implementing K-Means clustering
# import numpy as np


# def kmeans_clustering(data, k, max_iterations=100):
#     ## Randomly initialize k cluster centroids
#     centroids = data[np.random.choice(len(data), k, replace=False)]
    
#     for _ in range(max_iterations):
#         ## Assign each data point to the nearest centroid
#         labels = np.argmin(np.linalg.norm(data[:, np.newaxis] - centroids, axis=-1), axis=-1)
#         ## Update centroids
#         new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
#         ## Check for convergence
#         if np.all(centroids == new_centroids):
#             break
        
#         centroids = new_centroids
    
#     return centroids

# ## Test kmeans_clustering function
# data = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
# centroids = kmeans_clustering(data, k=2)
# print(centroids)

#** 3) Implementing a decision tree classifier
