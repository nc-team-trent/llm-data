# 🧠 LLM-Powered Data Processor

This project is a FastAPI-based Python application designed to process and analyze data using language models. It's fully containerized using Docker for easy setup and deployment.

---

## 📁 Project Structure

```
.
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── README.md
├── report
│   ├── project_idea.md
│   ├── project_report.md
│   └── project_requirements.md
├── requirements.txt
└── src
    ├── app
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-313.pyc
    │   │   ├── main.cpython-313.pyc
    │   │   ├── processor.cpython-313.pyc
    │   │   └── utils.cpython-313.pyc
    │   ├── main.py
    │   ├── processor.py
    │   └── utils.py
    └── data
        └── example.txt
```
#### 📦 Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

#### 🔧 Build & Run (in background):
bash
Copy
Edit


```
docker-compose up --build -d

```
#### 🧪 Check logs:

```
docker-compose logs -f

```
#### 🛑 Stop:
```
docker-compose down
```
#### 🐍 Test the APP

1. Go to the app URL : http://127.0.0.1:8000/transform/
You will find the user instructions there!

2. You can also test it interactively at: http://localhost:8000/docs


