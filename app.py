import numpy as np
import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    suggestions = get_suggestions()
    return render_template('home.html',suggestions=suggestions)



@app.route("/recommendation")
def recommendation():
    movie = request.args.get('movie')
    r = rcmd(movie)
    movie = movie.upper()
    if type(r)==type('string'):
        return render_template('recommendation.html',movie=movie,r=r,t='s')
    else:
        return render_template('recommendation.html',movie=movie,r=r,t='l')

# Get movies' title from final_data.csv:
def get_suggestions():
    data = pd.read_csv('final_data.csv')
    return list(data['title'])
    
def create_sim_matrix():
    data = pd.read_csv('final_data.csv')
    # create a count matrix:
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['tag'])
    # create a similarity matrix:
    sim = cosine_similarity(count_matrix)
    return data,sim

def rcmd(m):
    m = m.lower()
    # check if data and sim are already assigned:
    try:
        data.head()
        sim.shape
    except:
        data, sim = create_sim_matrix()
    # check if the movie is in database:
    if m not in data['title'].unique():
        return('This movie is not in our database. Please try with another movie')
    else:
        # get the index of the movie in the dataframe:
        i = data.loc[data['title']==m].index[0]

        # fetch the row containing similarity scores of the movie
        # from similarity matrix and enumerate it:
        lst = list(enumerate(sim[i]))

        # sort this list in decreasing order based on the similarity score
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)

        # taking top 1-7 movie scores
        lst = lst[1:7]

        # make an empty list that will containg all 6 movie recommendations
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['title'][a])
        return l


if __name__ == '__main__':
    app.run(debug=True)