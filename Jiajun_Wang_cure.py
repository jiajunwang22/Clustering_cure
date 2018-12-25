import numpy as np
import sys
import datetime

def comparator(x, y):
    if x[0] < y[0]:
        return -1
    if x[0] == y[0]:
        if x[1] < y[1]:
            return -1
        if x[1] > y[1]:
            return 1
        return 0
    return 1
samplefile = "sample_data.txt"
fullfile = "full_data.txt"

ratio = 0.2
list = []
n = 0
sum = 0
k = 3
start = datetime.datetime.now()
#hierachy clustering
with open(samplefile, "r") as file:
    lines = file.readlines()
    for line in lines:
        value = line.strip().split(",")
        list.append([[float(value[0]),float(value[1])], 1, [[float(value[0]),float(value[1])]]])
        n += 1

num = 1
while (n != 3):
    min_coordinate = None
    min_distace = sys.maxint
    num += 1
    for i in range(len(list)):
        cluster1 = list[i]
        centroid1 = np.array(cluster1[0]) / cluster1[1]
        for j in range(len(list)):
            if j > i:
                cluster2 = list[j]
                centroid2 = np.array(cluster2[0]) / cluster2[1]

                distance = (centroid2 - centroid1) ** 2
                if np.sum(distance) < min_distace:
                    min_coordinate = [i, j]
                    min_distace = np.sum(distance)

    cor1 = list[min_coordinate[0]]
    cor2 = list[min_coordinate[1]]
    new_cluster = [np.ndarray.tolist(np.array(cor1[0]) + np.array(cor2[0])), cor1[1] + cor2[1], cor1[2] + cor2[2]]
    list.remove(cor1)
    list.remove(cor2)
    list.append(new_cluster)

    n -= 1

centroid = []
# find representatives and calculate centroids
id = 0
re = []
for cluster in list:

    sortedcluster = sorted(cluster[2], cmp = comparator)
    repre = [sortedcluster[0]]
    iter = 0
    while (iter < n):
        iter += 1
        candi = None
        min_distace = sys.maxint
        if len(repre) == 1:
            center = np.array(repre)
        else:
            center = reduce(np.add, np.array(repre)) / len(repre)
        for coor in sortedcluster:
            if coor not in repre:
                dis = np.sum((center - np.array(coor)) ** 2)
                if dis < min_distace:
                    min_distace = dis
                    candi = coor
        repre.append(candi)
    clustercentroid = reduce(np.add, np.array(cluster[2])) / len(cluster[2])
    centroid.append(clustercentroid)
    l = []
    for representative in repre:
        representative = np.ndarray.tolist(np.array(representative) + ratio * (clustercentroid - np.array(representative)))
        l.append(representative)
    re.append(l)

# CURE
with open(fullfile, "r") as file:
    lines = file.readlines()
    points =  map(lambda line: [float(x) for x in line.strip().split(",")],lines)
    for point in points:
        min_dis = sys.maxint
        indexcluster = 0
        for i in range(len(re)):
            cluster = re[i]
            # print "no:", i
            for r in range(len(cluster)):
                representative = cluster[r]
                dis = np.sum((np.array(representative) - np.array(point)) ** 2)
                if dis < min_dis:
                    min_dis = dis
                    indexcluster = i

        list[i][2].append(point)


for x in range(len(list)):
    print list[x][2]


