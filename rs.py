import numpy as np
import scipy.optimize as spo
import scipy.io as spi
import matplotlib as mpl
import sys
import math

numEval = 0
recentCost = 0;
sysargs = sys.argv

def train(R, Y, numFeatures, numElements, numUsers):
    epsilon =10
    guess_vec = np.random.rand(numFeatures* (numElements+numUsers)) #random initialization of guess vector
    args = (R, Y, numFeatures, numElements,numUsers,epsilon)  # create args for spoptimize
    result = spo.optimize.fmin_cg(costFunction, guess_vec,fprime=gradFunction,args=args,maxiter=200,callback=cb)
    return result

def cb(Xi):
    global numEval
    global recentCost
    print('{}\r'.format("Iteration: " + format(numEval, '02')+" | Cost: "+  "{0:.5f}".format(recentCost)), end= "\r")
    numEval+=1


def costFunction(XandTheta, *args):
    global recentCost
    R, Y, numFeatures, numElements,numUsers,epsilon  = args # get helpful values

    X = np.reshape(XandTheta[:numFeatures*numElements],(numElements, numFeatures))
    theta = np.reshape(XandTheta[numFeatures*numElements:],(numUsers, numFeatures)) # unroll parameters
    cost = np.sum(np.sum(np.power((np.dot(X,np.transpose(theta)) - Y),2) * R)) / 2
    cost +=  (epsilon/2)*(np.sum(np.sum(X*X))+np.sum(np.sum(theta*theta)))
    recentCost = cost
    return cost

def gradFunction(XandTheta, *args):
    R, Y, numFeatures, numElements,numUsers,epsilon  = args # get helpful values

    X = np.reshape(XandTheta[:numFeatures*numElements],(numElements, numFeatures))
    theta = np.reshape(XandTheta[numFeatures*numElements:],(numUsers, numFeatures)) # unroll parameters

    theta_grad = np.dot(np.transpose((np.dot(X, np.transpose(theta)) - Y) * R), X) + epsilon*theta
    X_grad = np.dot((np.dot(X, np.transpose(theta)) - Y) * R, theta) + epsilon*X

    ans = np.concatenate((np.reshape(X_grad, -1) , np.reshape(theta_grad, -1))) #reroll parameters and return

    return ans

def featureNormalize(Y,R):
    Ymean = np.sum(np.transpose(Y)) / np.sum(np.transpose(R)) #compute mean
    return  Ymean

def predict(my_input):
    #load data from .mat file 
    matrices = spi.loadmat(sysargs[1])
    R = matrices.get('R')
    Y = matrices.get('Y')
    
    #testParams = spi.loadmat(sysargs[2])
    #X = testParams.get('X')
    #Theta = testParams.get('Theta')

    #append my ratings
    r_input = np.array(np.array(my_input,dtype=bool),dtype=int)
    Y = np.concatenate((my_input, Y), 1)
    R = np.concatenate((r_input, R), 1)
    
    Ymean = featureNormalize(Y,R)
    #Y = Y-Ymean.reshape((np.size(Ymean),1))

    #get useful values
    (numElements,numUsers) = np.shape(R)
    numFeatures = 10;
    
    #R = R[:numElements, :numUsers] 
    #Y = Y[:numElements, :numUsers] 
    #X = X[:numElements, :numFeatures] 
    #Theta = Theta[:numUsers, :numFeatures] 
   
    #args = (R,Y,numFeatures, numElements, numUsers, 1.5)
    #print(costFunction(np.concatenate((np.reshape(X,-1), np.reshape(Theta,-1))), R, Y,numFeatures, numElements, numUsers, 1.5 ))

    result = train(R,Y, numFeatures,numElements,numUsers)
    
    X = np.reshape(result[:numFeatures*numElements],(numElements, numFeatures))
    theta = np.reshape(result[numFeatures*numElements:],(numUsers, numFeatures)) # unroll parameters

    p = np.dot(X,np.transpose(theta))
    index_predictions = np.argsort(p[:,0] + Ymean)
    print(index_predictions[-10:])
    predictions =  np.sort(p[:,0] + Ymean)
    print(predictions[-10:])


def testCase():
    mv_ratings = np.zeros((1682,1))

    mv_ratings[0] = 4;
    mv_ratings[97] = 2;
    mv_ratings[6] = 3;
    mv_ratings[11] = 5;
    mv_ratings[53] = 4;
    mv_ratings[63] = 5;
    mv_ratings[65] = 3;
    mv_ratings[68] = 5;
    mv_ratings[182] = 4;
    mv_ratings[225] = 5;
    mv_ratings[354] = 5;
    
    predict(mv_ratings)

testCase()
