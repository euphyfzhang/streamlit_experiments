import streamlit as st
import snowflake.connector
import pandas as pd
import requests

### Snowflake connection
sn_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
sn_cur = sn_cnx.cursor()

#total count
sn_cur.execute("SELECT COUNT(1) FROM RAW.CHICAGO_CRIMES;")
total_cnt = sn_cur.fetchall()

#Group by 


### Set the title/header
st.set_page_config(layout='wide')
st.header('Welcome to my streamlit/snowflake experiments.')
st.subheader('Hope you enjoy my learning journey!')

## Layout
col1, col2, col3, col4 = st.columns((1,2,1,1))
with col1:
	st.write('Dataset general information')
	st.write(f'there are {total_cnt[0][0][0]} rows in the table!')
	
with col2:
	st.write('Bar chart group by primary_type')
	sn_cur.execute("select * FROM RAW.SUMMARY_CRIME_COUNTS;")
	ptg = sn_cur.fetchall()
	#st.write(ptg.columns)
	st.dataframe(ptg)
	
	number = st.number_input('Insert the primary type.')
	st.write('The current number is ', number)
	
	st.button("Submit", type="primary")
	if st.button('Say hello'):
		st.write('Why hello there')
	else:
		st.write('Goodbye')

	
with col3:
	st.write('3rd column')
	
with col4:
	st.write('4th column')