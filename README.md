# 20200511
Repository of SENECHAL-Morgan-M1-APP-BDML

# DEVOPS - TP1: Docker

## Objectives
- Create a GitHub repository named after your EFREI identifier.
- Develop a wrapper that retrieves the weather for a given location using its latitude and longitude (passed as environment variables), utilizing the OpenWeather API. You may use the programming language of your choice (bash, python, go, nodejs, etc.).
- Package your code in a Docker image.
- Publish your Docker image on DockerHub.
- Make your code accessible in a GitHub repository.

## Deliverables

1. Public GitHub repository URL containing the Dockerfile and wrapper code.
2. Public DockerHub registry URL where your Docker image is hosted.
3. A report detailing your technical choices, commands used, and challenges faced if the task wasn't completed. This report should be emailed no later than 48 hours after the TP ends to the professor's email with the subject: `[TP1-DEVOPS] LAST NAME FIRST NAME`.

## Grading Criteria

- Code availability on GitHub.
- A Dockerfile that successfully builds.
- Docker image availability on DockerHub.
- Functionality of the API, verifiable by running the following command with your Docker image:

docker run --env LAT="31.2504" --env LONG="-99.2506" --env API_KEY=****yourregistry/api:1.0.0


## Bonus Points

Earn bonus points for:

- No CVEs (Common Vulnerabilities and Exposures) as reported by `trivy`:

trivy image yourregistry/api:1.0.0

- No lint errors in the Dockerfile as reported by `hadolint`:

docker run --rm -i hadolint/hadolint < Dockerfile

- Ensuring no sensitive data (e.g., OpenWeather API key) is stored within the image.

# DevOps Skills Enhancement Project - CI/CD with OpenWeather API

## Introduction

In the quest to deepen DevOps skills, Practical Work #1 aims to showcase Continuous Integration and Continuous Deployment (CI/CD) using modern tools and innovative practices. The goal is to develop a simple yet functional application that queries the OpenWeather API for weather information based on provided geographical coordinates. This process includes creating a custom GitHub repository, developing a wrapper in the programming language of our choice, and encapsulating the application in a Docker image to ensure portability and ease of deployment. Finally, this image will be published on DockerHub, making our work accessible and reusable by the community. This project highlights the significance of automation and good development practices in today's tech landscape, underscoring the core principles of DevOps.

## Architecture

To meet the project's requirements, the following architecture has been employed:

### Components

- **`my_env`**: A virtual environment to include all necessary libraries for our application.
- **`src`**: The space used to store our Python script `main.py`, containing our application's wrapper.
- **`Dockerfile`**: This Docker script contains all the instructions to build our Docker image, including the base image of Python, installing dependencies from our `requirements.txt`, and the command to execute our Python script.
- **`requirements`**: A text file to list all the necessary dependencies for our application.

### Diagram

Below is the general structure of our project's architecture:

![Alternative Text](images/General-Shape.png)

## Implementation Steps

1. **Environment Setup**: Create the `my_env` virtual environment and install necessary libraries.
2. **Application Development**: Develop the `main.py` script in the `src` directory to interact with the OpenWeather API.
3. **Dockerization**: Use the `Dockerfile` to containerize the application, ensuring it includes the Python base image, installs dependencies, and specifies the command to run the script.
4. **Deployment**: Publish the Docker image to DockerHub for community access and reuse.

Code: 

Wrapper:

Ce script Python sert de wrapper pour l'API OpenWeather. Il permet de récupérer les informations météorologiques actuelles pour une localisation spécifiée par latitude et longitude.
 
Importation des modules

```python
import os
import requests
```

os : Ce module fournit une manière portable d'utiliser les fonctionnalités dépendantes du système d'exploitation, comme lire ou écrire dans des variables d'environnement.
requests : Un module externe qui facilite l'envoi de requêtes HTTP. Il est nécessaire de l'installer via pip.

Variables d'environnement

```python
LATITUDE = os.getenv('LATITUDE')
LONGITUDE = os.getenv('LONGITUDE')
API_KEY = os.getenv('OPENWEATHER_API_KEY')
```

Ces lignes récupèrent les valeurs des variables d'environnement pour la latitude, la longitude, et la clé API d'OpenWeather. Utiliser des variables d'environnement pour ces informations sensibles aide à sécuriser le code.

URL de base de l'API

```python
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
```

Définit l'URL de base pour accéder à l'API météo d'OpenWeather.

Fonction get_weather

```python
def get_weather(latitude, longitude, api_key):
```

Cette fonction fait la requête à l'API OpenWeather pour obtenir les données météorologiques basées sur la latitude et la longitude fournies.

Construction de la requête

```python
params = {
    'lat': latitude,
    'lon': longitude,
    'appid': api_key,
    'units': 'metric'  # ou 'imperial' pour Fahrenheit
}
response = requests.get(BASE_URL, params=params)
```
Les paramètres nécessaires pour la requête API sont définis, puis une requête GET est envoyée. units='metric' indique que la température sera en degrés Celsius.

Vérification de la réponse

```python
response.raise_for_status()
```

Cette méthode lève une exception si la requête échoue, permettant au script de gérer l'erreur plutôt que de continuer avec une réponse invalide.

Traitement de la réponse

```python
data = response.json()
weather_description = data['weather'][0]['description']
temperature = data['main']['temp']
city = data['name']
country = data['sys']['country']
print(f"La météo à {city}, {country} est : {weather_description} avec une température de {temperature}°C.")
```

Convertit la réponse en JSON, puis extrait et affiche la description de la météo, la température, le nom de la ville, et le code du pays.

Gestion des erreurs

```python
except requests.exceptions.HTTPError as err:
    print(f"Erreur lors de la récupération des données météo : {err}")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
```

Gère les éventuelles erreurs HTTP ou autres exceptions qui pourraient survenir pendant la requête.

Point d'entrée principal

```python
if __name__ == "__main__":
    if LATITUDE and LONGITUDE and API_KEY:
        get_weather(LATITUDE, LONGITUDE, API_KEY)
    else:
        print("Les variables d'environnement LATITUDE, LONGITUDE, et OPENWEATHER_API_KEY sont requises.")
```

Vérifie si les variables nécessaires sont définies avant d'exécuter la fonction get_weather. Si elles ne le sont pas, un message d'erreur est affiché.

Dockerfile:

Ce Dockerfile crée une image Docker pour notre application météo Python, en utilisant une image de base minimale pour réduire les vulnérabilités potentielles.

Image de base

```dockerfile
FROM python:3.9-alpine
```

python:3.9-alpine : Utilise une version légère d'une image Python basée sur Alpine Linux. Alpine est choisi pour sa petite taille et sa sécurité accrue.

Répertoire de travail

```dockerfile
WORKDIR /app
```

WORKDIR /app : Définit /app comme le répertoire de travail dans le conteneur. Les commandes qui suivent seront exécutées dans ce répertoire.

Installation des dépendances

```dockerfile
RUN apk add --no-cache build-base libffi-dev
```

apk add --no-cache build-base libffi-dev : Installe les paquets nécessaires pour compiler certaines dépendances Python. build-base inclut les outils de compilation, et libffi-dev est souvent requis pour les packages nécessitant des extensions C.

Installation des packages Python

```dockerfile
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
```

Copie requirements.txt dans le conteneur et installe les dépendances Python spécifiées. L'utilisation de --no-cache-dir aide à réduire la taille de l'image en évitant de stocker le cache de pip.

Copie du code source

```dockerfile
COPY src/ ./
```

Copie les fichiers du répertoire source src/ dans le répertoire de travail /app du conteneur. Cela inclut votre script Python et tout autre fichier nécessaire à l'exécution de votre application.

Variable d'environnement pour la clé API

```dockerfile
ENV OPENWEATHER_API_KEY=""
```

Définit une variable d'environnement OPENWEATHER_API_KEY qui sera utilisée par votre application. La valeur réelle de la clé API doit être fournie au runtime, garantissant que votre image Docker reste sécurisée.

Commande d'exécution

```dockerfile
CMD ["python", "./main.py"]
```

CMD ["python", "./main.py"] : Définit la commande par défaut pour exécuter l'application, lançant main.py avec Python. Cette commande est exécutée lorsque le conteneur démarre, sauf si une commande différente est spécifiée au démarrage du conteneur.

Test:

Wrapper:

Définition de LATITUDE et LONGITUDE

Pour configurer une application ou un script qui nécessite des variables d'environnement spécifiques, comme la latitude et la longitude pour notre application météo, nous pouvons les définir directement depuis notre terminal zsh. 

Input

```shell
export LATITUDE=48.8566
export LONGITUDE=2.3522
export OPENWEATHER_API_KEY=YOUR_KEY
```

Output

```shell
La météo à Paris, FR est : light rain avec une température de 8.66°C.
```

Les test pour notre wrapper fonctionne comme prévus.

Dockerfile:

Construire l'image Docker

Input

```shell
docker build -t monappweather:latest .
```

Output:

```shell
[+] Building 1.4s (12/12) FINISHED                                                                           docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                         0.0s
 => => transferring dockerfile: 812B                                                                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.9-alpine                                                         1.3s
 => [auth] library/python:pull token for registry-1.docker.io                                                                0.0s
 => [internal] load .dockerignore                                                                                            0.0s
 => => transferring context: 2B                                                                                              0.0s
 => [1/6] FROM docker.io/library/python:3.9-alpine@sha256:99161d2323b4130fed2d849dc8ba35274d1e1f35da170435627b21d305dad954   0.0s
 => [internal] load build context                                                                                            0.0s
 => => transferring context: 106B                                                                                            0.0s
 => CACHED [2/6] WORKDIR /app                                                                                                0.0s
 => CACHED [3/6] RUN apk add --no-cache build-base libffi-dev                                                                0.0s
 => CACHED [4/6] COPY requirements.txt ./                                                                                    0.0s
 => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt                                                          0.0s
 => CACHED [6/6] COPY src/ ./                                                                                                0.0s
 => exporting to image                                                                                                       0.0s
 => => exporting layers                                                                                                      0.0s
 => => writing image sha256:eb12932e8ad14e7fd2c29d78a58fb2903d2e394058a8f1899447892e26607dea                                 0.0s
 => => naming to docker.io/library/monappweather:latest                                                                      0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/poofijn3hkuosv7f0niyf7g3t

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview
```

Validation du Dockerfile et de l'image

Input

```shell
docker run --rm -i hadolint/hadolint < Dockerfile
```

Output:

```shell
-:8 DL3018 warning: Pin versions in apk add. Instead of `apk add <package>` use `apk add <package>=<version>`
```

Aucune erreur n'est rencontré concernant le : 0 lint errors on Dockerfile (hadolint) 

Scanner les vulnérabilités avec Trivy

Input

```shell
trivy image monappweather:latest
```

Output

```shell
2024-03-31T00:26:53.204+0100    INFO    Need to update DB
2024-03-31T00:26:53.204+0100    INFO    DB Repository: ghcr.io/aquasecurity/trivy-db:2
2024-03-31T00:26:53.204+0100    INFO    Downloading DB...
44.66 MiB / 44.66 MiB [-------------------------------------------------------------------------------] 100.00% 11.17 MiB p/s 4.2s
2024-03-31T00:26:58.860+0100    INFO    Vulnerability scanning is enabled
2024-03-31T00:26:58.860+0100    INFO    Secret scanning is enabled
2024-03-31T00:26:58.860+0100    INFO    If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2024-03-31T00:26:58.860+0100    INFO    Please see also https://aquasecurity.github.io/trivy/v0.50/docs/scanner/secret/#recommendation for faster secret detection
2024-03-31T00:26:58.891+0100    INFO    Detected OS: alpine
2024-03-31T00:26:58.891+0100    INFO    Detecting Alpine vulnerabilities...
2024-03-31T00:26:58.896+0100    INFO    Number of language-specific files: 1
2024-03-31T00:26:58.896+0100    INFO    Detecting python-pkg vulnerabilities...

monappweather:latest (alpine 3.19.1)

Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)

2024-03-31T00:26:58.898+0100    INFO    Table result includes only package filenames. Use '--format json' option to get the full path to the package file.

Python (python-pkg)

Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 1, HIGH: 1, CRITICAL: 0)

┌───────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────┐
│        Library        │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                          Title                           │
├───────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────┤
│ pip (METADATA)        │ CVE-2023-5752  │ MEDIUM   │ fixed  │ 23.0.1            │ 23.3          │ pip: Mercurial configuration injectable in repo revision │
│                       │                │          │        │                   │               │ when installing via pip                                  │
│                       │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2023-5752                │
├───────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────┤
│ setuptools (METADATA) │ CVE-2022-40897 │ HIGH     │        │ 58.1.0            │ 65.5.1        │ pypa-setuptools: Regular Expression Denial of Service    │
│                       │                │          │        │                   │               │ (ReDoS) in package_index.py                              │
│                       │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2022-40897               │
└───────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────┘
```

Concernant les vulnérabilité sur notre image selectionner "python:3.9-alpine", nous pouvons voir ici que nous avons aucune vulnérabilité de type critique: Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 1, HIGH: 1, CRITICAL: 0) : 


Exécuter le conteneur Docker

Input:

```shell
docker run --rm -e OPENWEATHER_API_KEY=b022acb509eacae0875ded1afe41a527 -e LATITUDE=31.2504 -e LONGITUDE=99.2506 monappweather  
```

Output:

```shell
La météo à Ganzi, CN est : overcast clouds avec une température de -2.91°C.
```

Publier l'image sur Docker Hub

Créer un compte sur Docker Hub

Link : https://hub.docker.com

Se connecter à Docker Hub depuis votre terminal

Input

```shell
docker login
```

Output

```shell
Authenticating with existing credentials...
Login Succeeded
```

Taguer l'image

```shell
docker tag monappweather:latest mgn94/monappweather:latest
```

Pousser l'image sur Docker Hub

```shell
docker push mgn94/monappweather:latest
```

Nous pouvons retrouvé notre image sur Docker Hub : https://hub.docker.com/repository/docker/mgn94/monappweather/general

Aucune donnée sensible dans l'image

Dans la réalisation de ce Tp1, nous avons pris des mesures pour nous assurer qu'aucune donnée sensible, comme notre clé API OpenWeather, ne soit stockée dans l'image Docker. C'est une bonne pratique de sécurité de s'assurer que toutes les données sensibles sont fournies via des variables d'environnement au moment de l'exécution du conteneur.

Conclusion:










