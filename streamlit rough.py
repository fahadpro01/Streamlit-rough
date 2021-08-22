from matplotlib import colors
from pandas._config.config import options
from pkg_resources import add_activation_listener
import streamlit as st
from streamlit.elements.legacy_data_frame import add_rows
from streamlit.proto.RootContainer_pb2 import SIDEBAR
from streamlit.state.session_state import Value
#Set the title
st.title("Data Science Analyser")

from PIL import Image

st.subheader('Easy to use just insert the data file ')

image=Image.open("pic.png")
st.image(image,use_column_width=True)

st.write("Writing whatever")
st.markdown("Lets see what i can write")

st.success("Mission Success")
st.info("This is the information for you")

st.warning("Be careful dude!")

st.error("Shit! error man")

st.help(range)

import numpy as np
import pandas as pd

dataframe=np.random.rand(10,10)
st.dataframe(dataframe)
st.text("-----------------"*100)

df=pd.DataFrame(np.random.rand(10,10))
st.dataframe(df.style.highlight_max(axis=1))

st.text("----"*100)

#Display chart
chart_data=pd.DataFrame(np.random.randn(20,3),columns=["a","s","d"])
st.line_chart(chart_data)
st.text("----"*100)
st.area_chart(chart_data)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=["a","s","d"])
st.bar_chart(chart_data)
st.text("----"*100)

import matplotlib.pyplot as plt
arr=np.random.normal(1,1,size=100)
plt.hist(arr)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
st.text("----"*100)

df=pd.DataFrame(np.random.randn(100,2)/[50,50]+[37.76,-122.4],columns=['lat','lon'])
st.map(df)

st.text("---------"*100)

if st.button("HEYYYY"):
    st.write("Enna da")
else:
    st.write("Ada poda")
    st.text("---------"*100)

    genre=st.radio("What your fav anime?", ("My hero","Naruto","HURRY"))
   
    st.text("-----"*100)

    #select
    options=st.selectbox("How are you?",("good","Awesome"))
    st.write("You said your day was:",options)

    st.text("-----"*100)

    age=st.slider("age?",0,75,20)
    st.write("Your age is :",age)

    values=st.slider("select the age of value",0,200,(15,80))
    st.write("Select a range:",values)


    number=st.number_input('Input Number')
    st.write("The number is:",number)
    st.text("======"*100)

    #file upload

    upload_file=st.file_uploader("Choose a CSV file",type='csv')

    if upload_file is not None:
        data=pd.read_csv(upload_file)
        st.write(data)
        st.success("File is uploaded")
    else:
            st.markdown("Please upload the file ")

            #color picker
            colors=st.sidebar.color_picker("Pick the color:",'#00f900')
            st.write("Colour:",colors)

          #add slide bar

          #st.text("-------"*100)
          #st.text("-------"*100)
        #add_selectbox= st.sidebar.selectbox("what?",("you are hero"))

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

import time

my_bar=st.progress(0)
for percent_complete in range(100): 
 time.sleep(0.1)
 my_bar.progress(percent_complete*1)

 with st.spinner("wait"):
     time.sleep(2)
     st.success("Mission Completed")
st.balloons()









