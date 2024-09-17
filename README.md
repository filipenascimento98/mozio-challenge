# Challenge Greenole

This API allows for background storage of measurement data that would otherwise originate from sensors.

# Technologies
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Postgis](https://postgis.net)
- Unitary Tests

# Installation

To access the API, first, clone this repository.
```bash
git clone https://github.com/filipenascimento98/mozio-challenge.git
```

# How to use
This project depends on [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/). With the dependencies resolved, navigate to the project directory that contains the __docker_compose.yml__ file and run the following command that will build and deploy the application:
```bash
docker-compose up -d --build
```
Thus, the application will run in a Docker container.

# Endpoints
For more details, you can consult the documentation for this API on the endpoint:
```bash
https://mozio-api.52.7.144.97.nip.io/api/doc/
```

# Project structure
A brief explanation of some structural elements of this project.
* api: Only app in this project.
    * views: Contains the files in which the views called by the defined routes.
    * serializers: Directory that stores the serializers that are responsible for validating the input data of each route.
    * tests: Directory that stores automated tests.

# Automated Tests
To run the automated tests navigate to the directory where the __manage.py__ file is located and execute the following command if you are running without container:
```bash
python manage.py test
```
If you running in container execute the test inside the container. To enter in container and execute the tests:
```bash
docker exec -it <container-name> /bin/bash
python manage.py test
```