import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Loan Approval Prediction App

This app predicts whether the loan will be approved or not...

Data obtained from kaggle datasets(https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset/data)

""")
st.image(r'C:\Users\DELL\ACM W -Data science\Project\CIBIL-score-for-PL.webp')
st.sidebar.header('Features')

def user_input_features():
    loan_term = st.sidebar.slider('Loan Term',2,20,10)
    income_annum = st.sidebar.slider('Annual Income',200000,10000000,5000000)
    loan_amount=st.sidebar.slider('Loan amount',300000,40000000,5000000)
    credit_score=st.sidebar.slider('Credit Score',300,900,500)
    data={' loan_term':loan_term,
          ' income_annum': income_annum,
          ' loan_amount': loan_amount,
          ' cibil_score': credit_score}
    features = pd.DataFrame(data,index=[0])
    return features
input_df=user_input_features()


st.subheader('Features')

st.write(input_df)

load_rf=pickle.load(open('loanap_rf.pkl','rb'))

prediction = load_rf.predict(input_df)

st.subheader('Prediction')
loan_status = np.array(['Approved','Rejected'])
st.write(loan_status[prediction])
