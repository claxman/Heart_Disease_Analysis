import  streamlit as st
import pickle
import time
from PIL import Image


st.title("Predict Heart Disease")
image = Image.open('asset.jpg')
st.image(image,use_column_width=True)

choice = st.radio("Choose an option",("Try with your own data", "Check out an example"))
    
if choice == "Try with your own data":
    st.text("Please Enter the Following Info to Get the Result:")
    model = pickle.load(open('./LogisticRegression.pkl','rb'))


    age = st.text_input("Enter your Age :")

    sex = st.selectbox('Gender :',["Male","Female"])
    if sex == "Male":
        sex = 1
    else:
        sex = 0

    cp = st.selectbox("Chest Pain Type :",["Typical Angina","Atypical Angina","Non-Anginal Pain","Asymptomatic"])
    if cp == "Typical Angina":
        cp = 0
    elif cp == "Atypical Angina":
        cp = 1
    elif cp == "Non-Anginal Pain":
        cp = 2
    else:
        cp = 3

    trestbps = st.text_input(label="Resting Blood Pressure (in mm Hg on admission to the hospital) :")

    chol = st.text_input(label="Serum Cholestoral in mg/dl :")

    fbs = st.selectbox("Is Fasting Blood Sugar > 120 mg/dl :",["True","False"])
    if fbs == "True":fbs = 1
    else:fbs = 0

    restecg  = st.selectbox('Resting Electrocardiographic Results :',["Normal","Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)","Showing probable or definite left ventricular hypertrophy by Estes' criteria"])
    if restecg == "Normal":restecg = 0
    elif restecg == "Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV":
        restecg = 1
    else:restecg = 2

    thalach = st.text_input(label="Maximum Heart Rate Achieved :",)

    exang = st.selectbox('Exercise Included Angina :',["Yes","No"])
    if exang == "Yes":exang = 1
    else:exang = 0

    oldpeak  = st.text_input(label="ST Depression Induced By Exercise Relative To Rest :")

    slope = st.selectbox('The Slope of the Peak Exercise ST Segment :',["Upsloping","Flat","Downsloping"])
    if slope == "Upsloping": slope = 0
    elif slope == "Flat": slope = 1
    else: slope = 2

    ca  = st.selectbox("Number of Major Vessels (0-3) Colored By Flourosopy :",["0","1","2","3"])

    thal = st.selectbox("Thal (3 = normal, 6 = fixed defect, 7 = reversable defect) :",["3","6","7"],index=0)
    if thal == 6:
        thal = 1
    elif thal == 7:
        thal = 3
    else:
        thal = 2

    try:
        pred = model.predict([[int(age),int(sex),float(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])
    except:
        st.exception(ValueError("Carefully Provide All the Data"))
        
    try:
        if st.button("Check The Patient"):
            with st.spinner("Predicting the Result....."):
                time.sleep(5)
                st.header(" ")
            
            if pred == 0 :
                st.error("Patient Has a Heart Problem")
            else:
                st.success("Patient is Healthy")

    except:
        st.exception(ValueError("Carefully Provide All the Data"))



if choice == "Check out an example":
    st.text("Please Enter the Following Info to Get the Result:")
    model = pickle.load(open('./LogisticRegression.pkl','rb'))


    age = st.text_input("Enter your Age :",value=57)

    sex = st.selectbox('Gender :',["Male","Female"], index=1)
    if sex == "Male":
        sex = 1
    else:
        sex = 0

    cp = st.selectbox("Chest Pain Type :",["Typical Angina","Atypical Angina","Non-Anginal Pain","Asymptomatic"], index = 1)
    if cp == "Typical Angina":
        cp = 0
    elif cp == "Atypical Angina":
        cp = 1
    elif cp == "Non-Anginal Pain":
        cp = 2
    else:
        cp = 3

    trestbps = st.text_input(label="Resting Blood Pressure (in mm Hg on admission to the hospital) :", value=130)

    chol = st.text_input(label="Serum Cholestoral in mg/dl :",value=236)

    fbs = st.selectbox("Is Fasting Blood Sugar > 120 mg/dl :",["True","False"],index=1)
    if fbs == "True":fbs = 1
    else:fbs = 0

    restecg  = st.selectbox('Resting Electrocardiographic Results :',["Normal","Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)","Showing probable or definite left ventricular hypertrophy by Estes' criteria"])
    if restecg == "Normal":restecg = 0
    elif restecg == "Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV":
        restecg = 1
    else:restecg = 2

    thalach = st.text_input(label="Maximum Heart Rate Achieved :",value=174)

    exang = st.selectbox('Exercise Included Angina :',["Yes","No"], index=1)
    if exang == "Yes":exang = 1
    else:exang = 0

    oldpeak  = st.text_input(label="ST Depression Induced By Exercise Relative To Rest :", value=0)

    slope = st.selectbox('The Slope of the Peak Exercise ST Segment :',["Upsloping","Flat","Downsloping"], index=1)
    if slope == "Upsloping": slope = 0
    elif slope == "Flat": slope = 1
    else: slope = 2

    ca  = st.selectbox("Number of Major Vessels (0-3) Colored By Flourosopy :",["0","1","2","3"],index=1)

    thal = st.selectbox("Thal (3 = normal, 6 = fixed defect, 7 = reversable defect) :",["3","6","7"],index=0)
    if thal == 6:
        thal = 1
    elif thal == 7:
        thal = 3
    else:
        thal = 2

    try:
        pred = model.predict([[int(age),int(sex),float(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])
    except:
        st.exception(ValueError("Carefully Provide All the Data"))
        
    try:
        if st.button("Check The Patient"):
            with st.spinner("Predicting the Result....."):
                time.sleep(5)
                st.header(" ")
            
            if pred == 0 :
                st.error("Patient Has a Heart Problem")
            else:
                st.success("Patient Is Healthy")

    except:
        st.exception(ValueError("Carefully Provide All the Data"))