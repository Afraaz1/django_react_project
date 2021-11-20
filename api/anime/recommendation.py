#libraries to read csv files and do data analysis
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


#loading data
anime_clean = r'..\input\anime_cleaned.csv'

#storing data
animeData = pd.read_csv(anime_clean)

#Number of colums and rows 
animeData.shape

#List of genres that will be tracked for this engine
columns = ['genre', 'studio']

print(type(animeData['studio'][2]))

#Combine important data together
def getFeatures(data):
    features = []
    for i in range(0, data.shape[0]):
        features.append(f"{data['genre'][i]}{data['studio'][i]}")

    return features

animeData['features'] = getFeatures(animeData)
animeData.head(3)

#Converting features into token counts
cm = CountVectorizer().fit_transform(animeData['features'])
cs = cosine_similarity(cm)
cs.shape

#Looking up shows
title = 'Bleach'
data = animeData[animeData['title'].str.match(title)]
anime_id = data['anime_id'].values[0]
print(anime_id)



#Creating a list of recommendations
totalScores = list(enumerate(cs[anime_id]))
sortedScores = sorted(totalScores, key = lambda x:x[1], reverse = True)
sortedScores = sortedScores[1:10]
print(sortedScores)

i=0
for item in sortedScores:
    anime_title = animeData[animeData.anime_id == item[0]]['title']
    print(i+1, anime_title)
    i=i+1
sortedScores = sortedScores[1:10]
print(sortedScores)


