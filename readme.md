# Testing HuggingFace models API
## Install API in local env

Python env:

    python3 -m venv myenv
    source myenv/bin/activate

Navigate to repo's root folder and:
    
    pip install -r requirements.txt

Run server:

    uvicorn app.main:app
    // options: CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]

## Run server with docker-compose (recommended)

Build image

    docker build . -t hugging-api

Deploy with docker-compose up

    docker network create test_network
    docker-compose up -d


