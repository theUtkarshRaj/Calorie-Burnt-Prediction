import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('trained_calorie.sav', 'rb'))

def Calorie_prediction(input_data):
    input_data = list(input_data)
    input_data[1] = 0 if input_data[1] == 'male' else 1

    # Convert to numpy array
    input_as_numpy_array = np.asarray(input_data, dtype=float)

    # Reshape the input for prediction
    input_data_reshaped = input_as_numpy_array.reshape(1, -1)

    try:
        # Make prediction
        prediction = np.round(float(loaded_model.predict(input_data_reshaped)), 2)
        return prediction
    except Exception as e:
        return str(e)

def main():
    # Giving a title
    st.title("Calorie Prediction")


    col1 , col2 ,col3 = st.columns(3)
    
    # Getting input data from user
    with col1:
     User_ID = st.text_input("Enter the User ID")
    with col2:
     Gender = st.selectbox("Gender", ["male", "female"])
    with col3:
     Age = st.text_input("Age")
    with col1:
     Height = st.text_input("Height")
    with col2:
     Weight = st.text_input("Weight")
    with col3:
     Duration = st.text_input("Duration")
    with col1:
     Heart_Rate = st.text_input("Heart Rate")
    with col2:
     Body_Temp = st.text_input("Body Temperature")

    # Code for prediction
    diagnosis = ''

    # Creating a button for prediction
    if st.button("Amount of Calorie"):
        # Check if any of the input fields are empty
        if any([User_ID == '', Age == '', Height == '', Weight == '', Duration == '', Heart_Rate == '', Body_Temp == '']):
            st.error("Please fill in all the input fields.")
        else:
            diagnosis = Calorie_prediction([User_ID, Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp])
            # Check if prediction failed
            if isinstance(diagnosis, str):
                st.error("Prediction failed. Please check your input data.")
            else:
                st.success(f"Predicted Calorie: {diagnosis} kcal")

if __name__ == '__main__':
    main()
