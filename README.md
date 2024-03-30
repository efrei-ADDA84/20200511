# 20200511
Repository of SENECHAL-Morgan-M1-APP-BDML

DEVOPS - TP1
Docker

lien docker hub : https://hub.docker.com

Objectifs:  
-Crée un repository Github avec pour nom votre identifiant EFREI
-Créer un wrapper qui retourne la météo d'un lieu donné avec sa latitude et sa longitude (passées en variable d'environnement) en utilisant openwheather API dans le langage de programmation de votre choix (bash, python, go, nodejs, etc)
-Packager son code dans une image docker 
-Mettre à disposition son image sur DockerHug 
-Mettre à disposition son code dans un repository Github

Livrables:
-URL repository Github publique (avec Dockerfile et le wrapper)
-URL registry DockerHub publique
-Rapport qui présente, étape par étape, les choix techniques, les commandes utilisées et les
-difficultées rencontrées si vous n'avez pas pu aller jusqu'au bout.

Notation:
-Code disponible sur Github
-Dockerfile qui build
-Docker image disponible sur DockerHub
-API qui renvoie la météo en utilisant la commande suivante en utilisant votre image :
-docker run --env LAT="31.2504"--env LONG="-99.2506"--env API_KEY=****maregistry/api:1.0.0 : Fait -> docker run --rm -e OPENWEATHER_API_KEY=b022acb509eacae0875ded1afe41a527 -e LATITUDE=31.2504 -e LONGITUDE=99.2506 monappweather

Bonus:
-0 CVE (trivy) trivy image maregistry/api:1.0.0: Fait: 0 critical donc Validé 
-0 lint errors on Dockerfile (hadolint) docker run --rm -i hadolint/hadolint < Dockerfile : Fait : No Error : Validé
-Aucune données sensibles stockées dans l'image (i.e: openweather API key) : Fait : Validé



git add . 
git commit -m "Commit du Tp1"
git push 

