# DevOps & DevSecOps Exam Study Kit

A comprehensive guide and quick-reference workspace covering Git/GitHub, Python APIs, Docker, Kubernetes, Terraform, Trivy Security Scanning, Pytest/JUnit, Jenkins CI/CD, and ArgoCD GitOps.

---

## Workspace Structure

```text
.
├── app.py                   # Minimal Flask API (Health Check & Data endpoints)
├── requirements.txt         # Dependencies (Flask & pytest)
├── Dockerfile               # Production Docker container image setup
├── test_app.py              # Pytest unit testing script (JUnit XML compatible)
├── main.tf                  # Terraform local infrastructure definition
├── Jenkinsfile              # Full CI/CD Pipeline (Checkout -> Test -> Trivy Scan -> Build)
├── argocd-app.yaml          # GitOps ArgoCD Application manifest
├── README.md                # Quick-start documentation & Command Reference
└── k8s/                     # Kubernetes Manifests
    ├── configmap.yaml       # Environment Configuration
    ├── deployment.yaml      # Deployment manifest (2 replicas)
    └── service.yaml         # NodePort Service manifest
```

---

## 1. Git & GitHub Fundamentals

### Workflow & Commands
```bash
# Initialize local repository
git init my-app
cd my-app

# Link to remote GitHub repository
git remote add origin https://github.com/your-username/your-repo.git

# Standard Git commit & push workflow
git status
git add .
git commit -m "feat: setup complete devops application"
git branch -M main
git push -u origin main
```

---

## 2. Python Backend APIs & Unit Testing

### Running API Locally
```bash
# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run application
python3 app.py

# Test endpoints in separate terminal
curl http://localhost:5000/
curl http://localhost:5000/api/v1/data
```

### Running Tests & Generating JUnit Reports
```bash
# Execute pytest and produce JUnit-compatible XML report for Jenkins
pytest --junitxml=results.xml
```

---

## 3. Docker Containerization

### Docker Workflow
```bash
# Build Docker image
docker build -t flaskapp:v1 .

# Run container in background
docker run -d -p 5000:5000 --name flask-container flaskapp:v1

# Inspect container status and logs
docker ps
docker logs flask-container

# Verify API inside container
curl http://localhost:5000/
```

---

## 4. Kubernetes Core & Manifests

### Deploying to Kubernetes Cluster
```bash
# Apply ConfigMap, Deployment, and Service manifests
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Verify resource deployment
kubectl get pods
kubectl get deployments
kubectl get svc
kubectl get configmap

# Troubleshooting & Logs
kubectl logs -l app=flaskapp
kubectl describe pod <pod-name>
```

---

## 5. Terraform Infrastructure as Code

### Terraform Execution Workflow (Strict Sequence)
```bash
# 1. Initialize working directory and download providers
terraform init

# 2. Format configuration file to standard layout
terraform fmt

# 3. Validate syntax and structural correctness
terraform validate

# 4. Preview execution plan
terraform plan

# 5. Apply changes without manual prompt
terraform apply -auto-approve
```

### Terraform State Management
```bash
# Inspect overall state file
terraform show

# List all tracked resources
terraform state list

# View detailed properties of a specific state item
terraform state show local_file.sample_config

# Display output variables
terraform output
```

---

## 6. DevSecOps & Security Tools

### Static Analysis & Container Scanning
```bash
# Python Static Application Security Testing (SAST) with Bandit
pip install bandit
bandit -r app.py

# File system & secrets scan with Trivy
trivy fs --severity HIGH,CRITICAL .

# Container image vulnerability scanning
trivy image --severity HIGH,CRITICAL flaskapp:v1
```

---

## 7. CI/CD: Jenkins & ArgoCD

### Jenkins Pipeline Summary
The included `Jenkinsfile` runs through the following automated stages:
1. **Checkout Code:** Pulls latest code from Git branch.
2. **Unit Tests:** Executes `pytest` and publishes JUnit XML test reports.
3. **Security Scan:** Runs `trivy fs .` to ensure zero critical secrets/vulnerabilities.
4. **Build & Tag:** Packages the verified code into a tagged Docker image.

### ArgoCD GitOps Deployment
```bash
# Apply ArgoCD Application Manifest
kubectl apply -f argocd-app.yaml

# OR create and sync directly via ArgoCD CLI
argocd app create flask-gitops-app \
  --repo https://github.com/your-username/your-repo.git \
  --path k8s \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default

# Trigger manual synchronization
argocd app sync flask-gitops-app

# Monitor deployment health
argocd app get flask-gitops-app
```