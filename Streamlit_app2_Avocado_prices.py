
import streamlit as st
import pandas as pd
import plotly.express as px

st.write("check out this [link](https://www.justintodata.com/streamlit-python-tutorial/)")

st.write("check out this, this is [all the streamlit elements](https://docs.streamlit.io/library/api-reference)")


st.write('# Avocado Prices dashboard')



st.write('# Avocado Prices dashboard')  #st.title('Avocado Prices dashboard')
st.markdown('''
This is a dashboard showing the *average prices* of different types of :avocado:  
Data source: [Kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
''')

st.header('Summary statistics')

avocado = pd.read_csv('avocado-updated-2020.csv')
st.write(avocado)
avocado_stats = avocado.groupby('type')['average_price'].mean()
st.dataframe(avocado_stats)


st.header('Line chart by geographies')
line_fig = px.line(avocado[avocado['geography'] == 'Los Angeles'],
                   x='date', y='average_price',
                   color='type',
                   title='Avocado Prices in Los Angeles')
st.plotly_chart(line_fig)