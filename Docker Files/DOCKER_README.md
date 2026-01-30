# Docker Quick Start

One-command deployment with Docker.

## Quick Deploy

```bash
docker-compose up -d
```

Access at: `http://localhost:8501`

## Files

- `Dockerfile` - Production container
- `docker-compose.yml` - Orchestration
- `.dockerignore` - Build optimization
- `DOCKER_DEPLOYMENT.md` - Complete guide

## Verify Integration

```bash
bash verify-docker.sh
```

## Stop

```bash
docker-compose down
```

## Full Documentation

See `DOCKER_DEPLOYMENT.md` for:
- Production deployment
- Kubernetes setup
- Security configuration
- Monitoring and troubleshooting
