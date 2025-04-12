todo-app/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
├── k8s/
│   ├── mariadb-deployment.yaml
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   └── kustomization.yaml (optional)
│
└── README.md


🛠️ Docker Build & Push (example)
bash
Copy
Edit
# Backend
cd backend
docker build -t yourdockerhub/backend:latest .
docker push yourdockerhub/backend:latest

# Frontend
cd ../frontend
docker build -t yourdockerhub/frontend:latest .
docker push yourdockerhub/frontend:latest
