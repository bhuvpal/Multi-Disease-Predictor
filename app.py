import streamlit as st
import pickle
from streamlit_option_menu import option_menu


#LungCancer1 = pickle.load(open('LungCancer1.pkl','rb'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             '))
selected = ['Breast Cancer Prediction','Lung Cancer Prediction','Diabetes Prediction','Heart Atteck Prediction','Parkinson Disease Prediction']
st.set_page_config('🦠MultiDiseasePrediction')

Breast_df = pickle.load(open('BreastCancer2.pkl','rb'))
Lung_df = pickle.load(open('LungCancer.pkl','rb'))
parkinson_df = pickle.load(open('Parkinson (1).pkl','rb'))
heart_df = pickle.load(open('heartAtteck (2).pkl','rb'))
Diabetes_df = pickle.load(open('Diabetes.pkl','rb'))
DiabetesScaler = pickle.load(open('scaling (1).pkl','rb'))
LungScaler = pickle.load(open('Scaler.pkl','rb'))
Breast_scaled = pickle.load(open('BreastScaler.pkl','rb'))
Parkinson_scaled = pickle.load(open('ParkinsonScaler.pkl','rb'))
Heart_Scaled = pickle.load(open('heartscale (1).pkl','rb'))
with st.sidebar:
    select = option_menu('MultiDisease Predictor',selected,default_index=0)



if select=='Breast Cancer Prediction':
    st.header('Breast Cancer Prediction System')

    col1,col2,col3 = st.columns(3)
    with col1: 
         radius = st.number_input('Enter Radius Mean')
         areamean = st.number_input('Enter Area Mean')
         concavitymean = st.number_input('Enter Concavity Mean')
         fractaldimension_mean = st.number_input('Enter FractalDimention Mean')
         area_Se = st.number_input('Enter Area SE')
         concave_points_Se = st.number_input('Enter Concave Point SE')
         perimeterworst = st.number_input('Enter Parimeter Worst')
         compactnessworst = st.number_input('Enter Compactness Worst')
         symmetryworst = st.number_input('Enter Symmetric Worst')
    
    
    with col2:
         texturemean = st.number_input('Enter Texture Mean')
         smoothnessmean = st.number_input('Enter Smoothness Mean')
         concavepoints_mean = st.number_input('Enter ConcavePoint Mean')
         radius_Se = st.number_input('Enter Radius SE')
         compactness_Se = st.number_input('Enter Compactness SE')
         radiusworst = st.number_input('Enter Radius Worst')
         areaworst = st.number_input('Enter Area Worst')
         concavityworst = st.number_input('Enter Concavity Worst')
         fractaldimension_worst = st.number_input('Enter FractalDimention Worst')
         

    with col3:
         perimetermean = st.number_input('Enter Parameter Mean')
         compactnessmean = st.number_input('Enter Compactness Mean')
         symmetrymean = st.number_input('Enter Symmetric Mean')
         perimeter_Se = st.number_input('Enter Parameter SE')
         concavity_Se = st.number_input('Enter Concavity SE')
         textureworst = st.number_input('Enter Texture Worst')
         smoothnessworst = st.number_input('Enter Smoothness Worst')
         concavepoints_worst = st.number_input('Enter ConcavePoint Worst')
    



    pred = ''
    if st.button('Test Breast Cancer'):
       input2 = Breast_scaled.transform([[radius,texturemean,perimetermean,areamean,smoothnessmean,compactnessmean,concavitymean,concavepoints_mean,
                                          symmetrymean,fractaldimension_mean,radius_Se,perimeter_Se,area_Se,compactness_Se,concavity_Se,concave_points_Se,
                                          radiusworst,texturemean,perimeterworst,areaworst,smoothnessworst,compactnessworst,concavityworst,concavepoints_worst,
                                          symmetryworst,fractaldimension_worst]])

       result2 = Breast_df.predict_proba(input2)
       pred = f'Chanses of Breast Cancer is {result2[0][1]*100:.2f}%'
       
    st.success(pred)
    

if select=='Lung Cancer Prediction':
   st.header('Lung Cancer Prediction System')


   col1,col2 = st.columns(2)
   with col1:
        gender = st.selectbox('Gender Status',[None,'Male','Female'])
        if gender=='Male':
             gender=1
        else:
             gender=0
        smoking = st.selectbox('Smoking Status',[None,'Yes','No'])
        if smoking=='Yes':
             smoking=2
        else:
             smoking=1

        anxiety = st.selectbox('Anxiety Status',[None,'Yes','No'])
        if anxiety=='Yes':
             anxiety=2
        else:
             anxiety=1
        disease = st.selectbox('Chronic Disease Status',[None,'Yes','No'])
        if disease=='Yes':
             disease=2
        else:
             disease=1
        allergy = st.selectbox('Allergy Status',[None,'Yes','No'])
        if allergy=='Yes':
             allergy=2
        else:
             allergy=1
        alcohol = st.selectbox('Alcohol Status',[None,'Yes','No'])
        if alcohol=='Yes':
             alcohol=2
        else:
             alcohol=1
        shortness = st.selectbox('Shortness or Breething Status',[None,'Yes','No'])
        if shortness=='Yes':
             shortness=2
        else:
             shortness=1
        pain = st.selectbox('Chest Pain Status',[None,'Yes','No'])
        if pain=='Yes':
             pain=2
        else:
             pain=1
   with col2:
        age = st.number_input('Enter The Age of Patirnt')
        Finger = st.selectbox('Yellow Finger status',[None,'Yes','No'])
        if Finger=='Yes':
             Finger=2
        else:
             Finger=1
        pressure = st.selectbox('Peer Presure Status',[None,'Yes','No'])
        if pressure=='Yes':
             pressure=2
        else:
             pressure=1
        fatigue = st.selectbox('Fatigue Status',[None,'Yes','No'])
        if fatigue=='Yes':
             fatigue=2
        else:
             fatigue=1
        wheezing = st.selectbox('Wheezing Status',[None,'Yes','No'])
        if wheezing=='Yes':
             wheezing=2
        else:
             wheezing=1
        coughing = st.selectbox('Coughing Status',[None,'Yes','No'])
        if coughing=='Yes':
             coughing=2
        else:
             coughing=1
        Swallow = st.selectbox('Swellwing Difficulteis Status',[None,'Yes','No'])
        if Swallow=='Yes':
             Swallow=2
        else:
             Swallow=1

   predd = ''

   if st.button('Test Lung Cancer'):
        input1 = LungScaler.transform([[gender,age,smoking,Finger,anxiety,pressure,disease,fatigue,allergy,wheezing,alcohol,coughing,shortness,Swallow,pain]])
        Result = Lung_df.predict_proba(input1)
        predd = f'Chanses of Lung Cancer is {Result[0][1]*100:.2f}%'
   st.success(predd)

if select=='Diabetes Prediction':
    st.header('Diabetes Prediction System')
    col1,col2,col3 = st.columns(3)
    with col1:
         pregnencies = st.number_input('Enter Number of Pregnencies')
         skinthick = st.number_input('Enter Skin Thickness Level')
         diabetes = st.number_input('Enter Diabetes Padigree Function')
    with col2:
         glucose = st.number_input('Enter Glucose Level')
         insulin = st.number_input('Enter Insulin Level')
         age = st.number_input('Enter Age of Patient')
    with col3:
         bloodpressure = st.number_input('Enter Blood Presure Level')
         bmi = st.number_input('Enter BMI')
    predy = ''
    if st.button('Test Diabetes'):
         input_df = DiabetesScaler.transform([[pregnencies,glucose,bloodpressure,skinthick,insulin,bmi,diabetes,age]])
         result = Diabetes_df.predict_proba(input_df)
         predy = f'Probability of Diabetes is {result[0][1]*100:.2f}%'
    st.success(predy)
     

if select=='Heart Atteck Prediction':
     st.header('Heart Atteck Prediction System')

     col1,col2 = st.columns(2)

     with col1:
          age = st.number_input('Enter Age')
          heartrate = st.number_input('Heart Rate')
          dbloodpressure = st.number_input('Diastolic Blood Pressure')
          ckmb = st.number_input('CK-MB')

     with col2:
          gender = st.selectbox('Select Gender',[None,'Male','Female'])
          if gender=='Male':
               gender=1
          else:
               gender=0
          bloodpressure = st.number_input('Systolic Blood Pressure')
          bloodsugar = st.number_input('Blood Sugar')
          troponin = st.number_input('Troponin')


     preddie = ''
     if st.button('Test HeartAtteck'):
          input44 = Heart_Scaled.transform([[age,gender,heartrate,bloodpressure,dbloodpressure,bloodsugar,ckmb,troponin]])
          res = heart_df.predict_proba(input44)
          preddie = f'Chances of Heart Atteck is {res[0][1]*100:.2f}%'


     st.success(preddie)



if select=='Parkinson Disease Prediction':
    st.header('Parkinson Disease Prediction System')

    col1,col2 = st.columns(2)
    with col1:
         avg_freq = st.number_input('MDVP:Fo(Hz)')
         low_freq = st.number_input('MDVP:Flo(Hz)')
         jitter_abs = st.number_input('MDVP:Jitter(Abs)')
         ppq = st.number_input('MDVP:PPQ')
         shimmer = st.number_input('MDVP:Shimmer')
         apq3 = st.number_input('Shimmer:APQ3')
         apq = st.number_input('MDVP:APQ')
         nhr = st.number_input('NHR')
         rdpe = st.number_input('RDPE')
         spread1 = st.number_input('spread1')
         d2 = st.number_input('D2')
     
    with col2:
         high_freq = st.number_input('MDVP:Fhi(Hz)',)
         jitter_percent = st.number_input('MDVP:Jitter(%)')
         rap = st.number_input('MDVP:RAP')
         ddp = st.number_input('Jitter:DDP')
         shimmer_db = st.number_input('MDVP:Shimmer(dB)')
         apq5 = st.number_input('Shimmer:APQ5')
         dda = st.number_input('Shimmer:DDA')
         hnr = st.number_input('HNR')
         dfa = st.number_input('DFA')
         spread2 = st.number_input('spread2')
         ppe = st.number_input('PPE')
     
    preddic = ''
    if st.button('Test Parkinson Disease'):
       input_data = Parkinson_scaled.transform([[avg_freq,high_freq,low_freq,jitter_percent,jitter_abs,
                                                 rap,ppq,ddp,shimmer,shimmer_db,apq3,apq3,apq,dda,nhr,hnr,rdpe,dfa,spread1,spread2,d2,ppe]])
       resultyyy = parkinson_df.predict_proba(input_data)
       preddic = f'Chances of Parkinson Disease is {resultyyy[0][1]*100:.2f}%'
    st.success(preddic)





    