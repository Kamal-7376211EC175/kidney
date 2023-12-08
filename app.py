import numpy as np
import pickle
import streamlit as st

#loading the saved model

loaded_model = pickle.load(open(r'C:\Users\kling\Desktop\ptac\ckd-main\kidney.pkl','rb'))

#creating a function for prediction

def kidney_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
      return('The person does not have ckd.')
    else:
      return('The person have ckd.')
  
def main():
    #give a title
    st.title('CKD Prediction Web App')
        						    
    #getting the input from the user
    bloodpressure = st.text_input('Blood Pressure')
    specificgravity = st.text_input('Specific Gravity')
    albumin = st.text_input('Albumin')
    sugar = st.text_input('Sugar')
    rbc=st.text_input('Red Blood Cell')
    bloodurea = st.text_input('Blood Urea')
    Serumcreatinine = st.text_input('Serum Creatinine')
    sodium = st.text_input('Sodium')
    potassium = st.text_input('Potassium')
    heamoglobin  = st.text_input('Heamoglobin')
    wbcc=st.text_input('White Blood Cell Count')
    rbcc=st.text_input('Red Blood Cell Count')
    hypertension = st.text_input('hypertension')
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = kidney_prediction([bloodpressure, specificgravity,albumin, sugar, rbc,bloodurea, Serumcreatinine, sodium,potassium,heamoglobin,wbcc,rbcc,hypertension])
    
    st.success(diagnosis)
            
if __name__ == '__main__':
    main()
    
 
