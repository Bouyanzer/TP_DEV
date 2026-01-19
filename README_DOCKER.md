# 📘 Introduction complète à Docker – Images, Containers, Commandes, Réseaux et Bonnes Pratiques

Ce document présente une vue d’ensemble complète de Docker : ses concepts, ses commandes, l’isolation, la création d’images, le partage, la sécurité ainsi que les bonnes pratiques professionnelles.

---

## 🧩 1. Concepts clés

### 🔹 Image vs Container

#### **Image**
Une image Docker est un **snapshot immuable**, servant de modèle pour créer des containers.  
Elle contient :
- un système de fichiers minimal,
- les dépendances,
- la configuration,
- les exécutables.

Elle est constituée de **layers** (couches), ce qui optimise :
- la taille,
- la mise en cache,
- la rapidité lors de la construction.

Exemples : `alpine:latest`, `python:3.11`.

#### **Container**
Un container est une **instance exécutable** d'une image.  
On peut en créer, supprimer, ou répliquer autant que nécessaire.

- *Image = modèle*
- *Container = instance vivante*

Les containers sont éphémères : sans volumes, toutes les données disparaissent lorsqu'on les supprime.

---

## 🔹 Isolation

Docker n’est pas une machine virtuelle.  
Les containers **partagent le noyau (kernel) de l’hôte** mais sont isolés via :

- **namespaces** (PID, réseau, mounts…)
- **cgroups** (limitations CPU/RAM)
- **seccomp**, **AppArmor**, **capabilities**

Avantages :
- plus léger qu’une VM,
- démarre très vite.

Limites :
- isolation moins forte qu’une VM,
- attention aux privilèges.

---

## 🔹 Pourquoi certaines images sont petites ?

Les images comme **Alpine** sont très légères car :
- elles ne contiennent que l’essentiel,
- beaucoup d’outils courants manquent (`bash`, `curl`, etc).

Installer un paquet dans Alpine :

```sh
apk add --no-cache vim
```

Dans Debian/Ubuntu :

```sh
apt-get update && apt-get install -y vim
```

⚠ Installer dans un container **ne modifie pas l’image**, mais seulement l’instance.  
Pour persister, utiliser un **Dockerfile** ou un `docker commit`.

---

# 🤝 2. Orchestration – Quand utiliser quoi ?

| Outil | Niveau | Usage |
|-------|--------|-------|
| **Docker Compose** | Simple | Multi-containers sur une seule machine |
| **Docker Swarm** | Moyen | Orchestration simple, clusters légers |
| **Kubernetes** | Avancé | Orchestration industrielle à grande échelle |

---

# 🛠️ 3. Commandes Docker essentielles

## ▶️ Lancer un container

```sh
docker run -it --name moncontainer alpine sh
```

- `-i` : STDIN ouvert  
- `-t` : terminal  
- `-it` : mode interactif

### Mode détaché

```sh
docker run -d --name nginx1 -p 8080:80 nginx
```

---

## 📋 Lister

```sh
docker ps
docker ps -a
docker images
```

---

## 🧹 Supprimer / nettoyer

```sh
docker rm <container>
docker rm -f <container>
docker rm -f $(docker ps -aq)

docker rmi <image>
docker image prune -a
docker system prune -a --volumes
docker volume prune
```

---

## ➡️ Interagir avec un container

```sh
docker exec -it <container> sh
docker start <container>
```

| Commande | Action |
|----------|--------|
| `docker run` | crée + démarre un container |
| `docker start` | démarre un container existant |
| `docker exec` | lance une commande dans un container actif |

---

# 🧱 4. Construire une image – Dockerfile

Exemple minimal :

```Dockerfile
FROM debian:bullseye-slim
LABEL maintainer="exemple@mail.com"

RUN apt-get update
COPY . /app
CMD ["python3", "app.py"]
```

Construire :

```sh
docker build -t monimage:latest .
```

Lancer :

```sh
docker run -it monimage
```

---

# 📦 5. Créer une image depuis un container

## 🟡 `docker commit`
Sauvegarde l’état d’un container :

```sh
docker commit <id> monimage:tag
```

## 🟡 export / import
- `docker export` : exporte le filesystem (pas les metadata)
- `docker import` : crée une image depuis un tar

## 🟢 save / load (recommandé)

```sh
docker save -o monimage.tar monimage:tag
docker load -i monimage.tar
```

---

# 🌍 6. Partager une image sur Docker Hub

```sh
docker login
docker tag monimage:tag monuser/monimage:tag
docker push monuser/monimage:tag
```

---

# 🌐 7. Réseaux, ports et volumes

## 🔌 Ports

```sh
docker run -d -p 8080:80 nginx
```

➡ `localhost:8080` → container port `80`

## 💾 Volumes

### Bind mount :
```sh
docker run -v /host/path:/container/path ...
```

### Volumes nommés :
```sh
docker run -v monvolume:/data ...
```

Sans volume → données perdues si container supprimé.

---

# 🔐 8. Sécurité – bonnes pratiques

- Ne pas utiliser `--privileged`.
- Utiliser un utilisateur non-root (`USER` dans Dockerfile).
- Réduire les capacités (`--cap-drop=ALL`).
- Ne pas copier de secrets dans l’image.
- Tenir les images à jour.

---

# 🏗️ 9. Bonnes pratiques de construction d'images

- Utiliser des images officielles et versionnées : `python:3.10-alpine`.
- Nettoyer les caches (`apt-get clean`, `rm -rf /var/lib/apt/lists/*`).
- Minimiser les layers.
- Éviter les installations inutiles.
- Ne pas manipuler des secrets dans les Dockerfile.

---

# 🎯 Conclusion

Ce guide couvre :
- les concepts fondamentaux (images, containers, isolation),
- les commandes essentielles,
- la gestion des données et réseaux,
- la création et le partage d’images,
- la sécurité et les bonnes pratiques.

Il constitue une base solide pour comprendre et utiliser Docker efficacement, en développement comme en production.
