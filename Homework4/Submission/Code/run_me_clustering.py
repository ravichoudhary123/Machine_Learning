import numpy as np
import matplotlib.pyplot as plt
import util

#Load the data. imgs is an array of shape (N,8,8) where each 8x8 array
#corresponds to an image. imgs_vectors has shape (N,64) where each row
#corresponds to a single-long-vector respresentation of the corresponding image.
img_size = (8,8)
imgs, imgs_vectors  = util.loadDataQ1()

#You should use the data in imgs_vectors to learn a clustering model.
#This starter code uses random clusters.
K  = 5
N  = imgs_vectors.shape[0]
Zs = np.random.random_integers(1,K,N)

#The code below shows how to plot examples from clusters as an image array
for k in np.unique(Zs):
	plt.figure(k)
	if np.sum(Zs==k)>0:
  	  util.plot_img_array(imgs_vectors[Zs==k,:], img_size,grey=True)
  	plt.suptitle("Cluster Exmplars %d/%d"%(k,K))
plt.show()

#The code below shows how to compute and plot cluster centers as an image array
centers = np.zeros((len(np.unique(Zs)),64))
plt.figure(1)
i=0
for k in np.unique(Zs):
    centers[i,:] = np.mean(imgs_vectors[Zs==k,:],axis=0)
    i=i+1
util.plot_img_array(centers, img_size,grey=True)
plt.suptitle("Cluster Centers (K=%d)"%K)
plt.show()