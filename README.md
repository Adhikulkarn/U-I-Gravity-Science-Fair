# 🌍 Gravity Playground Simulator  
A U&I Science Fair Project

This project is a science-fair learning tool built for U&I.  
It allows students to explore how **gravity changes on different planets** by simulating:

- ⚖️ **Weight on different planets**  
- 🛠️ **Custom planet gravity** (user-defined mass & radius)  
- 🚀 **Escape velocity**  
- 🦘 **Jump height variation**  
- 🪂 **Fall time simulation**

The goal is to make space physics interactive, visual, and easy to understand for kids.

---

## 🚀 Tech Stack

### **Backend**
- **FastAPI** – REST API for physics calculations  
- **Python** – Gravity formulas & simulations  

### **Frontend**
- **HTML**  
- **CSS** (custom UI + animations)  
- **JavaScript** (fetch API calls + dynamic UI)

---

## 🛠️ Setup Instructions (Run Project Locally)

### **1️⃣ Backend Setup**

#### **Step 1: Navigate to the backend directory**
```bash
cd backend
```
#### **step 2: Create a vertual environment**
For windowa: 
```bash
python -m venv venv
venv\Scripts\activate
```
For Linux (Ubuntu):
```bash
python3 -m venv venv
source venv/bin/activate
```

#### **Step 3: Download requirements**
Install the requirements from requirements.txt by 
```bash
pip install -r requirements.txt
```

#### **Step 4: Run Backend Server**
To run the backend Server use the following command 
```bash
uvicorn main:app --reload
```
YOU ARE ALL SET WITH THE BACKEND
The backend server will be locally running at
```bash
http://127.0.0.1:8000
```
### **2️⃣ Frontend Setup**

Running the frontend is simple, Go to The **index.html** file in the frontend folder and run it using the **Live Server** extention from VScode. If not available, download the extention from VScode Extention by searching 'Live Server'

YOU ARE ALL SET WITH THE FRONTEND
The frontend code will be locally running at
```bash
http://127.0.0.1:5500
```

BOOOM YOU ALL SET WITH PROJECT RUNNING IN YOUR LAPTOP!!!!!!!!!!!!!!!!!!!!!!!


