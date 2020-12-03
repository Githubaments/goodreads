import streamlit as st
import pandas as pd
import plotly.express as px
import gender_guesser.detector as gender
import xmltodict
import urllib.request


key = (os.environ.get('key'))


st.set_page_config(page_title='Drink Recommender', page_icon="https://raw.githubusercontent.com/Githubaments/Images/main/favicon.ico")

user_input = st.text_input("Input your own Goodreads Profile Link")
st.write("Head to [here](https://www.goodreads.com)")

@st.cache
def get_user_data(user_id, key, v='2', shelf='read', per_page='200'):
    api_url_base = 'https://www.goodreads.com/review/list/'
    final_url = api_url_base + user_id + '.xml?key=' + key + \
        '&v=' + v + '&shelf=' + shelf + '&per_page=' + per_page
    contents = urllib.request.urlopen(final_url).read()
    return(contents)

user_input = str(user_input)
contents = get_user_data(user_id=user_id, v='2', shelf='read', per_page='200')
contents = xmltodict.parse(contents)

df = json_normalize(contents['GoodreadsResponse']['reviews']['review'])
u_books = len(df['book.id.#text'].unique())
u_authors = len(df['book.authors.author.id'].unique())
df['read_at_year'] = [i[-4:] if i != None else i for i in df['read_at']]
has_records = any(df['read_at_year'])




st.write(contents)
