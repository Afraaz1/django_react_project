# %%
#libraries to read csv files and do data analysis
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def recommendAnime(title):
    
    #loading data
    anime = r'input\AnimeList.csv'

    #storing data
    animeData = pd.read_csv(anime)


    #Combine important data together
    def getFeatures(data):
        features = []
        for i in range(0, data.shape[0]):
            features.append(f"{data['genre'][i]}{data['type'][i]}")

        return features

    animeData['features'] = getFeatures(animeData)


    #Converting features into token counts
    cm = CountVectorizer().fit_transform(animeData['features'])
    cs = cosine_similarity(cm)
    cs.shape

    #Looking up shows
    data = animeData[animeData['title'].str.match(title)]
    anime_id = data['anime_id'].values[0]
    animeList = []
#Creating a list of recommendations)
    if(anime_id>14478):
        print("No suitable anime found")
    else:
        totalScores = list(enumerate(cs[anime_id]))
        sortedScores = sorted(totalScores, key = lambda x:x[1], reverse = True)
        sortedScores = sortedScores[1:30]
        i=0
        for item in sortedScores:
            anime_title = animeData[animeData.anime_id == item[0]]['title']
            if(anime_title.empty):
                next
            else:
                print(i, anime_title)
                animeList.append(anime_title)
                i=i+1
                if(i==11):
                    break
                
    return animeList
                
