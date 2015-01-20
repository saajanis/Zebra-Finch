import csv
import numpy as np
import itertools


import kMeans as km
import distance



def getSongRepresentation (fileName, row):

    with open (fileName, "rb") as CSVfile:
          
        songs = csv.reader(CSVfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        returnSong = []
        
        listreturn = []
        x=1
        for song in songs:
            listintr = []
            for MFCCrow in song:
                listintr.append( np.asarray( ( MFCCrow.strip("[").strip("]").split(",") ), dtype=float) )        
            listreturn.append(listintr)
            if (x>=20):
                break;
            x=x+1
        
        
        i=1
        for song in songs:
            
            for MFCCrow in song:
                returnSong.append( np.asarray( ( MFCCrow.strip("[").strip("]").split(",") ), dtype=float) )        
            if (i>=1):
                break;
            i=i+1
        
        returnSong = np.asarray(returnSong)
        #return returnSong
        return listreturn[row-1]
        
def getIndividualAnnotations (trainingConsolidatedAnnotation, trainingSongLengths):
     
#     print len(trainingConsolidatedAnnotation)
#     print trainingSongLengths
    returnDict = []
    lengthUsedSoFar = 0
     
    for songLength in trainingSongLengths:
        returnDict.append ( trainingConsolidatedAnnotation[lengthUsedSoFar : lengthUsedSoFar+songLength] )
                  
        lengthUsedSoFar+=songLength
    
    return returnDict  



def levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n] 
        
################MAIN#####################

song_1 =  getSongRepresentation("o31_1wkpre.csv", 11) ;
song_2 =  getSongRepresentation("o40_1wkpre.csv", 1) ;
song_3 =  getSongRepresentation("r34_1wkpre.csv", 1) ;
song_4 =  getSongRepresentation("r725_1daypre.csv", 1) ;
song_5 =  getSongRepresentation("o31_1wkpre.csv", 12) ;


training = (np.concatenate( (song_1,song_2, song_3, song_4, song_5) ))
trainingSongLengths = [len(song_1), len(song_2), len(song_3), len(song_4), len(song_5)]

num_clusters = 10


# for i in xrange (2,25,1):
#         result =   km.euclidian_k_means(np.asarray(song_1), i,'euclidean')
#         
#         print result

result =   km.euclidian_k_means(np.asarray(training), num_clusters,'euclidean')
trainingConsolidatedAnnotation =  result[1]




AnnotationDict = getIndividualAnnotations (trainingConsolidatedAnnotation, trainingSongLengths)


print AnnotationDict

combinations = itertools.combinations(range(len(AnnotationDict)), 2)

for combination in combinations:
    print [i+1 for i in combination]
    print "levenshtein : " + str(distance.levenshtein(AnnotationDict[combination[0]], AnnotationDict[combination[1]]) )
    print "nlevenshtein 1: " + str(distance.nlevenshtein(AnnotationDict[combination[0]], AnnotationDict[combination[1]], method=1) )
    print "nlevenshtein 2: " + str(distance.nlevenshtein(AnnotationDict[combination[0]], AnnotationDict[combination[1]], method=2) )
    #print "hamming: " + str(distance.hamming(AnnotationDict[combination[0]], AnnotationDict[combination[1]]) )
    #print "sorensen: " + str(distance.sorensen(AnnotationDict[combination[0]], AnnotationDict[combination[1]]) )
    #print "jaccard: " + str(distance.jaccard(AnnotationDict[combination[0]], AnnotationDict[combination[1]]) )


# song_1 =  getSongRepresentation("o31_1wkpre.csv") ;
# song_2 =  getSongRepresentation("o40_1wkpre.csv") ;
# song_3 =  getSongRepresentation("r34_1wkpre.csv") ;
# song_4 =  getSongRepresentation("r725_1daypre.csv") ;
# song_5 =  getSongRepresentation("r725_1wkpre.csv") ;
    