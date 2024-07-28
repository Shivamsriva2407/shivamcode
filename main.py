import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
# import matplotlib.pyplot as plt
import dash as dash
import dash_html_components as html
from dash import dcc
from dash.dcc import Input
from dash.html import Output
import streamlit as st
st.set_page_config(layout='wide')

df = pd.read_csv('India.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title("India Data viz")

df.drop(columns=['Male_Literate', 'Female_Literate'], inplace=True)
primary_parameters = sorted(df.columns[6:])

selected_state = st.sidebar.selectbox('Select a state', list_of_states)
primary = st.sidebar.selectbox('Select primary Parameter', primary_parameters)
secondary = st.sidebar.selectbox('Select secondar Parameter', primary_parameters)

plot = st.sidebar.button('Plot Graph')

if plot:
    # pass
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size=primary, color=secondary, size_max=15, zoom=4,
                                mapbox_style='carto-positron',width=1200,height=800,hover_name='District name')
        st.plotly_chart(fig,use_container_width=True)
        # pass plot for india
    else:
        state_df = df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, size_max=15, zoom=4,
                                mapbox_style='carto-positron', width=1200, height=800,hover_name='District name')
        st.plotly_chart(fig, use_container_width=True)

