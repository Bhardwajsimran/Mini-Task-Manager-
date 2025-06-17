#  Mini Task Manager

A simple web-based task manager built using **Flask** (backend) and **Next.js + Tailwind CSS** (frontend).  
Made during my internship to practice CRUD operations, REST APIs, and UI basics.

---

## Tech Stack

- **Frontend:** Next.js, React, Tailwind CSS
- **Backend:** Python, Flask (in-memory data storage)
- **API:** RESTful endpoints
- **Deployment:** Localhost

---

## Features

-  Add new tasks
-  View all tasks
-  Delete tasks
- Simple UI with Tailwind CSS

---

## Getting Started

### Backend (Flask)

```bash
cd backend
pip install flask
python app.py

The backend will run at http://localhost:5000.


---

 Frontend (Next.js)

cd frontend
npm install
npm run dev

The frontend will run at http://localhost:3000.


---

API Endpoints

Method	Endpoint	Description

GET	/tasks	Get all tasks
POST	/tasks	Add a new task
DELETE	/tasks/<task_id>	Delete a task


---

Project Structure

mini-task-manager/
├── backend/
│   └── app.py
├── frontend/
│   ├── pages/
│   │   └── index.js
│   ├── styles/
│   │   └── globals.css
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── package.json
├── .gitignore
└── README.md




