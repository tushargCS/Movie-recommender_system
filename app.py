import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
        try:
            resp = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2d571d989169f882c545e415f3acbd21&language=en-US'.format(movie_id))
            if(resp!=None):
                data = resp.json()
                return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']
        except:
            return None

def recommend(movie):
    movies_index = movies_list[movies_list['title']==movie].index[0]
    distances = similarity[movies_index]
    similar_movies = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[0:6]

    recommend_movies = []
    top_movies_poster = []
    for i in similar_movies:
        movie_id = movies_list.iloc[i[0]].movie_id
        # fetch poster from API
        recommend_movies.append(movies_list.iloc[i[0]].title)
        top_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,top_movies_poster

movies_list = pickle.load(open('Movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which Movie would you like to watch', movies_list['title'].values
)
print(selected_movie_name)
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)

    if(names[0]!=None and posters[0]!=None):
        with col1:
            st.text(names[0])
            st.image(posters[0])
    if (names[1] != None and posters[1] != None):
        with col2:
            st.text(names[1])
            st.image(posters[1])
    if (names[2] != None and posters[2] != None):
        with col3:
            st.text(names[2])
            st.image(posters[2])
    if (names[3] != None and posters[3] != None):
        with col4:
            st.text(names[3])
            st.image(posters[3])
    if (names[4] != None and posters[4] != None):
        with col5:
            st.text(names[4])
            st.image(posters[4])

