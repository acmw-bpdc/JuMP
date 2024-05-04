import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.ensemble import RandomForestRegressor

st.header(':blue[STUDENT PERFORMANCE PREDICTION APP]',divider='green')


st.write(''' :blue[This app predicts the performance of a student based on various features pertaining to a student.This app finds the final grade G3 of a student.] ''')
st.write('''Data set obtained from kaggle :''')
st.write(''':blue[$https://www.kaggle.com/datasets/larsen0966/studentperformancedataset$]''')
from imageloader import render_image


render_image("image1.jpg")


st.sidebar.header(':green[User input features]',divider='blue')

def user_input_features():
        
        school= st.sidebar.selectbox('School',('GP','MS'))
        age=st.sidebar.slider('Age',15,22,18)
        G1=st.sidebar.slider('G1',3,19,9)
        G2=st.sidebar.slider('G2',0,19,9)
        Medu=st.sidebar.slider('Mother Education',0,4,2)
        Fedu=st.sidebar.slider('Father Education',0,4,2)
        traveltime=st.sidebar.slider('Traveltime',1,4,2)
        studytime=st.sidebar.slider('StudyTime',1,4,2)
        failures=st.sidebar.slider('Failures',0,3,1)
        activities=st.sidebar.slider('Activities',0,1)
        internet=st.sidebar.slider('Internet ',0,1)
        famrel=st.sidebar.slider('Familyrelation',1,5,2)
        freetime=st.sidebar.slider('freetime',1,5,2)
        health=st.sidebar.slider('Health',1,5,2)
        absences=st.sidebar.slider('absences',0,75,44)
       

        data={'school':school,'age':age,'Medu':Medu,'Fedu':Fedu,'traveltime':traveltime,'studytime':studytime,'failures':failures,'activities':activities,'internet':internet,'famrel':famrel,'freetime':freetime,'health':health,'absences':absences,'G1':G1,'G2':G2}
        features = pd.DataFrame(data,index=[0])
        return features
input_df= user_input_features()

encode= ['school']
for col in encode:
        dummy=pd.get_dummies(input_df[col],prefix=col)
        del input_df[col]
        input_df=input_df[:1]


st.subheader(':green[User input Features]',divider='blue')
st.write(input_df)


    
load_clf=pickle.load(open('Stud_rf.pkl','rb'))
prediction=load_clf.predict(input_df)


st.subheader(':green[Predicted Student Score-G3]',divider='blue')
st.write(prediction)


