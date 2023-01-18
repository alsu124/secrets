import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st







primaryColor="#6eb52f"
backgroundColor="#f0f0f5"
secondaryBackgroundColor="#e0e0ef"
textColor="#262730"
font="sans serif"
'# News metrics dashboard'

st.write('# ')
st.text_input('News link')

public_gsheets_url="https://docs.google.com/spreadsheets/d/1Y74Bc8H2fJvhFobbhesPESMouNpG8hRiwggsjRavg_w/edit#gid=0"

st.button("Predict")
df = pd.DataFrame({'ВПО': ['  ', '   ', '    '], 'Жертва': ['  ', '   ', '    '],'Дата': ['  ', '   ', '    '],'Страна жертвы': ['  ', '   ', '    '],'Уязвимость': ['  ', '   ', '    '],'Тип атаки': ['  ', '   ', '    '], 'Категория жертвы': ['  ', '   ', '    '],'Последствия атаки': ['  ', '   ', '    '],'APT-атака': ['  ', '   ', '    '],'Объект атаки': ['  ', '   ', '    '],'Supply chain': ['  ', '   ', '    '],'Способ доставки': ['  ', '   ', '    '],'Количество жертв': ['  ', '   ', '    ']})
st.dataframe(df)

st.button("Send analyst version")

st.button("Retrain")


