# RAG App – PanScience Innovations Assignment

## Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline that enables users to upload documents and query them. It uses:
- **Vector Database** for efficient document retrieval
- **LLM API** (OpenAI, Gemini, etc.) for contextual answer generation
- **FastAPI** for REST API endpoints
- **Docker** for containerization and deployment

---

## Features
- Upload up to 20 documents (max 1000 pages each)
- Automatic chunking and vector embedding storage
- Query processing with top-k document retrieval
- API endpoints for uploading, querying, and viewing metadata
- Fully containerized for local and cloud deployment

---

## Tech Stack
- **Backend:** FastAPI (Python)
- **Vector DB:** ChromaDB
- **LLM API:** Configurable (OpenAI, Gemini, etc.)
- **Containerization:** Docker & Docker Compose
- **Testing:** Postman

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/naveentopno20/rag-app.git
cd rag-app

---
```
### 2. Install Dependencies 

pip install -r requirements.txt

---

### 3. Run with Docker

docker-compose up --build
The API will be available at:
http://localhost:8000

---

### API Endpoints

| Method | Endpoint     | Description              |
| ------ | ------------ | ------------------------ |
| POST   | `/upload`    | Upload documents         |
| POST   | `/query`     | Query uploaded documents |
| GET    | `/documents` | List document metadata   |

---

### Postman Testing

The Postman collection is included in:
docs/rag-app-postman.json
Import this file into Postman to test all endpoints.

---

### Screenshots

1. Docker container running the RAG app.
2. Successful API query request (Swagger UI/Postman).

---

### Repository

GitHub Link: https://github.com/naveentopno20/rag-app

---

### Author
```bash
Naveen Topno

If you want, I can **directly prepare this file** for you now so you can just commit and push it to update your GitHub README.  
Do you want me to create this `README.md` file so you can just upload it?
