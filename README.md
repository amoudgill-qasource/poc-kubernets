# Python E-commerce Platform

[![CI/CD Pipeline](https://img.shields.io/badge/CI/CD-CloudBees%20%2B%20Octopus-blue)](https://jenkins.io/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Kind-blue)](https://kind.sigs.k8s.io/)
[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)

## 📋 Project Overview

**Project Title:** Retail E-commerce Platform
**Brand Name:** MultiZone

A comprehensive e-commerce solution built with Django, featuring product catalog management, user authentication, shopping cart functionality, and secure payment processing. This platform provides a complete online shopping experience with modern web technologies.

## 🏗️ Architecture & Technology Stack

### Core Technologies
- **Backend:** Python Django 4.2
- **Database:** MySQL 8.0
- **Frontend:** HTML5, CSS3, JavaScript
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Kind)
- **CI/CD:** CloudBees Core + Octopus Deploy

### Infrastructure Components
- **Local Development:** Docker Compose
- **Container Registry:** Local Docker images
- **CI Tool:** CloudBees Core (Self-hosted Jenkins)
- **CD Tool:** Octopus Deploy (Self-hosted)
- **Kubernetes:** Kind cluster for local development
- **Package Management:** Helm charts

## 🚀 CI/CD Pipeline Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Feature Branch│ -> │   CloudBees CI  │ -> │  Octopus Deploy │ -> │   Kind Cluster  │
│     Git Push    │    │   (Kaniko Build)│    │    (CLI Trigger)│    │  (Helm Deploy)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                        │                        │
         └─ Auto-trigger         └─ Image Build           └─ Release Creation      └─ App Deploy
```

### Continuous Integration (CI) - CloudBees Core

- **Platform:** Self-hosted Jenkins-based CI solution
- **Trigger:** Automatic on feature branch commits
- **Build Tool:** Kaniko (Kubernetes-native container builds)

#### CI Pipeline Features:
- **Automated Triggers:** Pipeline activates on every commit to feature branches
- **Container Build:** Uses Kaniko executor for secure, reproducible builds
- **Version Management:** Semantic versioning (major.minor format)
- **Artifact Preparation:** Creates deployable Docker images

### Continuous Deployment (CD) - Octopus Deploy

**Platform:** Self-hosted deployment orchestration
**Integration:** CLI-based triggers from Jenkins
**Deployment Strategy:** Environment-specific releases

#### CD Pipeline Features:
- **Release Management:** Automated release creation and versioning
- **Environment Promotion:** Development → Staging workflow
- **Rollback Capability:** One-click rollback to previous versions
- **Audit Trail:** Complete deployment history and tracking
- **Multi-environment:** Isolated deployments per environment

### Application Deployment - Kind Cluster

**Platform:** Kubernetes in Docker for local development
**Cluster Name:** `develop-cluster`
**Deployment Method:** Helm charts with GitOps integration

#### Deployment Features:
- **Local Kubernetes:** Full K8s environment without cloud costs
- **Helm Integration:** Declarative application deployment
- **Service Mesh:** Ingress and service configuration
- **Database:** Integrated MySQL with persistent storage
- **Monitoring:** Resource limits and health checks

## 📁 Repository Structure

```
py-ecommerce-k8s/
├── ecommerce/                 # Django application
│   ├── manage.py
│   ├── ecommerce/            # Django project settings
│   ├── eshop/                # Main application module
│   ├── static/               # Static assets (CSS, JS, Images)
│   └── templates/            # HTML templates
├── helm/                     # Kubernetes Helm charts
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── values-dev.yaml
│   └── templates/
├── .octopus/                 # Octopus Deploy configuration
│   ├── deployment_process.ocl
│   ├── variables.ocl
│   └── deployment_settings.ocl
├── Jenkinsfile               # CI/CD pipeline definition
├── Dockerfile                # Container build configuration
├── docker-compose.yml        # Local development setup
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🛠️ Development Setup

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- kubectl
- Helm 3.x
- Kind
- Git

### Local Development (SQLite)

1. **Clone and Setup Environment:**
   ```bash
   git clone <repository-url>
   cd py-ecommerce-k8s
   cp .env.example .env
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   cd ecommerce
   python manage.py migrate
   ```

4. **Start Development Server:**
   ```bash
   python manage.py runserver
   ```

### Docker Development (MySQL)

1. **Build and Run:**
   ```bash
   docker-compose up --build
   ```

2. **Run Migrations:**
   ```bash
   docker-compose exec web python ecommerce/manage.py migrate
   ```

### Kubernetes Development (Kind + Helm)

1. **Create Kind Cluster:**
   ```bash
   kind create cluster --name develop-cluster
   ```

2. **Deploy Application:**
   ```bash
   cd helm
   helm install ecommerce . -f values-dev.yaml
   ```

3. **Access Application:**
   ```bash
   kubectl get svc
   kubectl port-forward svc/ecommerce 8000:80
   ```

## 🔄 CI/CD Workflow

### Branching Strategy
- `main`: Production-ready code
- `feature/*`: Feature development branches
- `helm`: Infrastructure-as-Code branch

### Pipeline Execution Flow

1. **Code Commit** (Feature Branch)
   - Developer pushes code to feature branch
   - Webhook triggers CloudBees pipeline

2. **CI Build Process** (CloudBees)
   ```bash
   # Build triggered automatically on commit
   # Uses Kaniko for container build
   # Creates versioned image: sample-app:1.2
   ```

3. **Image Deployment** (Kind Cluster)
   ```bash
   # Load image into Kind cluster
   kind load image-archive sample-app-1.2.tar --name develop-cluster
   ```

4. **Infrastructure Update** (GitOps)
   ```bash
   # Update Helm values in separate branch
   git checkout helm
   sed -i 's/tag:.*/tag: "1.2"/' values.yaml
   git commit -m "chore: update image tag to 1.2"
   git push origin helm
   ```

5. **Release Creation** (Octopus CLI)
   ```bash
   # Create new release via CLI
   octopus release create --project e-commerce --version 1.2
   ```

6. **Application Deployment** (Octopus)
   ```bash
   # Deploy to development environment
   octopus release deploy --project e-commerce --version 1.2 --environment Development
   ```

## ⚙️ Configuration

### Environment Variables

#### Django Application
```bash
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=mysql://user:password@db:3306/ecommerce_db
```

#### CI/CD Pipeline
```bash
# CloudBees/Jenkins Configuration
APP_NAME=sample-app
KIND_CLUSTER=develop-cluster
BUILD_AGENT=linux-agent-170

# Octopus Deploy Configuration
OCTOPUS_SERVER=http://10.10.5.170:8080
OCTOPUS_SPACE=Default
OCTOPUS_PROJECT=e-commerce
OCTOPUS_ENV=Development
OCTOPUS_API_KEY=your-api-key
```

### Infrastructure Configuration

#### Helm Values (Development)
```yaml
image:
  repository: sample-app
  tag: "1.2"
  pullPolicy: Never

django:
  DEBUG: "True"
  ALLOWED_HOSTS: "sample.dev.local,localhost,127.0.0.1"
  DATABASE_URL: "mysql://django_user:django_password@db:3306/ecommerce_project"

ingress:
  enabled: true
  host: sample.dev.local

mysql:
  enabled: true
  database: ecommerce_project
  user: django_user
  password: django_password
```

## 🔧 Troubleshooting

### Common CI/CD Issues

#### Pipeline Not Triggering
```bash
# Check webhook configuration in CloudBees
# Verify branch patterns in Jenkinsfile
# Confirm Git repository connectivity
```

#### Kaniko Build Failures
```bash
# Verify Dockerfile syntax
# Check Kaniko executor permissions
# Ensure base images are accessible
```

#### Octopus Connection Issues
```bash
# Test Octopus server connectivity
octopus server --server $OCTOPUS_SERVER --api-key $OCTOPUS_API_KEY

# Verify project and environment exist
octopus project list
octopus environment list
```

#### Kind Cluster Problems
```bash
# Check cluster status
kind get clusters

# Verify kubectl context
kubectl cluster-info
kubectl get nodes

# Check pod status
kubectl get pods -n dev
kubectl describe pod <pod-name> -n dev
```

#### Helm Deployment Issues
```bash
# Validate chart syntax
helm template ecommerce . -f values-dev.yaml

# Check release status
helm list -n dev
helm status ecommerce -n dev

# View detailed logs
kubectl logs <pod-name> -n dev
```

### Database Issues
```bash
# Check MySQL pod status
kubectl get pods -n dev | grep mysql

# Connect to database
kubectl exec -it <mysql-pod> -n dev -- mysql -u django_user -p ecommerce_project
```

## 📊 Monitoring & Logging

### Application Logs
```bash
# View application logs
kubectl logs -f <app-pod> -n dev

# View MySQL logs
kubectl logs -f <mysql-pod> -n dev
```

### Pipeline Monitoring
- **CloudBees:** Pipeline execution history and logs
- **Octopus:** Deployment dashboard and audit trail
- **Kubernetes:** Pod status, resource usage, and events

## 🤝 Contributing

1. Create a feature branch from `develop`
2. Make your changes and test locally
3. Push to your feature branch to trigger CI
4. Create a pull request to `develop`
5. After review, merge to trigger full pipeline

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🖼️ Screenshots

![Home Page](./HomePage.png)

---

**Note:** This documentation is maintained as part of the CI/CD pipeline. Updates to the README should follow the established Git workflow to ensure proper version control and deployment.
