import streamlit as st
import joblib
import pandas as pd

# 1. Load the saved model
# Make sure 'my_model.pkl' is in the same folder as this script!
model = joblib.load('model.pkl')

st.title(" Income Predictor AI")
st.write("Fill in the details below to check the income bracket.")

# 2. Create Inputs for your 5 columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    
    # Dropdown for Education
    education = st.selectbox("Education Level", 
        ["Bachelors", "Some-college", "11th", "HS-grad", "Masters", "Doctorate", "Assoc-acdm", "Assoc-voc"])
    
    marital_status = st.selectbox("Relationship Status", 
        ["Husband", "Wife", "Own-child", "Unmarried", "Not-in-family", "Other-relative"])

with col2:
    hours_per_week = st.number_input("Hours Worked per Week", min_value=1, max_value=100, value=40)
    
    # Net Capital (Capital Gain minus Capital Loss)
    net_capital = st.number_input("Net Capital (Gain - Loss)", value=0)

# 3. Predict Button
if st.button("Predict Income"):
    # CREATE THE DATAFRAME
    # IMPORTANT: The column names here MUST match your 'x_adults' columns exactly!
    input_data = pd.DataFrame([[age, education, relationship, hours_per_week, net_capital]], 
                                columns=['Age', 'education', 'relationship', 'hour work', 'net capital'])
    
    # 4. Show Result
    prediction = model.predict(input_data)
    
    if prediction[0] == '>50K':
        st.balloons()
        st.success("High Income: This person likely earns more than $50,000/year!")
    else:
        st.info("Standard Income: This person likely earns $50,000/year or less.")