
# Dockerizing and Orchestrating a Microservices Application

A hands-on project showcasing the power of Docker and orchestration tools like Docker Swarm, Kubernetes, Helm, and Argo CD to containerize and deploy a microservices-based web application.

## 🚀 Project Overview

This project demonstrates:

- **Containerization** of a simple frontend-backend web application using Docker.
- **Orchestration** using Docker Swarm and Kubernetes.
- **CI/CD automation** using GitHub and Argo CD.
- **Deployment** via Helm charts.

## 🔗 Live Endpoints

- **Frontend**: http://localhost:8080  
- **Backend API**: http://localhost:5000/api/todos  
- **Argo CD UI**: https://localhost:8081  

---

## 📁 Folder Structure

```
.
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   └── index.html
├── k8s/
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   └── frontend-service.yaml
├── deployment-helm-backend/
├── deployment-helm-frontend/
└── docker-compose.yml
```

---

## 🎯 Objectives

- Containerize a multi-service application.
- Explore orchestration using Docker Swarm and Kubernetes.
- Automate deployment using Helm and Argo CD.

---

## 🛠️ Tools & Technologies

- Docker  
- Docker Swarm  
- Kubernetes (kubectl, Minikube)  
- Helm  
- Argo CD  
- GitHub  

---

## ⚙️ Setup Instructions

### 1. Docker Installation

**Ubuntu:**

```bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
sudo docker run hello-world
```

**Windows:**

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Enable WSL 2 and virtualization
- Run `docker --version` to verify installation

---

## 🧱 Containerization

**Build Images:**

```bash
# Backend
cd backend
docker build -t <username>/todo-backend .

# Frontend
cd ../frontend
docker build -t <username>/todo-frontend .
```

**Run Containers:**

```bash
docker run -d -p 5000:5000 --name backend <username>/todo-backend
docker run -d -p 8080:80 --name frontend <username>/todo-frontend
```

---

## ⚓ Docker Swarm Deployment

```bash
docker swarm init
docker stack deploy -c docker-compose.yml todoapp
docker service ls
```

---

## ☸️ Kubernetes Deployment

**Push Images to Docker Hub:**

```bash
docker login
docker tag local-image <username>/image-name:tag
docker push <username>/image-name:tag
```

**Apply Kubernetes Configs:**

```bash
kubectl apply -f k8s/
kubectl get deployments
kubectl get pods
kubectl get services
```

**Forward Ports Locally:**

```bash
kubectl port-forward pod/<pod-name> 5000:5000  # backend
kubectl port-forward pod/<pod-name> 8080:80    # frontend
```

---

## 🤖 Argo CD + Helm Setup (Auto Deployment)

**Install Argo CD:**

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl port-forward service/argocd-server -n argocd 8081:80
```

**Helm Chart Structure Includes:**

- Chart.yaml  
- values.yaml  
- deployment.yaml  

**Push to GitHub:**

```bash
git init
git remote add origin https://github.com/your-repo/python-todo.git
git add .
git commit -m "initial commit"
git push origin main
```

**Connect GitHub Repo to Argo CD:**

1. Log in at https://localhost:8081  
2. Create apps for frontend and backend  
3. Use repo URL, correct branch, and path  

---

## 📚 References

- [Docker Documentation](https://docs.docker.com/get-started/docker-overview/)  
- [Kubernetes Documentation](https://kubernetes.io/docs/concepts/overview/)  
- [Argo CD Documentation](https://argo-cd.readthedocs.io/en/stable/)  

---

## 👨‍💻 Authors

- Gurminder Singh  
- Kushal Sharma  
- Nameson Gaudel  
- Pradeep Wagle  
- Sagar Giri  

Postgraduate in DOCT, Lambton College  
Course: CBD 3324  
Instructor: Mohammad Salim  
Date: April 14, 2025
