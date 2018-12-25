# Clustering_cure
part of Data Mining HW

CURE works in two passes:
1. Pick a sample from data given, cluster it hierarchically, and determine k clusters from dendrogram. Identify n Representative points from each cluster and move them p% towards the centroid of cluster
2. Scan complete data and assign points to closest cluster by taking distance between point x and cluster C

Given with two data files – sample and full data in Euclidean space. The task is to do hierarchical clustering on the sample data and come up with k clusters (user specified). Remember in hierarchical clustering, each point begins in its own cluster, and pairs of clusters are merged as one moves up the hierarchy. Cluster distance is given by the distance of two closest points, one from each cluster. From the resulting Dendrogram, you can find the k clusters. A Naive implementation of hierarchical clustering should do given that the sample file in our case will be smaller.

This is how CURE will work step by step: 
  
	• Find initial clusters from a sample - It will take a sample of data from disk and perform hierarchical clustering on the sample - Cluster distance is given by the distance of two closest points, one from each cluster. - It then finds k initial clusters by cutting the dendrogram properly 
  
	• Finding representatives for each cluster - Each cluster is represented by n representative points where n can be user specified - Representatives are chosen by first picking a smallest coordinate point (Smallest x and smallest y in set of 2D points) in the cluster (formed by the sample), then repeatedly find other points farthest away from representative points already selected - It then moves representative p% towards the centroid of cluster, where p can be user specified.
  
	• Assign remaining data points (loaded from disk) to the closest clusters by taking distance from point x to the closest representative point in C
