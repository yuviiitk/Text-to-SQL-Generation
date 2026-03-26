import streamlit as st
import pandas as pd
import sqlite3
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key = api_key)

def generate_sql(prompt):
    response = client.chat.completions.create(model="llama-3.1-8b-instant",
                                              messages = [{"role": "user", "content": prompt}])
    return response.choices[0].message.content

st.title("Text to SQL Generation")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    conn = sqlite3.connect("data.db")
    df.to_sql("my_table", conn, if_exists="replace", index=False)
    st.success("Data stored in database succesfully")
    st.subheader("Data Preview")
    st.dataframe(df.head())
    columns = ", ".join(df.columns)
    st.subheader("Table Schema ( Columns )")
    st.write(columns)
    st.subheader("Ask a question")
    user_query = st.text_input("Enter your question in english")
    if user_query:
        prompt = f"""
                You are an SQL expert
                Table: my_table
                Columns: {columns}
                Rules:
                    - Use only given columns
                    - Return only SQL query
                    - No explanation
                Question: {user_query}
                """
        sql_query = generate_sql(prompt)
        sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
        st.subheader("Generated SQL")
        st.code(sql_query, language="sql")
        try:
            result_df = pd.read_sql_query(sql_query, conn)
            st.subheader("Generated SQL Result")
            st.dataframe(result_df)
        except Exception as e:
            st.error(f"Error executing SQL: {e}")