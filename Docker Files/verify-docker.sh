#!/bin/bash
# verify-docker.sh - Quick Docker integration test
# Run this to verify Docker files work with your repository

set -e  # Exit on any error

echo "========================================"
echo "  NER-Aegis AI - Docker Verification"
echo "========================================"
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test 1: Check required files
echo "Test 1: Checking required files..."
files=("Dockerfile" "docker-compose.yml" ".dockerignore" "app.py" "requirements.txt" "logic/__init__.py")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $file exists"
    else
        echo -e "${RED}✗${NC} $file missing"
        exit 1
    fi
done
echo ""

# Test 2: Validate Dockerfile syntax
echo "Test 2: Validating Dockerfile..."
if docker build --no-cache -t ner-aegis-ai:test . > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Dockerfile builds successfully"
else
    echo -e "${RED}✗${NC} Dockerfile build failed"
    echo "Run 'docker build -t ner-aegis-ai:test .' to see errors"
    exit 1
fi
echo ""

# Test 3: Test docker-compose syntax
echo "Test 3: Validating docker-compose.yml..."
if docker-compose config > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} docker-compose.yml is valid"
else
    echo -e "${RED}✗${NC} docker-compose.yml has errors"
    exit 1
fi
echo ""

# Test 4: Start container
echo "Test 4: Starting container..."
if docker-compose up -d > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Container started"
else
    echo -e "${RED}✗${NC} Container failed to start"
    docker-compose logs
    exit 1
fi
echo ""

# Wait for container to be ready
echo "Waiting for application to be ready (30 seconds)..."
sleep 30

# Test 5: Health check
echo "Test 5: Checking application health..."
if curl -f -s http://localhost:8501/_stcore/health > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Health check passed"
else
    echo -e "${YELLOW}!${NC} Health check failed (this is okay if Streamlit endpoint differs)"
fi
echo ""

# Test 6: Check if app is accessible
echo "Test 6: Checking application accessibility..."
if curl -f -s http://localhost:8501 > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Application is accessible on port 8501"
else
    echo -e "${RED}✗${NC} Application not accessible"
    docker-compose logs
    exit 1
fi
echo ""

# Test 7: Test Python imports in container
echo "Test 7: Testing Python imports..."
if docker-compose exec -T ner-aegis-ai python -c "from logic import risk_engine, evacuation_planner, alert_engine; print('Success')" > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} All Python modules import successfully"
else
    echo -e "${RED}✗${NC} Python import errors"
    docker-compose exec -T ner-aegis-ai python -c "from logic import risk_engine, evacuation_planner, alert_engine"
    exit 1
fi
echo ""

# Test 8: Test core functionality
echo "Test 8: Testing core functionality..."
if docker-compose exec -T ner-aegis-ai python -c "
from logic.risk_engine import compute_risk_score
score = compute_risk_score(300, 40, 60, 15, 10)
assert 0 <= score <= 100, 'Invalid risk score'
print('Risk calculation works')
" > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Core functionality works"
else
    echo -e "${RED}✗${NC} Core functionality failed"
    exit 1
fi
echo ""

# Cleanup
echo "Cleaning up..."
docker-compose down > /dev/null 2>&1
echo -e "${GREEN}✓${NC} Cleanup complete"
echo ""

# Summary
echo "========================================"
echo -e "${GREEN}  ALL TESTS PASSED!${NC}"
echo "========================================"
echo ""
echo "Docker integration is working correctly."
echo "You can now:"
echo "  • Push to GitHub with confidence"
echo "  • Deploy with: docker-compose up -d"
echo "  • Access at: http://localhost:8501"
echo ""
echo "For detailed deployment instructions, see:"
echo "  DOCKER_DEPLOYMENT.md"
echo ""
