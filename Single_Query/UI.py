import streamlit as st
import subprocess
import pandas as pd
import hashlib
from tinydb import TinyDB, Query

def process_question(NL_question):
    try:
        subprocess.call(["./single_query.sh",str(NL_question)])
        with open("output.txt") as output_file:
            query = output_file.readline()
        st.write("SQL Query:")
        st.write(query)
    except Exception:
        st.write("Some Error Occurred")

def generate_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def display_schema_info():
    st.write("DB ID: employee_hire_evaluation")
    employee_columns = ["employee id","name","age","city"]
    shop_columns = ["shop id","name","location","district","number products","manager name"]
    hiring_columns = ["shop id","employee id","start from","is full time"]
    evaluation_columns = ["employee id","year awarded","bonus"]
    st.write("1) employee")
    st.write(employee_columns)
    st.write("2) shop")
    st.write(shop_columns)
    st.write("3) hiring")
    st.write(hiring_columns)
    st.write("4) evaluation")
    st.write(evaluation_columns)


if __name__ == "__main__":
    st.title("NL to SQL")
    menu = ["Home", "Query"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.title("Team Members")
        names = [["Ishwar Joshi","PES1UG19CS191"],["Manjunath Gowda S","PES1UG19CS264"],["Satwik Bhagwat","PES1UG19CS438"],["Shreevathsa BK","PES1UG19CS461"]]
        data = pd.DataFrame(names,columns=("Name","SRN"))
        st.table(data)
    elif choice == "Query":
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            db = TinyDB('credentials.json')
            DBquery = Query()
            result = db.search(DBquery.name == username)
            if len(result) == 1 and generate_hash(password) == result[0]['hash']:
                st.sidebar.success("Logged In as {}".format(username))
                with st.form("Question_form"):
                    st.write("NL to SQL")
                    NL_question = st.text_input('Enter your Query')
                    submitted = st.form_submit_button("Submit")
                    if submitted:
                        process_question(NL_question)
                display_schema_info()
            else:
                st.error("Incorrect username or password")
        else:
            st.subheader("Enter your credentials in the menu on the left")
