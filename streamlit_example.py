import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")




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


