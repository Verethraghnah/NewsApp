# Streamlit app for getting the news from the gnewsclient library
import streamlit as st
from gnewsclient import gnewsclient
import pandas as pd

# Create a title and a subheader
st.title('News App')
st.subheader('Get the latest news from the world')

# Get input from the user
new_categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
category = st.sidebar.selectbox('Select a category', new_categories)
number_of_articles = st.sidebar.slider('Number of articles', 1, 20, 5)


@st.cache
def load_data():
    client = gnewsclient.NewsClient(language='english',
                                    location='United States',
                                    topic=category,
                                    max_results=number_of_articles)
    return client.get_news()


# Load the data
data = load_data()

# show the articles
for article in data:
    st.write(article['title'])
    st.write(article['link'])
    st.write(' ')

# show the data as a table
st.subheader('Data')
df = pd.DataFrame(data)
st.write(df)
