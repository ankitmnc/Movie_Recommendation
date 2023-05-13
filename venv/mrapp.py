import streamlit as st
import pickle
import pandas as pd
import requests

def findp(mid):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(mid))
    data=response.json()
    return "https://image.tmdb.org/t/p/original"+data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    tmp=[]
    num=[]
    for i in movie_list:
        tmp.append(movies.iloc[i[0]].title)
        num.append(findp(movies.iloc[i[0]].id))
    return tmp,num

movies_list=pickle.load(open('mdt_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title('TOP 10 SIMILAR MOVIES')
option = st.selectbox('Select Your Movie',movies['title'].values)
if st.button('Fetch Movies'):
    tmp,num=recommend(option)

    col1, col2, col3 ,col4,col5,col6,col7,col8,col9,col10= st.columns(10)

    with col1:
        st.text(tmp[0])
        st.image(num[0])
    with col2:
        st.text(tmp[1])
        st.image(num[1])
    with col3:
        st.text(tmp[2])
        st.image(num[2])
    with col4:
        st.text(tmp[3])
        st.image(num[3])
    with col5:
        st.text(tmp[4])
        st.image(num[4])
    with col6:
        st.text(tmp[5])
        st.image(num[5])
    with col7:
        st.text(tmp[6])
        st.image(num[6])
    with col8:
        st.text(tmp[7])
        st.image(num[7])
    with col9:
        st.text(tmp[8])
        st.image(num[8])
    with col10:
        st.text(tmp[9])
        st.image(num[9])
