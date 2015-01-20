import sklearn.metrics as metrics


def getSilhoutteScore(data,labels,sampleSize,metric):
	return  metrics.silhouette_score(data, labels,sample_size=len(data),metric='cosine')


def getAccuracy(data,labels,sampleSize,metric):
	return getSilhoutteScore(data,labels,sampleSize,metric)