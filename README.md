# 🚀 Containerized Application Deployment with Docker, Jenkins & AWS

A complete CI/CD project demonstrating how to build, containerize, and deploy a Python Flask application using **Docker**, **Jenkins**, and **Amazon Web Services (AWS)**.

This project showcases modern DevOps practices including automated builds, Docker image creation, continuous integration, and cloud deployment.

---

## 📌 Project Overview

This project automates the deployment of a Flask web application through a Jenkins CI/CD pipeline.

The workflow includes:

* Containerizing the application using Docker
* Automating build and deployment using Jenkins
* Deploying the application on AWS
* Managing application updates through a CI/CD pipeline

---

## 🏗️ Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
Jenkins Pipeline
    │
    ├── Build Flask Application
    ├── Build Docker Image
    ├── Run Tests (Optional)
    └── Deploy Container
    │
    ▼
AWS EC2 Instance
    │
    ▼
Docker Container
    │
    ▼
Flask Web Application
```

---

## 🛠️ Tech Stack

| Category         | Technologies |
| ---------------- | ------------ |
| Language         | Python 3     |
| Framework        | Flask        |
| Containerization | Docker       |
| CI/CD            | Jenkins      |
| Cloud            | AWS EC2      |
| Version Control  | Git & GitHub |
| Operating System | Ubuntu Linux |

---

## 📂 Project Structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── templates/
└── README.md
```

---

## ⚙️ Features

* Python Flask web application
* Dockerized application
* Jenkins CI/CD pipeline
* Automated Docker image build
* AWS EC2 deployment
* Easy application updates through GitHub
* Production-ready deployment workflow

---

## 🐳 Docker

### Build Image

```bash
docker build -t flask-app .
```

### Run Container

```bash
docker run -d -p 5000:5000 flask-app
```

Visit:

```
http://localhost:5000
```

---

## 🔄 Jenkins Pipeline

The Jenkins pipeline performs the following steps:

1. Pulls the latest code from GitHub
2. Builds the Flask application
3. Creates a Docker image
4. Stops the existing container (if running)
5. Deploys a new Docker container
6. Makes the updated application available

---

## ☁️ AWS Deployment

The application is deployed on an AWS EC2 instance.

Deployment process:

* Launch an EC2 instance
* Install Docker
* Install Jenkins
* Configure Jenkins pipeline
* Connect GitHub repository
* Build and deploy automatically

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open your browser:

```
http://localhost:5000
```





---

## 📈 Skills Demonstrated

* DevOps Fundamentals
* CI/CD Pipeline Implementation
* Docker Containerization
* Jenkins Automation
* AWS EC2 Deployment
* Linux Administration
* Git & GitHub
* Python Flask Development




---

