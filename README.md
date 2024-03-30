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

## Report

Introduction:

Dans le cadre de l'approfondissement des compétences en DevOps, ce travail pratique numero 1 vise à illustrer l'intégration continue et le déploiement continu (CI/CD) en utilisant des outils modernes et des pratiques innovantes. L'objectif est de créer une application simple mais fonctionnelle qui interroge l'API OpenWeather pour obtenir des informations météorologiques basées sur des coordonnées géographiques fournies. Ce processus comprend la création d'un répertoire GitHub personnalisé, le développement d'un wrapper dans le langage de programmation de notre choix, et l'encapsulation de l'application dans une image Docker pour assurer la portabilité et la facilité de déploiement. Enfin, cette image sera publiée sur DockerHub, rendant notre travail accessible et réutilisable par la communauté. Ce projet met en lumière l'importance de l'automatisation et des bonnes pratiques de développement dans le paysage technologique actuel, soulignant l'essence même des principes DevOps.

Architecture: 

Pour répondre au besoin de ce projet, j'ai décidé d'utilisé l'architecture ci dessous: 

![Texte alternatif](images/General-Shape.png)

"my_env": Cette espace nous permet de crée un environement virtuel nous permettant d'y ajouter toutes les library nécéssaire pour notre application.

"src": Cette espace est utilisé pour stocké notre script python "main.py" contenant le wrapper de notre application.

"Dockerfile": Ce script docker nous permet d'inséré toutes les instructions pour construire notre image Docker, y compris la base de l'image python, l'installation des dépendances à partir de notre "requirements.txt", et la commande pour exécutert notre script python. 

"requirements": Ce fichier text nous permet d'ajouté tout les dépendances nécéssaires à notre application.

Code: 

Wrapper:

Ce script Python sert de wrapper pour l'API OpenWeather. Il permet de récupérer les informations météorologiques actuelles pour une localisation spécifiée par latitude et longitude.
 
Importation des modules

```python
import os
import requests


Test:

Conclusion:










