"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home Page", "Solution Overview", "EDA", "Recommender System","About the company"]
    st.sidebar.image('aqw.jpeg', width =150)
    st.sidebar.title("JM1 Movie Recommender®")
    st.sidebar.title("Menu") 
    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('azs.jpg',use_column_width=True)
        # Header contents
        #st.write('# Movie Recommender Engine')
        #st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        #st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------

     
    
    st.sidebar.subheader("Cinema should make you forget you are sitting in a theater.~Roman Polanski") 
    st.sidebar.title("                  ")
    st.sidebar.title("                  ")
    st.sidebar.title("                  ")

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("To attain best algorithms we use the following logic")
        st.image ('q4.png')
        st.image ('q2.png')
        st.image ('q3.png')
        st.image ('q1.png')
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    # Building out the EDA page
    if page_selection == "EDA":
        st.title("Flex AI Movies EDA")
        #st.subheader("Movie EDA") 
        st.image('edda.jpg', width=350) 
        st.subheader ('scroll below to view the different EDA images and diagrams')    
        with st.expander("Expand to see Word cloud"):
            st.subheader("word vloud for movie actors and actress")
            st.image('MV5.jpg')
        with st.expander("Expand to see Worst rated movies"):  
            st.subheader("Worst rated movies")
            st.image('MV6.jpg') 
        with st.expander("Expand to see Most rated movies"):
            st.subheader("most rated movies")
            st.image('MV3.jpg') 
        with st.expander("Expand to see chronology of rating per year"):
            st.subheader("rating years and scores")
            st.image('MV7.jpg')       
       
        
        
    # Building out the "Information" page
    if page_selection == "Home Page":
        st.image('v2.jpg', width=500)
        #from PIL import Image        
        #col1, col2 = st.columns(2)
        #with col1:
         #   st.image('picc.jpg', width =265)
        #with col2:
         #   st.image('picc.jpg', width =265)
        st.header(' Welcome to Flex AI')
        st.subheader("Mission")
        st.info("To Provide an accurate and robust solution to individuals so as to optimise choices surrounding the content they engage with on a daily basis, hence generating platform affinity for the streaming services which best facilitates their audience's viewing.")
        st.subheader("Vision Statement")
        st.info("To construct a recommendation algorithm based on content or collaborative filtering, capable of accurately predicting how a user will rate a movie they have not yet viewed, based on their historical preferences.")      
        #st.subheader("Confusion Matrix of the Logistric Regression Model")
        #st.image('cf.jpg')
        #st.subheader("Bar Graph showing the size of the individual sentiments")
        #st.image("bars.jpg")
        #st.subheader("Raw Twitter data and label")
        #if st.checkbox('Show raw data'): # data is hidden if box is unchecked
         #   st.write(raw[['sentiment', 'message']]) # will write the df to the page
               
    # Building our company's profile page
    if page_selection == "About the company":
        st.title("Company's profile") 
        #st.image('aqw.jpeg', width =150)
        #st.subheader("Welcome to ZF3 company")
        st.info("Welcome to JM1 Movie company. The company was founded in July 2022 by the following pioneers")
        # You can read a markdown file from supporting resources folder        
#Display Images side by side        
        from PIL import Image        
        col1, col2 = st.columns(2)
        with col1:
            st.header("Yinka Akindele")
            st.subheader("Technical Operations")             
            st.image('yinka_akindele.jpg', width =245)
            with st.expander("Expand to see Yinka Akindele's profile"): 
                st.info("Yinka Akindele is very passionate about AI/ML, he is also skilled and qualified in  Electrical/Electronics Design and Simulation. Reach him at akindeleyinka1005@gmail.com")
           
        with col2:
            st.header("Michael Okereafor")
            st.subheader("Technical Operations")             
            st.image('Michael Okereafor.jpg', width =220)  
            with st.expander("Expand to see Michael Okereafor's profile"): 
                st.info("Michael Okereafor is passionate about Power BI, SQL, Machine Learning and Neural Networks, he also has great skills and experience in Computer Engineering and Marketing. Contact him through mikel.okereafor@gmail.com")
                
        col3, col4 = st.columns(2)        
        with col3:
            st.header("Raheemat Adetunji")
            st.subheader("movie expert")            
            st.image('Raheemat Adetunji.jpg', width=235) 
            with st.expander("Expand to see Raheemat Adetunji's profile"): 
                st.info("Raheemat Adetunji is passionate, skilled and experienced in Power Bi, SQL, and Machine Learning, she aso has a great interest in Github , EC2 and web clouding. Contact her at icontola@gmail.com")
           
        with col4:
            st.header("Ayoola Solanke")
            st.subheader("Technical Operations")             
            st.image('Ayo.jpeg', width =235)
            with st.expander("Expand to see Ayoola Solanke's profile"): 
                st.info("Ayoola Solanke is passionate about Solution Architect, She is a DevOPS and a Data scientist. Reach her at Ayoslanky@gmail.com.")
            
        col5, col6 = st.columns(2)             
        with col5:
            st.header("Ifeanyi Okeke")
            st.subheader("Technical Operations")             
            st.image('Ifeanyi Okek.jpg', width =265)  
            with st.expander("Expand to see Ifeanyi Okeke's profile"): 
                st.info("Okeke Ifeanyi is passionate about Data Analytics, He also has skills in Machine learning , Process engineering, Design and control. Reach him at johnifeanyi229@gmail.com")            
              
        with col6:           
            st.header("Victor Meleka")
            st.subheader("Technical Operations")             
            st.image('Victor Meleka.jpg', width =265)
            with st.expander("Expand to see Victor Meleka's profile"): 
                st.info("Victor Meleka is passionate abouth Python, sql, machine learning modelling and streamlit, he is also skilled in Control and Instrumentation Engineering. Contact him at vicmeleka@gmail.com")
            
        #st.subheader("More information")
        #if st.checkbox('Show contact information'): # data is hidden if box is unchecked
         #   st.info("icontola@gmail.com, vicmeleka@gmail.com")
            
        #with st.expander("Expand to see Company's video profile"):       
         #   video_file = open('Kinini.mp4', 'rb')
          #  video_bytes = video_file.read()
           # st.video(video_bytes)            
             
            #st.success("Text Categorized as: {}".format(prediction))
        

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
