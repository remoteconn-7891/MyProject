# Arborfindr Project

Welcome to the Arborfindr project! This project uses Django and Solr for managing and searching arborist data. Below you will find instructions on how to clone the project, set up a virtual environment, install requirements, and run the project using Docker.

## Table of Contents

1. [Cloning the Project](#cloning-the-project)
2. [Creating a Virtual Environment](#creating-a-virtual-environment)
3. [Activating the Virtual Environment](#activating-the-virtual-environment)
4. [Installing Requirements](#installing-requirements)
5. [Running Solr](#running-solr)
6. [Running Docker Compose](#running-docker-compose)

## Cloning the Project

To clone this project, run the following command in your terminal:

```bash
git clone git@github.com:remoteconn-7891/MyProject.git
cd arborfindr
```

## Creating a Virtual Environment

To create a virtual environment, use the following command:

```bash
# For Windows
python -m venv .venv
```


```bash
# For Linux or macOS
python3 -m venv .venv
```

## Activating the Virtual Environment

### Windows

Activate the virtual environment with the following command:

```bash
.\.venv\Scripts\activate
```

### Linux or macOS

Activate the virtual environment with the following command:

```bash
source .venv/bin/activate
```

## Installing Requirements

Once the virtual environment is activated, install the required packages using:

```bash
pip install -r requirements.txt
```

## Running Solr

### Windows

1. Open a new Command Prompt or PowerShell window.
2. Navigate to your Solr installation directory and start Solr:

```bash
solr start
```

3. Open your web browser and go to `http://localhost:8983/solr`.

### Linux

1. Open a terminal window.
2. Navigate to your Solr installation directory and start Solr:

```bash
solr start
```

3. Open your web browser and go to `http://localhost:8983/solr`.

## Running Docker Compose

To run the project using Docker, execute the following commands in your terminal:

1. Build and start the Docker containers:

```bash
docker-compose up --build
```

2. After building, the services will start automatically. You can access the web application at `http://localhost:8000`.

3. If you need to stop the services, you can do so with:

```bash
docker-compose down
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
