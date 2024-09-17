# Mozio Challenge

This API create, update, delete and retrieves geo information about providers and their service areas.

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

# How to access
The API can be accessed via the base url:
```bash
https://mozio-api.52.7.144.97.nip.io/api/
```
Their endpoints can be accessed through the documentation mentioned above.
## Collection to use on Postman
 A collection to be used on postman is avaiable on https://drive.google.com/file/d/1_Va-XlvgK4faIRbLWBv2-gOlhJ5le86D/view?usp=sharing . Remember to change the collection variables to use the API local or online. For default, the variables are set to local API.

# Project structure
A brief explanation of some structural elements of this project.
* api: Only app in this project.
    * views: Contains the files in which the views called by the defined routes.
    * serializers: Directory that stores the serializers that are responsible for validating the input data of each route.
    * tests: Directory that stores automated tests.

# PEP8
To comply with PEP8, the [flake8](https://flake8.pycqa.org/en/latest/#) library was used, which indicates the adjustments that must be made. The lines are up to 120 characters long, a value that was set as a limit in the challenge description.

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