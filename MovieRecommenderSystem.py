import pandas as pd
import numpy as np

df = pd.read_csv('Learning_Dataset/IMDB-Movie-Data.csv')
df['Movie_Id'] = range(0,1000)
print(df.head(5))

### Feature Tranformation

# Get a count of the number of rows/movies and columns
print(df.shape)

# Create a list of important columns for our recommendation engine
columns = ['Actors', 'Director', 'Genre', 'Title']

# Check for any missing values: null_values = False if there are no empty values
null_values = df[columns].isnull().values.any()
print(null_values)

# Create a function to combine the values of the importatnt columns into a single string (concatination of all important column values)
def get_imp_features(data):
    imp_features = []
    for i in range(0, data.shape[0]):
        imp_features.append(data['Actors'][i] +' '+ data['Director'][i] +' '+ data['Genre'][i] +' '+ data['Title'][i])

    return imp_features

# Create a column to hold the combined strings
df['important_features'] = get_imp_features(df)
print(df.head())

# Convert the text to matrix of token counts
from sklearn.feature_extraction.text import CountVectorizer
cm = CountVectorizer().fit_transform(df['important_features'])

# Get the cosine similarity matrix from the count matrix:
from sklearn.metrics.pairwise import cosine_similarity
cs = cosine_similarity(cm)
#print(cs)

# Get the name of the movie that the user likes
title = 'The Amazing Spider-Man'

# Find the movie_id
movie_id = df[df.Title == title]['Movie_Id'].values[0]

# Create a list of enumerations for the similarity scores [(movie_id, similarity score), (...)]
scores = list(enumerate(cs[movie_id]))

# Sort the score list for the greatest value to be on the top
sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
sorted_scores = sorted_scores[1:]
#print(sorted_scores)

# Create a loop to print the first 7 similar movies
a = 0
print('The seven most recommended movies to', title, 'are:\n')
for i in sorted_scores:
    movie_title = df[df.Movie_Id == i[0]]['Title'].values[0]
    print(a+1, movie_title)
    a=a+1
    if a > 6:
        break