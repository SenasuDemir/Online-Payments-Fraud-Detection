import pandas as pd
from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import streamlit as st
import joblib

df=pd.read_csv('PS_20174392719_1491204439457_log.csv')
model = joblib.load('best_model.pkl')

preprocessor=ColumnTransformer(
    transformers=[
        ('num',StandardScaler(),['step','amount','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest']),
        ('cat',OneHotEncoder(),['type'])
    ]
)
pipeline=Pipeline(steps=[('preprocessor',preprocessor),('regressor',model)])
pipeline.fit(df[['step','amount','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest','type']],df[['isFraud']])
def price_pred(step,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,type):
    input_data=pd.DataFrame({
        'step':[step],
        'amount':[amount],
        'oldbalanceOrg':[oldbalanceOrg],
        'newbalanceOrig':[newbalanceOrig],
        'oldbalanceDest':[oldbalanceDest],
        'newbalanceDest':[newbalanceDest],
        'type':[type]
    })
    prediction=pipeline.predict(input_data)[0]
    return prediction

def main():
    st.title('Fraud Detection')
    st.write('Enter process detail and predict fraud or not')

    
    type=st.selectbox('Type',df['type'].unique())
    amount=st.number_input('Amount',int(df['amount'].min()),int(df['amount'].max()))
    oldbalanceOrg=st.number_input('oldbalanceOrg',int(df['oldbalanceOrg'].min()),int(df['oldbalanceOrg'].max()))
    newbalanceOrig=st.number_input('newbalanceOrig',int(df['newbalanceOrig'].min()),int(df['newbalanceOrig'].max()))
    oldbalanceDest=st.number_input('oldbalanceDest',int(df['oldbalanceDest'].min()),int(df['oldbalanceDest'].max()))
    newbalanceDest=st.number_input('newbalanceDest',int(df['newbalanceDest'].min()),int(df['newbalanceDest'].max()))
    step=st.number_input('step',int(df['step'].min()),int(df['step'].max()))


    if st.button('Predict'):
        prediction=price_pred(step,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,type)
        if prediction==1:
            st.write(f'The Proces is FRAUD')
        elif prediction==0:
            st.write(f'The Proces is NOT FRAUD')
        
if __name__=='__main__':
    main()
