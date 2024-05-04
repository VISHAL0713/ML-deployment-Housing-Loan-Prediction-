import streamlit as st
import pickle
model = pickle.load(open('model.pkl', 'rb'))
def predict(Gender,Married,Dependents,Education,Self_Employed,LoanAmount,Loan_Amount_term,Credit_History,TotalIncome):
    prediction=model.predict([[Gender,Married,Dependents,Education,Self_Employed,LoanAmount,Loan_Amount_term,Credit_History,TotalIncome]])
    return prediction
def main():
    st.title("Housing Loan Prediction") 
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Housing Loan Predictor </h2>   
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Gender = st.text_input("Gender","Enter 1 for Male and 0 for female")
    Married = st.text_input("Married","Enter 1 for Yes and 0 for No")
    Dependents = st.text_input("Dependents","Enter Integer value Here")
    Education = st.text_input("Education","Enter 0 for Graduate and 1 for Non-Graduate")
    Self_Employed = st.text_input("Self_Employed","Enter 1 for Yes and 0 for No")
    LoanAmount = st.text_input("LoanAmount","Type Here")
    Loan_Amount_term = st.text_input("Loan_Amount_term","Type Here")
    Credit_History = st.text_input("Credit_History","Type Here")
    TotalIncome = st.text_input("TotalIncome","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(Gender,Married,Dependents,Education,Self_Employed,LoanAmount,Loan_Amount_term,Credit_History,TotalIncome)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
main()