## 🧱 PARTIE 1 — DOCKER : API + SITE WEB


Objectif : Comprendre les bases de la conteneurisation. Nous allons créer manuellement deux images Docker distinctes (une pour le backend en Python, une pour le frontend en PHP), les construire, et les lancer indépendamment en les connectant via un réseau Docker personnalisé. C'est l'approche fondamentale pour comprendre comment Docker isole les processus.

### 🔹 Étape 1 : Préparer l’arborescence


# Créer les dossiers pour l'API (product-service) et le site web (simplesite)
mkdir -p ~/docker-tp/product-service
mkdir -p ~/docker-tp/simplesite

# Se déplacer dans le répertoire de travail
cd ~/docker-tp


### 🔹 Étape 2 : Construire l’image API Python


# Construire l'image Docker nommée 'product-service-image'
# Le point '.' ou 'product-service' indique le contexte de construction (où se trouve le Dockerfile)
docker build -t product-service-image product-service


### 🔹 Étape 3 : Lancer l’API Python


# Lancer le conteneur en mode détaché (-d)
# Nommer le conteneur 'product-service'
# Connecter au réseau 'reseau' et mapper le port 82 de l'hôte vers 82 du conteneur
docker run -d --name product-service --network reseau -p 82:82 product-service-image


### 🔹 Étape 4 : Tester l’API


# Envoyer une requête HTTP pour vérifier que l'API répond
curl http://localhost:82/products


### 🔹 Étape 5 : Construire l’image du site PHP


# Construire l'image Docker pour le site web PHP
docker build -t simplesite-image simplesite


### 🔹 Étape 6 : Lancer le site web PHP


# Lancer le site web sur le port 8080 (mappé vers le port 80 interne)
# Le connecter au même réseau que l'API pour qu'ils puissent communiquer
docker run -d --name site --network reseau -p 8080:80 simplesite-image


## 🧱 PARTIE 2 — DOCKER COMPOSE


Objectif : Simplifier le lancement d'applications multi-conteneurs. Au lieu de taper plusieurs commandes docker run manuelles et de gérer le réseau à la main, nous utilisons un fichier docker-compose.yml. Ce fichier définit toute l'infrastructure (services, volumes, réseaux) et permet de tout lancer en une seule commande. C'est l'outil idéal pour les environnements de développement.

### 🔹 Étape 7 : Créer le fichier docker-compose.yml


version: '3'
services:
  product-service:
    build: ./product-service       # Chemin vers le Dockerfile de l'API
    volumes:
      - ./product-service:/usr/src/app # Montage du code en temps réel (Hot Reload)
    ports:
      - "5001:82"                  # Exposition sur le port 5001 de l'hôte

  website:
    image: php:apache              # Utilisation d'une image officielle PHP/Apache
    volumes:
      - ./simplesite:/var/www/html # Montage du code source PHP
    ports:
      - "5002:80"                  # Accessible via http://localhost:5002
    depends_on:
      - product-service            # S'assure que l'API démarre avant le site


### 🔹 Étape 8 : Lancer le projet


# Démarrer tous les services définis dans le fichier compose
# --build : Reconstruit les images si le code a changé
# -d : Mode détaché (arrière-plan)
docker-compose up --build -d


### 🔹 Étape 9 : Arrêter tout


# Arrêter les conteneurs et supprimer les réseaux créés par compose
docker-compose down


## 🧱 PARTIE 3 — KUBERNETES : Commandes kubectl


Objectif : Découvrir l'orchestration de conteneurs à grande échelle avec Kubernetes (k8s). Contrairement à Docker Compose qui gère des conteneurs sur une seule machine, Kubernetes gère des Pods (groupe de conteneurs) répartis sur un cluster. Ici, nous utilisons l'approche impérative (lignes de commande directes) pour créer, scaler (augmenter le nombre d'instances) et exposer une application Nginx.

### 🔹 Étape 10 : Créer un Deployment simple


# Créer un déploiement nommé 'hello-nginx' basé sur l'image 'nginx'
kubectl create deployment hello-nginx --image=nginx


### 🔹 Étape 11 : Scaler le Deployment


# Augmenter le nombre de répliques (pods) à 3 pour la haute disponibilité
kubectl scale deployment hello-nginx --replicas=3


### 🔹 Étape 12 : Exposer le Deployment


# Créer un Service pour rendre le déploiement accessible
# Type NodePort : Ouvre un port sur le nœud du cluster
kubectl expose deployment hello-nginx --port=80 --type=NodePort


### 🔹 Étape 13 : Obtenir l’URL (Minikube)


# Obtenir l'URL d'accès au service via Minikube
minikube service hello-nginx


### 🔹 Étape 14 : Vérifier les ressources Kubernetes


# Lister tous les Pods, Deployments et Services
kubectl get pods
kubectl get deployments
kubectl get svc


### 🔹 Étape 15 : Supprimer Deployment + Service


# Nettoyer les ressources créées manuellement
kubectl delete deployment hello-nginx
kubectl delete service hello-nginx


## 🧱 PARTIE 4 — KUBERNETES YAML


Objectif : Passer à l'approche déclarative (Infrastructure as Code), qui est la bonne pratique en production. Au lieu de taper des commandes, nous décrivons l'état souhaité du système dans un fichier YAML. Si le fichier change, on "applique" simplement les changements, et Kubernetes se charge de faire converger l'état actuel vers l'état désiré (exemple : maintenir toujours 4 pods actifs).

### 🔹 Étape 16 : Créer le fichier nginx.yaml


apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-yaml          # Nom de la ressource Deployment
spec:
  replicas: 4               # On demande 4 pods identiques
  selector:
    matchLabels:
      app: nginx-yaml       # Le déploiement gère les pods avec ce label
  template:
    metadata:
      labels:
        app: nginx-yaml     # Label appliqué à chaque pod
    spec:
      containers:
        - name: nginx       # Nom du conteneur
          image: nginx      # Image à utiliser
          ports:
            - containerPort: 80 # Port exposé par le conteneur


### 🔹 Étape 17 : Appliquer le fichier YAML


# Créer ou mettre à jour les ressources définies dans le fichier YAML
kubectl apply -f nginx.yaml


### 🔹 Étape 18 : Vérifier les pods


# Vérifier que les 4 pods sont bien en cours d'exécution
kubectl get pods
kubectl get deployments


### 🔹 Étape 19 : Exposer ce Deployment YAML


# Exposer le déploiement 'nginx-yaml' sur le port 80 via NodePort
kubectl expose deployment nginx-yaml --port=80 --type=NodePort


### 🔹 Étape 20 : Obtenir l’URL (Minikube)


# Ouvrir le service dans le navigateur (commande spécifique à Minikube)
minikube service nginx-yaml


### 🔹 Étape 21 : Supprimer les ressources YAML


# Supprimer toutes les ressources définies dans le fichier (Deployment)
kubectl delete -f nginx.yaml
