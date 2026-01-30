# Docker Deployment Guide - NER-Aegis AI

Complete guide for containerized deployment of NER-Aegis AI.

---

## Quick Start

### Using Docker Compose (Recommended)

```bash
# Build and start the application
docker-compose up -d

# Access the application
open http://localhost:8501
```

That's it! The application is now running in a container.

---

## Prerequisites

- Docker Engine 20.10+ ([Install Docker](https://docs.docker.com/get-docker/))
- Docker Compose 2.0+ (included with Docker Desktop)
- 2GB RAM minimum
- 1GB disk space

---

## Deployment Options

### Option 1: Docker Compose (Recommended for Production)

**Build and Start:**
```bash
docker-compose up -d
```

**View Logs:**
```bash
docker-compose logs -f
```

**Stop:**
```bash
docker-compose down
```

**Rebuild:**
```bash
docker-compose up -d --build
```

### Option 2: Docker CLI

**Build Image:**
```bash
docker build -t ner-aegis-ai:latest .
```

**Run Container:**
```bash
docker run -d \
  --name ner-aegis-ai \
  -p 8501:8501 \
  --restart unless-stopped \
  ner-aegis-ai:latest
```

**View Logs:**
```bash
docker logs -f ner-aegis-ai
```

**Stop Container:**
```bash
docker stop ner-aegis-ai
docker rm ner-aegis-ai
```

---

## Configuration

### Environment Variables

Edit `docker-compose.yml` to customize:

```yaml
environment:
  - STREAMLIT_SERVER_PORT=8501        # Port number
  - STREAMLIT_SERVER_ADDRESS=0.0.0.0  # Listen address
  - STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### Port Mapping

Change port in `docker-compose.yml`:

```yaml
ports:
  - "8080:8501"  # Access on port 8080 instead
```

### Data Persistence

Data is stored in Docker volumes:
- `aegis-data` - Application data
- `aegis-logs` - Application logs

**Backup Volumes:**
```bash
docker run --rm \
  -v aegis-data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/aegis-data-backup.tar.gz /data
```

**Restore Volumes:**
```bash
docker run --rm \
  -v aegis-data:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/aegis-data-backup.tar.gz -C /
```

---

## Production Deployment

### With Reverse Proxy (Nginx)

**nginx.conf:**
```nginx
server {
    listen 80;
    server_name ner-aegis.example.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### With SSL/TLS (Let's Encrypt)

```bash
# Install certbot
sudo apt-get install certbot python3-certbot-nginx

# Obtain certificate
sudo certbot --nginx -d ner-aegis.example.com

# Auto-renewal is configured automatically
```

### Docker Swarm Deployment

**Create swarm:**
```bash
docker swarm init
```

**Deploy stack:**
```bash
docker stack deploy -c docker-compose.yml ner-aegis
```

**Scale service:**
```bash
docker service scale ner-aegis_ner-aegis-ai=3
```

### Kubernetes Deployment

**deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ner-aegis-ai
spec:
  replicas: 2
  selector:
    matchLabels:
      app: ner-aegis-ai
  template:
    metadata:
      labels:
        app: ner-aegis-ai
    spec:
      containers:
      - name: ner-aegis-ai
        image: ner-aegis-ai:latest
        ports:
        - containerPort: 8501
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
---
apiVersion: v1
kind: Service
metadata:
  name: ner-aegis-ai
spec:
  selector:
    app: ner-aegis-ai
  ports:
  - port: 80
    targetPort: 8501
  type: LoadBalancer
```

**Deploy:**
```bash
kubectl apply -f deployment.yaml
```

---

## Monitoring and Health Checks

### Health Check Endpoint

The container includes a health check:
```bash
curl http://localhost:8501/_stcore/health
```

### Container Status

```bash
# Docker Compose
docker-compose ps

# Docker CLI
docker ps
docker inspect ner-aegis-ai
```

### View Logs

```bash
# All logs
docker-compose logs

# Follow logs (live)
docker-compose logs -f

# Last 100 lines
docker-compose logs --tail=100

# Specific service
docker-compose logs -f ner-aegis-ai
```

### Resource Usage

```bash
# View resource stats
docker stats ner-aegis-ai

# Detailed inspection
docker inspect ner-aegis-ai | grep -A 10 Memory
```

---

## Troubleshooting

### Container Won't Start

**Check logs:**
```bash
docker-compose logs
```

**Common issues:**
- Port 8501 already in use: Change port mapping
- Insufficient memory: Increase Docker memory limit
- Build errors: Run `docker-compose build --no-cache`

### Application Not Accessible

**Verify container is running:**
```bash
docker-compose ps
```

**Check port mapping:**
```bash
docker port ner-aegis-ai
```

**Test health check:**
```bash
curl http://localhost:8501/_stcore/health
```

### Performance Issues

**Increase resources in docker-compose.yml:**
```yaml
deploy:
  resources:
    limits:
      cpus: '2'
      memory: 2G
    reservations:
      cpus: '1'
      memory: 1G
```

### Data Persistence Issues

**List volumes:**
```bash
docker volume ls
```

**Inspect volume:**
```bash
docker volume inspect aegis-data
```

**Clear volumes (CAUTION: Deletes data):**
```bash
docker-compose down -v
```

---

## Security Best Practices

### 1. Non-Root User
Container runs as non-root user `aegis` (already configured).

### 2. Network Isolation
Use Docker networks to isolate containers:
```yaml
networks:
  aegis-network:
    driver: bridge
    internal: true  # No external access
```

### 3. Read-Only Filesystem
Add to docker-compose.yml:
```yaml
security_opt:
  - no-new-privileges:true
read_only: true
tmpfs:
  - /tmp
  - /app/.streamlit
```

### 4. Resource Limits
Always set memory and CPU limits:
```yaml
deploy:
  resources:
    limits:
      memory: 1G
      cpus: '1'
```

### 5. Scan for Vulnerabilities
```bash
# Scan image
docker scan ner-aegis-ai:latest

# Or use Trivy
trivy image ner-aegis-ai:latest
```

---

## CI/CD Integration

### GitHub Actions

**.github/workflows/docker.yml:**
```yaml
name: Docker Build and Push

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build Docker image
        run: docker build -t ner-aegis-ai:latest .
      
      - name: Run tests
        run: docker run ner-aegis-ai:latest python test_compatibility.py
      
      - name: Push to registry
        run: |
          echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
          docker tag ner-aegis-ai:latest user/ner-aegis-ai:latest
          docker push user/ner-aegis-ai:latest
```

---

## Updating the Application

### Update Code

```bash
# Pull latest changes
git pull

# Rebuild and restart
docker-compose up -d --build
```

### Update Base Image

```bash
# Pull latest base image
docker-compose pull

# Rebuild
docker-compose up -d --build
```

---

## Cleanup

### Remove Containers

```bash
# Stop and remove
docker-compose down

# Remove with volumes (CAUTION: Deletes data)
docker-compose down -v
```

### Remove Images

```bash
# Remove specific image
docker rmi ner-aegis-ai:latest

# Remove all unused images
docker image prune -a
```

### Clean System

```bash
# Remove all unused containers, networks, images
docker system prune -a

# Include volumes (CAUTION)
docker system prune -a --volumes
```

---

## Appendix: Complete Commands Reference

### Build and Deploy
```bash
docker-compose up -d              # Start
docker-compose up -d --build      # Rebuild and start
docker-compose down               # Stop
docker-compose restart            # Restart
```

### Monitoring
```bash
docker-compose ps                 # Status
docker-compose logs -f            # Logs
docker stats                      # Resources
```

### Maintenance
```bash
docker-compose pull               # Update images
docker system prune               # Cleanup
docker volume ls                  # List volumes
```

### Debugging
```bash
docker-compose exec ner-aegis-ai /bin/bash  # Shell access
docker-compose logs --tail=100              # Recent logs
docker inspect ner-aegis-ai                 # Detailed info
```

---

**Last Updated:** January 30, 2026  
**Docker Version:** 24.0+  
**Compose Version:** 2.0+
