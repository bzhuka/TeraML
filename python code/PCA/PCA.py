import numpy as np

class PCA:
    def __init__(self, X):
        '''X is sample, K is dimensions wanted'''
        self.startX = X
        self.X = self.normalizeFeatures(X)
    def reduce(self):
        '''reduces the dimension of X and returns single value decomposition of its covariance matrix'''
        sigma = np.dot(self.X.T, self.X)/self.X.shape[0]
        U, s, V = np.linalg.svd(sigma, full_matrices=True)
        return [U, s, V];
    def findThresholdK(self, threshold):
        '''reduces the dimension with a threshold'''
        U, s, V = self.reduce() #reduced first

        total = 0 #calculates total Sii sum
        for n in s:
            total += n

        for k in range(s.shape[0], -1, -1): #k is the dimension chosen
            variance = 0
            for j in range(k): #j is iterating through to get the value
                variance += s[j]
            if variance/total < threshold:
                print("Variance retained : " + str(variance/total))
                return [k+1, U]
    def normalizeFeatures(self, X):
        '''loops through the 2d columns and normalizes each column value'''
        for i in range(X.shape[1]):
            Xmean = np.mean(X[:, i])
            X[:, i] = (X[:, i] - Xmean)
            stdev = np.std(X[:, i], dtype=np.float64)
            X[:, i] = X[:, i]/ stdev
        return X
    def getZ(self, k, U):
        '''recovers the matrix with the given U'''
        Ureduce = U[:, 0:k]
        Z = np.dot(Ureduce.T, self.X.T).T #we need to transpose because it gives us k x sample
        return Z, Ureduce
    def recoverData(self, Z, Ureduced):
        return np.dot(Z,Ureduced.T)
