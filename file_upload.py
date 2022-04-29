# video tutorial
#https://www.youtube.com/watch?v=w2PwerViVbA
import pandas as pd
import streamlit as st
# import plotly_express as px

#configuration
st.set_option('deprecation.showfileUploaderEncoding', False)
#title of the app
st.title('This is streamlit')

#add slide bar
st.sidebar.subheader('Data visualization App')

#setup file upload
uploaded_df = st.sidebar.file_uploader(label='Upload your CSV or Excel File',
										type=['csv', 'xlsx'])
global df
if uploaded_df is not None:
	# print(type(uploaded_df))
	try:
		df = pd.read_csv(uploaded_df)
	except Exception as e:
		print(e)
		df = pd.read_excel(uploaded_df)
		# st.write(df.head())

st.write(df.sample(10))
