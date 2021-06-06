import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('white')

column_name = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names= column_name)
print(df.head())

movie_titles = pd.read_csv('Movie_Id_Titles')

# Merging the two datasets together
df = pd.merge(df, movie_titles, on='item_id')

### Exploratory Data Analysis (EDA)

# Let's explore the data and look at some of the best rated movies

# We create a new dataframe with average rating and number of ratings: Sorted from highest to lowest rating
df_group1 = df.groupby('title')['rating'].mean().sort_values(ascending=False)

df_group2 = df.groupby('title')['rating'].count().sort_values(ascending=False)

# Creating a dataframe with the mean rating values and number of ratings:
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())

ratings['Total rating count'] = pd.DataFrame(df.groupby('title')['rating'].count())

plt.figure(figsize=(10,4))
plt.title('Total Number of Ratings')
plt.hist(ratings['Total rating count'], bins=70)

plt.figure(figsize=(10,4))
plt.title('Movie Ratings Vs Number of People')
plt.hist(ratings['rating'], bins=70)

#plt.figure(figsize=(10,10))
sns.jointplot(x='rating', y='Total rating count', data=ratings, alpha=0.5)
#plt.show()

### Recommending Similar Movies:

#Creating a Pivot Table with UserId as the index axis and Movie title as another axis.
#Each cell consists of the rating the user gave to that movie.
moviemat = df.pivot_table(index='user_id', columns='title', values='rating')
print(moviemat.head())

print(ratings.sort_values('Total rating count', ascending=False).head())

# We now grab the user ratings for two movies
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

# We can the use corrwith() method to get correlations between two panda series
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

#Let us clean this by NAN values and using a DataFrame instead of a series:
corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)

corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
# Higher the correlation, the more correlated the movie is and thereby we recommend the highest correlated movies

# Sorting wrt highest correlation.
corr_starwars.sort_values('Correlation', ascending=False)

# We will take only the movies that have been rated by more than 100 users:
# For this, we will first add the Total rating count column to our dataframe and then sort them
corr_starwars = corr_starwars.join(ratings['Total rating count'])
corr_starwars = corr_starwars[corr_starwars['Total rating count']>100].sort_values('Correlation', ascending=False)

corr_liarliar = corr_liarliar.join(ratings['Total rating count'])
corr_liarliar = corr_liarliar[corr_liarliar['Total rating count']>100].sort_values('Correlation', ascending=False)

print(corr_starwars.head())
print(corr_liarliar.head())

plt.show()
