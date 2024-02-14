# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 20:08:22 2024

@author: Administrator
"""
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model paths
diabetes_prediction = pickle.load(open('diabetes_traning.sav','rb'))
heart_diseases_prediction = pickle.load(open('heart_data.sav','rb'))
parkinsons_prediction = pickle.load(open('Parkinson_data.sav','rb'))
breast_cancer_prediction = pickle.load(open('breast_cancer_data.sav','rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Health monitoring and disease prediction using ML system',
                                      ['diabetes prediction',
                                       'heart diseases prediction',
                                       'parkinsons prediction',
                                       'breast cancer prediction'],
                                       icons=['activity','heart','person','amd'],
                                       default_index=0)
if (selected=='diabetes prediction'):
     st.title('Diabetes Prediction using ML')
     col1,col2,col3=st.columns(3)
  
     with col1:
         Pregnancies = st.text_input('Number of Pregnancies')
     with col2:
         Glucose = st.text_input('Glucose level')
     with col3:
         PBloodPressure = st.text_input('BloodPressure level')
     with col1:
         SkinThickness = st.text_input('SkinThickness of Skin')
     with col2:
         Insulin = st.text_input('Insulin level')
     with col3:
         BMI = st.text_input('BMI meter')
     with col1:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction level')
     with col2:
         Age = st.text_input('Age of person')
         
         
         diab_diagnosis = ''

     if st.button('Diabetes Test Result'):
        pred_diagnosis = diabetes_prediction.predict([[Pregnancies, Glucose, PBloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if pred_diagnosis[0] == 1:
            diab_diagnosis = 'the person is diabetic'
        else:
                diab_diagnosis = 'the person is not diabetic'
      
     st.success(diab_diagnosis)       
         
         
         
         
         
         
         
         
         
         
         
if (selected == 'heart diseases prediction'):
    st.title('Heart Diseases Prediction using ML')
    col1, col2, col3 = st.columns(3)
   
    with col1:
        age = st.text_input('Age of person', key='age_input')
    with col2:
        sex = st.text_input('Gender', key='sex_input')
    with col3:
        cp = st.text_input('Chest pain type', key='cp_input')
    with col1:
        trestbps = st.text_input('Resting blood pressure', key='trestbps_input')
    with col2:
        chol = st.text_input('Serum cholestoral in mg/dl', key='chol_input')
    with col3:
        fbs = st.text_input('Fasting blood sugar > 120 mg/dl', key='fbs_input')
    with col1:
        restecg = st.text_input('Resting electrocardiographic results', key='restecg_input')
    with col2:
        thalach = st.text_input('Maximum heart rate achieved', key='thalach_input')
    with col3:
        exang = st.text_input('Exercise induced angina', key='exang_input')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest', key='oldpeak_input')
    with col3:
        slope = st.text_input('The slope of the peak exercise ST segment', key='slope_input')
    with col1:
        ca = st.text_input('Number of major vessels (0-3) colored by fluoroscopy', key='ca_input')
    with col2:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', key='thal_input')

    heart_diagnosis = ''

    if st.button('Heart Test Result'):
        hrt_diagnosis = heart_diseases_prediction.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
     
        if hrt_diagnosis[0] == 1:
            heart_diagnosis = 'the person has heart disease'
        else:
            heart_diagnosis = 'the person does not have heart disease'

    st.success(heart_diagnosis)                
       
   
if (selected == 'parkinsons prediction'):
    st.title('Parkinsons Prediction using ML')
    col1, col2, col3 = st.columns(3)
   
    with col1:
        MDVP_Fo = st.text_input('Mean frequency (Hz) of the fundamental frequency', key='MDVP_Fo_input')
    with col2:
        MDVP_Fhi = st.text_input('Highest frequency (Hz) of the signal', key='MDVP_Fhi_input')
    with col3:
        MDVP_Flo = st.text_input('Lowest frequency (Hz) of the signal', key='MDVP_Flo_input')
    with col1:
        MDVP_Jitter = st.text_input('Percentage of jitter in the signal', key='MDVP_Jitter_input')
    with col2:
        MDVP_Jitter_Abs = st.text_input('Absolute jitter value', key='MDVP_Jitter_Abs_input')
    with col3:
        MDVP_RAP = st.text_input('Relative amplitude perturbation', key='MDVP_RAP_input')
    with col1:
        MDVP_PPQ = st.text_input('Five-point period perturbation quotient', key='MDVP_PPQ_input')
    with col2:
        Jitter_DDP = st.text_input('Average absolute difference of differences between jitter cycles', key='Jitter_DDP_input')
    with col3:
        MDVP_Shimmer = st.text_input('Amplitude variation in the signal', key='MDVP_Shimmer_input')
    with col1:
        MDVP_Shimmer_dB = st.text_input('Shimmer in dB', key='MDVP_Shimmer_dB_input')
    with col2:
        Shimmer_APQ3 = st.text_input('Amplitude perturbation quotient (APQ3)', key='Shimmer_APQ3_input')
    with col3:
        Shimmer_APQ5 = st.text_input('Amplitude perturbation quotient (APQ5)', key='Shimmer_APQ5_input')
    with col1:
        MDVP_APQ = st.text_input('Amplitude perturbation quotient', key='MDVP_APQ_input')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer of the signal', key='Shimmer_DDA_input')
    with col3:
        NHR = st.text_input('Noise-to-harmonics ratio', key='NHR_input')
    with col1:
        HNR = st.text_input('Harmonics-to-noise ratio', key='HNR_input')
    with col2:
        RPDE = st.text_input('Recurrence period density entropy', key='RPDE_input')
    with col3:
        DFA = st.text_input('Detrended fluctuation analysis', key='DFA_input')
    with col1:
        spread1 = st.text_input('Spread of principal component 1', key='spread1_input')
    with col2:
        spread2 = st.text_input('Spread of principal component 2', key='spread2_input')
    with col3:
        D2 = st.text_input('Nonlinear dynamical complexity measurement', key='D2_input')
    with col1:
        PPE = st.text_input('Pitch period entropy', key='PPE_input')

    parkinsons_diagnosis = ''

    if st.button('Parkinsons Test Result'):
        parkinsons_diagnosis = parkinsons_prediction.predict([[MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if parkinsons_diagnosis[0] == 1:
            parkinsons_diagnosis = 'the person has Parkinson\'s disease'
        else:
            parkinsons_diagnosis = 'the person does not have Parkinson\'s disease'

    st.success(parkinsons_diagnosis)

if (selected == 'breast cancer prediction'):
    st.title('Breast Cancer Prediction using ML')
    col1, col2, col3 = st.columns(3)
   
    with col1:
        radius_mean = st.text_input('Radius Mean', key='radius_mean_input')
        perimeter_mean = st.text_input('Perimeter Mean', key='perimeter_mean_input')
        compactness_mean = st.text_input('Compactness Mean', key='compactness_mean_input')
        concavity_mean = st.text_input('Concavity Mean', key='concavity_mean_input')
        concave_points_mean = st.text_input('Concave Points Mean', key='concave_points_mean_input')
    with col2:
        texture_mean = st.text_input('Texture Mean', key='texture_mean_input')
        area_mean = st.text_input('Area Mean', key='area_mean_input')
        smoothness_mean = st.text_input('Smoothness Mean', key='smoothness_mean_input')
        symmetry_mean = st.text_input('Symmetry Mean', key='symmetry_mean_input')
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean', key='fractal_dimension_mean_input')
    with col3:
        radius_se = st.text_input('Radius SE', key='radius_se_input')
        perimeter_se = st.text_input('Perimeter SE', key='perimeter_se_input')
        compactness_se = st.text_input('Compactness SE', key='compactness_se_input')
        concavity_se = st.text_input('Concavity SE', key='concavity_se_input')
        concave_points_se = st.text_input('Concave Points SE', key='concave_points_se_input')
    
    breast_cancer_diagnosis = ''

    if st.button('Breast Cancer Test Result'):
        breast_cancer_diagnosis = breast_cancer_prediction.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, perimeter_se, compactness_se, concavity_se, concave_points_se]])
        
        if breast_cancer_diagnosis[0] == 1:
            breast_cancer_diagnosis = 'the person has Breast Cancer'
        else:
            breast_cancer_diagnosis = 'the person does not have Breast Cancer'

    st.success(breast_cancer_diagnosis)

