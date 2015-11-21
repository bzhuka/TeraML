import scipy.io as load
import PCA
import matplotlib.pyplot as plt
arr = load.loadmat('data1.mat').get('X')
reduc = PCA.PCA(arr)

k, U = reduc.findThresholdK(0.54)
Z, Ureduced = reduc.getZ(k, U)
Xrecovered = reduc.recoverData(Z, Ureduced)
print(Xrecovered)
plt.plot(reduc.X[:, 0], reduc.X[:, 1], 'rs', Xrecovered[:, 0], Xrecovered[:, 1], 'b^')
plt.show()


