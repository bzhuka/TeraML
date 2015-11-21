import scipy.io as load
import KMean
import matplotlib.pyplot as plt

arr = load.loadmat('ex7data2.mat').get('X')
cluster = KMean.KMean(arr)
centroid, cGroup = cluster.evolveCluster(0,1000,3)
print(centroid)

plt.plot(arr[:, 0], arr[:, 1], 'rs', centroid[:, 0], centroid[:, 1], 'b^')
ax = plt.gca()
plt.show()

plt.plot(centroid[:, 0], centroid[:, 1], 'b^')
plt.show()

