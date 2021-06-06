# Movie Recommendation System: a) Content-Based Filterning, b) Collaborative Filtering 
A Movie Recommender System to estimate the top N movies that a user is likely to watch based on:
1) **Content-Based Filtering:** Here we use the variables: Movie title, Actors, Director and Genre to make recommendations based on this
<img src="https://github.com/srikanthv0610/Movie-Recommendation-System/blob/main/plots/movie.png" width="400" height="500">

### Steps:
* Pre-processing the IMDB Movie dataset
* Create a list of important columns for our recommendation engine and concatinate them into a single string
* Convert the text to matrix of token counts and Get the cosine similarity matrix from the count matrix
* Create a list of enumerations for the chosen movie with similarity scores
* Sort for the greatest value to be on the top and recommend the movies with higher score


2) **Collaborative Filtering:** Here we find the most related movies for a target movie and make recommendations based on this
<img src="https://github.com/srikanthv0610/Movie-Recommendation-System/blob/main/plots/movie2.png" width="550" height="520">

### Steps:
* Pre-processing the rating and movie data
* Create a mapper between movie id's and movie titles
* Perform Exploratory Data Analysis (EDA)
* Create a Pivot Table with UserId as the index axis and Movie title as another axis. Each cell consists of the rating the user gave to that movie.
* Using correlation to estimate the probabilities and recommend the movies with higher correlation

## Descriptive Statistics:
We determine how many times the movies have been rated to create the count variable:

![Plot1](https://github.com/srikanthv0610/Movie-Recommendation-System/blob/main/plots/Figure_1.png)
Represents the histogram for the number of ratings

![Plot2](https://github.com/srikanthv0610/Movie-Recommendation-System/blob/main/plots/Figure_2.png)
* Here we observe that the integer rating values have taller bars compared to the floating values.
* The rating data are approximately normally distributed with a mean approximately = 3.5.  

![Plot3](https://github.com/srikanthv0610/Movie-Recommendation-System/blob/main/plots/Figure_3.png).
* The scatter plot between average ratings and number of ratings.
* We obseve a positive relation between the two variables, i.e movie with large amount of ratings have higher average ratings.

## Result:

![Plot4](https://github.com/srikanthv0610/Movie-Recommendation-System/blob/main/plots/Fig4.PNG)

![Plot5](https://github.com/srikanthv0610/Movie-Recommendation-System/blob/main/plots/Fig5.PNG)
