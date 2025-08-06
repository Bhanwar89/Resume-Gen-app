# Resume Generator App (Docker + Streamlit)

This project runs a Streamlit-based resume generator inside Docker.

## 📦 Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed

---

## 🚀 Build the Docker Image
From the project root (where your `Dockerfile` is located):

```bash
docker build -t resume-gen-app .
```

```bash
docker run -it --rm -p 8501:8501 resume-gen-app
```

Access the app on 
```
http://localhost:8501
```
