import numpy as np
from sklearn.cluster import KMeans
from time import time
import accuracy
#import mlpy
import random
import math


def euclidian_k_means(data, clusters, metric):
    t0 = time()
    model = KMeans(init='k-means++', n_clusters=clusters, n_init=5)
    model.fit(data)
    t1 = time()
    return ('Kmeans', model.labels_, clusters, accuracy.getAccuracy(data,model.labels_,len(data),'euclidean'),t1-t0)


def LB_Keogh(s1,s2,r):
    LB_sum=0
    for ind,i in enumerate(s1):
 
        lower_bound=min(s2[(ind-r if ind-r>=0 else 0):(ind+r)])
        upper_bound=max(s2[(ind-r if ind-r>=0 else 0):(ind+r)])
 
        if i>upper_bound:
            LB_sum=LB_sum+(i-upper_bound)**2
        elif i<lower_bound:
            LB_sum=LB_sum+(i-lower_bound)**2
 
    return math.sqrt(LB_sum)


# def dtw_k_means(data,num_clust,metric):
#     t0 = time()
#     centroids=random.sample(data,num_clust)
#     counter=0
#     for n in range(50):
#         counter+=1
#         #print counter
#         assignments={}
#         #assign data points to clusters
#         for ind,i in enumerate(data):
#             min_dist=float('inf')
#             closest_clust=None
#             for c_ind,j in enumerate(centroids):
#                 if LB_Keogh(i,j,5)<min_dist:
#                     cur_dist=mlpy.dtw_std(i,j,dist_only=True)
#                     if cur_dist<min_dist:
#                         min_dist=cur_dist
#                         closest_clust=c_ind
#             if closest_clust in assignments:
#                 assignments[closest_clust].append(ind)
#             else:
#                 assignments[closest_clust]=[]
#  
#         #recalculate centroids of clusters
#         for key in assignments:
#             clust_sum=0
#             for k in assignments[key]:
#                 clust_sum=clust_sum+data[k]
#             centroids[key]=[m/len(assignments[key]) for m in clust_sum]
# 
#     labels = [0] * len(data)
#     for key in assignments:
#     	for value in assignments[key]:
#     		labels[value] = key
# 
#     t1 = time()
# 
#     labels = np.array(labels)
#     return ('Kmeans DTW', len(assignments.keys()), accuracy.getAccuracy(data,labels,len(data),'euclidean'),t1-t0)
