
import re
import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

# @st.cache
def get_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    article = soup.find_all(href=re.compile("article/"))
    # print(article)

    list = []
    for el in article:
        try:
            list.append(el.contents[3].text)
            # print("-"*10)
        except:
            break        
    return list

url = 'https://www.hokkaido-np.co.jp/news/n_economy'

# streamlit for display    
st.write('''
        # 北海道新聞[経済]
        ''')

df = pd.DataFrame({'最新情報':get_data(url)})
st.dataframe(df)
