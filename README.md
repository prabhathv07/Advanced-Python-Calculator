# Docker + Python QR Code Generator

## Project Overview

A Dockerized Python application that generates QR codes linking to GitHub profiles.

## Features

- Generates QR code PNG files
- Customizable via environment variables
- Docker container support

## QR Code Output

![My GitHub QR Code](qr_codes/github_qr.png)
_Scan this QR code to visit [my GitHub profile](https://github.com/prabhathv07)_

## Usage

### Docker Commands

```bash
# Build the image
docker build -t my-qr-app .

# Run with default settings
docker run -d --name qr-generator -v $(pwd)/qr_codes:/app/qr_codes my-qr-app

# Run with custom settings
docker run -d --name qr-generator \
  -e QR_DATA_URL='https://github.com/prabhathv07' \
  -e QR_CODE_FILENAME='custom_qr.png' \
  -v $(pwd)/qr_codes:/app/qr_codes \
  my-qr-app
```

### Docker Logs

![Docker Logs](docker_logs.png)
_Example output from `docker logs qr-generator`_

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest --cov=main

# Generate coverage report
pytest --cov=main --cov-report=html
```
