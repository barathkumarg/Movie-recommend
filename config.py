import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv("tamil_movie_dataset_2019.csv")
features = ['Name', 'WrittenBy', 'Starring', 'MusicBy', 'Cinematography', 'EditedBy']
for feature in features:
    df[feature] = df[feature].fillna('')

def combined_features(row):
    return row['Name']+" "+row['WrittenBy']+" "+row['Starring']+" "+row['MusicBy']+" "+row['Cinematography']+" "+row['EditedBy']

df["combined_features"] = df.apply(combined_features, axis =1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

def get_index_from_title(title):

        return df[df.Name == title]["index"].values[0]





def get_title_from_index(index):
    a=[]
    a.append( df[df.index == index]["Name"].values[0])
    a.append( df[df.index == index]["Director"].values[0])
    a.append(df[df.index == index]["Starring"].values[0].replace('\n',', '))
    return a
i=0


def get_movies(title):
    movie_user_likes = title
    movie_index = get_index_from_title(movie_user_likes)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

    out = []
    i = 1

    for movie in sorted_similar_movies:
        out.append(get_title_from_index(movie[0]))
        i = i + 1
        if i > 15:
            break

    return out
