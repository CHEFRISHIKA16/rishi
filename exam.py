import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("data.csv")
x=df[[['HoursStudied']]
y=df['Examscore']
X_train,X_test,y_train,y_test=train_test_split(X, Y, test_size=0.2,randam_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
st.title("Exam Score Prediction")
st.write("Enter hours studied to predict the exam score")
hours=st.number_input("Hours studied:",min_value=0.0,step=0.1)
     if st.button("prediction score")
     precdicted_score = model.predict([[hours]])[0]
     st.success(f"predicted score:{predicted_score:2f}")
st.write("###Sample training Data")
st.dataframe(df)
                
                        
