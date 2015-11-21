import numpy as np
import sys
class KMean:
    def __init__(self, X):
        self.X = X
    def initCentroids(self, K):
        '''randomly shuffles the set of points and chooses the first K for centroids'''
        np.random.shuffle(self.X)
        return self.X[0:K]
    def findClosestCentroid(self, centroids):
        '''finds the closest centroids'''
        centroidGroups = {}
        for n in range(self.X.shape[0]):
            x = self.X[n]
            minDist = sys.maxsize
            index = 0
            for i,c in enumerate(centroids):
                if self.dist(x, c) < minDist:
                    minDist = self.dist(x, c)
                    index = i
            if index in centroidGroups:
                centroidGroups[index] = np.vstack([centroidGroups[index], x])
            else:
                centroidGroups[index] = x
        return centroidGroups

    def dist(self, X, Y):
        '''standard distance formula'''
        dist = (Y-X)**2
        return np.sum(dist)
    def evolveCluster(self, threshold, maxIter, K):
        '''evolving cluster per threshold/iteration'''
        centroids = self.initCentroids(K)
        sumDist = threshold+1 #just to make it bigger for now.
        cGroup = {}
        while maxIter != 0 and sumDist > threshold:
            sumDist = 0
            cGroup = self.findClosestCentroid(centroids)
            for i in cGroup: #finding the avg of each centroid
                arr = cGroup[i]
                p = np.mean(arr, axis=0)
                sumDist += self.dist(p, centroids[i])
                centroids[i] = p #assign the new centroid
            maxIter-= 1
        if sumDist < threshold:
            print("Cluster ended with a threshold distance of sumDist")
        else:
            print("Cluster ended with finishing iterations")

        return [centroids, cGroup]
