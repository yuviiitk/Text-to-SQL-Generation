# 🧠 Text-to-SQL AI Application

An AI-powered web application that converts natural language queries into SQL, executes them on structured data, and displays results instantly.

---

## 🚀 Live Demo

👉 Deployed on Render
link: https://text-to-sql-generation.onrender.com/

---

## 📌 Project Overview

This project allows users to:

* Upload a CSV dataset
* Ask questions in plain English
* Automatically convert queries into SQL using AI
* Execute SQL on the dataset
* View results instantly

---

## 🧠 How It Works

```
User Input (English)
        ↓
Prompt Engineering
        ↓
Groq LLM (AI Model)
        ↓
SQL Query Generation
        ↓
SQLite Database Execution
        ↓
Results Display (Streamlit UI)
```

---

## ⚙️ Tech Stack

### 💻 Development

* Python
* Pandas
* SQLite

### 🤖 AI

* Groq API (LLM)

### 🎨 Frontend

* Streamlit

### ⚙️ DevOps

* Git & GitHub
* Docker
* Render (Cloud Deployment)

---

## 🧩 Features

* 📁 Upload CSV file
* 🧠 Convert natural language → SQL
* ⚡ Execute SQL queries instantly
* 📊 Display results in table format
* 🔐 Secure API key handling
* 🌐 Live deployment

---

## 📂 Project Structure

```
Text-to-SQL-App/
│
├── app.py              # Main Streamlit app
├── requirements.txt   # Dependencies
├── Dockerfile         # Container setup
├── .dockerignore      # Ignore unnecessary files
├── .gitignore         # Ignore secrets & system files
├── sample.csv         # Example dataset
└── README.md
```

---

## 🛠️ Setup Instructions (Local)

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/text-to-sql-app.git
cd text-to-sql-app
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add API Key

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Application

```
streamlit run app.py
```

---

## 🐳 Docker Setup

### Build Docker Image

```
docker build -t text-to-sql-app .
```

---

### Run Container

```
docker run -p 8501:8501 -e GROQ_API_KEY=your_key text-to-sql-app
```

---

### Open App

```
http://localhost:8501
```

---

## ☁️ Deployment (Render)

1. Push code to GitHub
2. Go to Render
3. Create new Web Service
4. Select repository
5. Choose Docker environment
6. Add environment variable:

```
GROQ_API_KEY = your_key
```

7. Deploy

---

## 💡 Example Queries

* Show all data
* Highest marks
* Average marks by city
* Show marks of Aman
* Highest and lowest marks

---

## 🧠 Key Learnings

* Prompt Engineering for AI
* LLM Integration
* SQL Query Generation
* Docker Containerization
* Cloud Deployment

---

## 🚀 Future Improvements

* Improve AI accuracy (better prompts)
* Add chat-style UI
* Add authentication system
* Replace SQLite with PostgreSQL
* Convert backend to FastAPI

---

## 📄 Resume Description

Built and deployed an AI-powered Text-to-SQL application that converts natural language queries into SQL using Groq LLM, executes them on structured datasets, and serves results via a containerized Streamlit application deployed on Render.

---

## 🤝 Contributing

Feel free to fork this repository and improve the project.

---

## ⭐ Acknowledgement

This project demonstrates practical implementation of AI + Backend + Deployment in a real-world scenario.
