# Pazar - Marketplace Application

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-Proprietary-red) ![Status](https://img.shields.io/badge/status-In_Development-yellow)

## **Introduction**

Pazar est une application de place de marché sécurisée pour le commerce entre particuliers et entreprises. Elle intègre des fonctionnalités de réseau social ainsi qu'une procédure de vérification d'identité (KYC) pour sécuriser les transactions.

### **Objectif principal**

Créer une expérience de commerce en ligne sécurisée et personnalisée pour les utilisateurs cherchant à acheter ou vendre des produits.

---

## **Fonctionnalités principales (MVP)**

### **1. Authentification utilisateur**

- Gestion des comptes et connexion sécurisée.
- Vérification d'identité (KYC).

### **2. Création et gestion des annonces**

- Publication d'annonces avec des images et descriptions détaillées.
- Gestion des annonces dans un tableau de bord utilisateur.

### **3. Feed personnalisé**

- Affichage des annonces personnalisées selon les préférences des utilisateurs.

### **4. Recherche avancée**

- Recherche par filtres : catégories, localisation, prix, et autres critères.

### **5. Paiements sécurisés**

- Intégration avec Stripe pour des transactions fluides et sécurisées.

### **6. Messagerie privée**

- Communication en temps réel avec support des pièces jointes.

---

## **Technologies utilisées**

### **Frontend**

- **React.js** : Pour des interfaces utilisateur interactives et dynamiques.
- **TypeScript** : Typage statique pour une base de code plus fiable.

### **Backend**

- **Django** : Gestion des APIs REST et des fonctionnalités principales.
- **Node.js** : Support des services en temps réel comme la messagerie.

### **Bases de données**

- **PostgreSQL** : Pour les données critiques et relationnelles.
- **Redis** : Cache pour accélérer les réponses.
- **Elasticsearch** : Recherche rapide et avancée.

### **Services tiers**

- **Amazon Personalize** : Recommandations personnalisées.
- **Stripe** : Paiements sécurisés.
- **AWS S3** : Stockage des médias.
- **Onfido** : Vérification d'identité KYC.

### **Orchestration et automatisation**

- **Docker** : Conteneurisation des services.
- **Kubernetes** : Orchestration des conteneurs.
- **Terraform** : Automatisation de l'infrastructure cloud.

---

## **Installation et exécution locale**

### **Prérequis**

- Docker installé.
- Node.js installé (v16 ou plus).
- Python 3.9 ou plus.
- PostgreSQL, Redis, et Elasticsearch disponibles localement ou via Docker.

### **Étapes**

1. Clonez ce dépôt :

   ```bash
   git clone <repo-url>
   cd pazar
   ```

2. Installez les dépendances frontend et backend :

   ```bash
   cd frontend
   npm install
   cd ../backend
   pip install -r requirements.txt
   ```

3. Démarrez les services requis avec Docker Compose :

   ```bash
   docker-compose up
   ```

4. Lancez les serveurs frontend et backend :

   - Frontend :

     ```bash
     cd frontend
     npm start
     ```

   - Backend :

     ```bash
     cd backend
     python manage.py runserver
     ```

---

## **Tests**

### **Tests unitaires**

- Frontend :

  ```bash
  cd frontend
  npm test
  ```

- Backend :

  ```bash
  cd backend
  pytest
  ```

### **Tests d'intégration et end-to-end**

- Utilisez Cypress pour les tests d'intégration :

  ```bash
  cd frontend
  npx cypress open
  ```

- Selenium pour les tests E2E :

  ```bash
  python -m selenium_tests
  ```

---

## **Roadmap**

### **Phases principales**

1. **Développement du MVP** : Focus sur les fonctionnalités clés.
2. **Tests et validation** : S'assurer de la qualité et des performances.
3. **Déploiement** : Application accessible en ligne.

---

## **Contribution**

Nous travaillons en équipe restreinte pour livrer un MVP robuste. Les suggestions d'amélioration sont les bienvenues !

---

## **Licences et crédits**

- **Licence propriétaire** : Ce projet est protégé par une licence propriétaire. Toute utilisation ou distribution non autorisée est interdite.
- Technologies utilisées : React.js, Django, Node.js, PostgreSQL, Redis, Elasticsearch, Stripe, etc.
