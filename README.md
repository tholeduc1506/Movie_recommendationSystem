# Software and Tools Requirements:
1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [Heroku Account](https://heroku.com)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

Create a new environment:
```
conda create -p venv python==3.11 -y
```

Activate your new environment:
```
conda activate [path of your new environment]
```

Intall necessary tools in requirements.txt:
```
pip install -r requirements.txt
```

Run app.py

# Content - Based Recommendation System
Content-based filtering is one popular technique of recommendation or recommender systems. The content or attributes of the things you like are referred to as "content." 

Here, the system uses your features and likes in order to recommend you with things that you might like. It uses the information provided by you over the internet and the ones they are able to gather and then they curate recommendations according to that.  

The goal behind content-based filtering is to classify products with specific keywords, learn what the customer likes, look up those terms in the database, and then recommend similar things.

This type of recommender system is hugely dependent on the inputs provided by users, some common examples included Google, Wikipedia, etc. For example, when a user searches for a group of keywords, then Google displays all the items consisting of those keywords.

## Similarity Score : 
The aim of similarity scoring is to create a function that takes a pair of objects and produces a numerical score quantifying their relatedness. For a pair of news articles, this score might be high when the content of the pair covers the same topic. A high score for two structured records of car defects could convey that the two defects originated from the same underlying root cause.

## How Cosine Similarity works?
Cosine similarity is a measurement that quantifies the similarity between two or more vectors. It’s the cosine of the angle between vectors, which are typically non-zero and within an inner product space. 
Cosine similarity is described mathematically as the division between the dot product of vectors and the product of the Euclidean norms or magnitude of each vector.

  ![image](https://github.com/tholeduc1506/Movie_recommendationSystem/blob/f08f9887a77504673f5f8969068209adb8a73a8c/static/cosine_similarity.png)

# Movie Recommendation System:
This is a movie recommender system built with Python. I've used IMDB 5000 Movie Dataset to built this.
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

## Data Preprocessing:
I created a 'tag' column which includes information regarding Overview, genres, keywords, cast and crew of each movie. This 'tag' column plays as 'content-based vector' of the movies. After data preprocessing, the final_data table includes movie_id, title and tag column.


  ![image](https://github.com/tholeduc1506/Movie_recommendationSystem/blob/c6242f1762511705e23b68f0a239efb474aec838/static/datapreprocessing.PNG)


## For app.py, home.html:
For Cinnamon checker: I tried to build some functions to output movie list that callable in 'var films' in 'home.html', but it does not work. Then, I had to make a long list of movies in 'var films'. Please give me advice to solve this problem.


  ![image](https://github.com/tholeduc1506/Movie_recommendationSystem/blob/31b97113c16fa297d735787a368cc98875ef5fff/static/MovieList.PNG)


I am a 5-year civil engineer and have no experience in frontend UI, I am just able to build a simple web app like this.

Deployed app: https://tldmovierecommendationsystem.herokuapp.com/