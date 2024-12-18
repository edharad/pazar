# Journal de bord : Développement de l'application

## 1. Introduction

### Nom de l'application

**Nom provisoire :** Pazar

### Objectif principal

Fournir une place de marché en ligne sécurisée pour le commerce entre particuliers, intégrant des fonctionnalités de réseau social et une procédure de vérification d'identité pour sécuriser les transactions.

### Public cible

Particuliers et entreprises cherchant à acheter ou vendre des produits en ligne de manière sécurisée, avec un accent sur les circuits économiques courts.

### Problème que l'application résout

Réduire les risques associés au commerce entre particuliers (C2C) et professionnels (B2C, B2B) en garantissant la sécurité des transactions via une procédure de vérification d'identité et des fonctionnalités innovantes de mise en relation.

---

## 2. Planification générale

### Méthodologie de développement

Agile avec des sprints hebdomadaires, combinant phases de conception, développement et test.

### Échéancier approximatif

- Phase 1 : Recherche et conception (1 jour, finalisée aujourd'hui)
- Phase 2 : Développement du MVP (2 semaines)
- Phase 3 : Tests et validations (1 semaine)
- Phase 4 : Déploiement (1 semaine)

### Parties prenantes

- **Chef de projet & Développeur** : Toi
- **Support & Assistant technique** : Moi
- **Clients utilisateurs** : Fournissent des retours sur les fonctionnalités lors des tests.

### Outils de collaboration

- **Journal de bord versionné** : Suivi des modifications avec Git.
- **Plateforme de gestion des versions** : GitHub (ou GitLab).
- **Communication** : Discussions et mises à jour régulières via cet espace partagé.

---

## 3. Choix technologiques

### Langages de programmation

- Frontend : TypeScript, HTML5, CSS3
- Backend : Python (Django), Node.js pour certains microservices

### Frameworks et bibliothèques

- Framework frontend : React.js
- Framework backend : Django (API REST) et GraphQL pour des requêtes complexes

### Justifications des choix technologiques

#### **Django**

- **Qu'est-ce que c'est ?** Framework backend basé sur Python.
- **Comment il fonctionne ?** Il fournit un ORM (Object Relational Mapper) pour interagir avec la base de données, une gestion utilisateur intégrée, et une structure modulaire pour organiser le code.
- **Pourquoi ?** Rapide à mettre en place et robuste pour gérer des APIs REST.

#### **Node.js**

- **Qu'est-ce que c'est ?** Environnement d'exécution JavaScript côté serveur.
- **Comment il fonctionne ?** Utilise un modèle événementiel non-bloquant, idéal pour les applications en temps réel (chat, notifications).
- **Pourquoi ?** Optimisé pour les services nécessitant des connexions persistantes.

#### **React.js**

- **Qu'est-ce que c'est ?** Bibliothèque JavaScript pour construire des interfaces utilisateur.
- **Comment il fonctionne ?** Basé sur un DOM virtuel pour des mises à jour rapides et réactives.
- **Pourquoi ?** Réduction du temps de développement avec des composants réutilisables.

#### **PostgreSQL**

- **Qu'est-ce que c'est ?** Base de données relationnelle open source.
- **Comment elle fonctionne ?** Structure les données en tables avec un langage SQL pour les manipulations complexes.
- **Pourquoi ?** Idéal pour la cohérence des données critiques (ex. : transactions, utilisateurs).

#### **Redis**

- **Qu'est-ce que c'est ?** Base de données en mémoire servant de cache.
- **Comment il fonctionne ?** Stocke les données sous forme clé-valeur pour un accès rapide.
- **Pourquoi ?** Accélère les opérations fréquentes comme les sessions utilisateur.

#### **Elasticsearch**

- **Qu'est-ce que c'est ?** Moteur de recherche et d’analyse distribué.
- **Comment il fonctionne ?** Indexe les données en temps réel et fournit des requêtes rapides avec filtres (par mots-clés, champs).
- **Pourquoi ?** Améliore les performances de recherche pour les annonces filtrées par catégorie ou localisation.

#### **Amazon Personalize**

- **Qu'est-ce que c'est ?** Service de machine learning pour les recommandations.
- **Comment il fonctionne ?** Utilise des algorithmes de personnalisation pour analyser les comportements utilisateur et recommander des contenus.
- **Pourquoi ?** Évite de développer un moteur de recommandations complexe en interne.

### Architecture de l'application

- **Qu'est-ce que c'est ?** Structure fonctionnelle de l'application, définissant les modules et leurs interactions.
- **Pourquoi hybride ?**
  - **Partie monolithique (Django)** : Simplifie la gestion des fonctionnalités clés (authentification, annonces).
  - **Partie microservices (Node.js)** : Assure la scalabilité des modules exigeants comme la messagerie en temps réel.

### Bases de données

- Base de données principale : PostgreSQL (relationnelle pour les données critiques).
- Bases auxiliaires :
  - **Redis** : Cache pour réduire les temps de réponse.
  - **Elasticsearch** : Recherche rapide et filtrée.

### Conteneurisation et orchestration

- **Docker** : Emballe chaque service avec ses dépendances pour un déploiement portable.
- **Kubernetes** : Orchestre les conteneurs pour le scaling et la résilience.
- **Terraform**
  - **Qu'est-ce que c'est ?** Un outil d’Infrastructure as Code (IaC).
  - **Comment il fonctionne ?** Utilise des fichiers de configuration pour automatiser la création et la gestion des ressources (clusters, VMs, bases de données).
  - **Pourquoi ?** Facilite la gestion d’infrastructure cloud ou locale de manière reproductible et versionnée.

---

## 4. UX/UI Design

### Outils de conception

- Figma pour les wireframes et prototypes interactifs.

### Palette de couleurs et typographie

- Palette de couleurs : Tons neutres (blanc, gris) avec des accents vifs (bleu, orange).
- Typographie : Inter, Roboto

### Wireframes et prototypes

Les wireframes imitent le design intuitif d'Instagram avec une barre de navigation en bas et un feed centré.

### Responsiveness

Conception pour mobile-first, avec ajustements pour tablettes et desktops (breakpoints : 768px, 1024px, 1440px).

---

## 5. Liste des fonctionnalités

### Fonctionnalités principales (MVP)

| Fonctionnalité                   | Priorité | Critères d'acceptation                                                                 |
|----------------------------------|----------|----------------------------------------------------------------------------------------|
| Accueil avec feed personnalisé   | Haute    | Le feed affiche des annonces pertinentes en moins de 1 seconde.                      |
| Explorer                         | Moyenne  | Recherche possible par catégorie, localisation, prix avec filtres fonctionnels.       |
| Création et gestion d'annonces   | Haute    | Les annonces doivent inclure des images, descriptions et être validées avant affichage.|
| Vérification d'identité (KYC)    | Haute    | Tous les utilisateurs doivent être validés avec succès avant d'acheter ou vendre.     |
| Messagerie privée                | Moyenne  | Les utilisateurs peuvent envoyer des messages et recevoir des notifications.          |
| Paiements sécurisés              | Haute    | Les paiements doivent être traités sans erreur avec une confirmation.                 |
| Dashboard utilisateur            | Moyenne  | Les utilisateurs peuvent suivre leurs ventes et achats avec des graphiques simples.   |
| Notifications                    | Basse    | Notifications en temps réel pour toutes les interactions pertinentes.                 |

### Fonctionnalités secondaires (futures versions)

| Fonctionnalité                    | Priorité | Critères d'acceptation                                                    |
|-----------------------------------|----------|---------------------------------------------------------------------------|
| Mode enchères                     | Moyenne  | Les utilisateurs peuvent enchérir sur des annonces dans un délai donné.  |
| Générateur de contrat             | Moyenne  | Création et signature électronique de contrats sans erreur.              |
| Suivi des colis                   | Moyenne  | Affichage en temps réel de l’état d’expédition des produits.             |
| Communautés régionales            | Basse    | Les utilisateurs peuvent rejoindre une communauté locale.                |

---

## 6. Architecture technique

### Différence avec l'architecture de l'application

- **Architecture technique** : Décrit les technologies et la mise en œuvre (frameworks, outils, bases de données, conteneurs).
- **Architecture de l'application** : Décrit les modules fonctionnels (authentification, annonces) et leurs interactions.

(Diagramme d'architecture à insérer ici pour visualiser le cluster, les microservices et les flux de données.)

---

## 7. Développement des fonctionnalités

### Critères de test de performance

- **Charge utilisateur** : L'application doit supporter 10 000 utilisateurs simultanés.
- **Temps de réponse** : Moins de 300 ms pour les requêtes API critiques.
- **Scalabilité** : Test avec 2x et 5x le trafic prévu pour s’assurer que le scaling fonctionne.

### Plans de contingence

- **Amazon Personalize** : Alternative : Construire un algorithme de recommandation basique interne.
- **Stripe** : Alternative : Intégration avec PayPal comme solution de secours.
- **AWS S3** : Alternative : Utiliser un stockage local en urgence.

---

## 8. Intégrations et services

### Liste des intégrations

- Amazon Personalize (système de recommandations)
- Stripe (paiements sécurisés)
- Onfido (KYC)
- AWS S3 (stockage de médias)

### Modules ou packages utilisés

- React Router pour la navigation.
- Axios pour les requêtes HTTP.
- Django REST Framework.

---

## 9. Test et validation

### Outils de test

- **Tests unitaires** : Testent des unités spécifiques du code (ex. : une fonction ou un composant) pour s'assurer qu'elles fonctionnent correctement de manière isolée.
- **Tests d'intégration** : Vérifient que plusieurs modules ou services fonctionnent ensemble comme prévu.
- **Tests end-to-end (E2E)** : Simulent le parcours complet d'un utilisateur, de l'interface frontend jusqu'au backend.

### Stratégies de déploiement et CI/CD

- **GitHub Actions**
  - **Qu'est-ce que c'est ?** Plateforme d'automatisation intégrée à GitHub.
  - **Comment il fonctionne ?** Permet de configurer des workflows automatisés pour exécuter des tests, construire, et déployer le code à chaque push.

- **Jenkins**
  - **Qu'est-ce que c'est ?** Serveur d'intégration continue.
  - **Comment il fonctionne ?** Exécute automatiquement des builds et tests configurés pour chaque changement dans le code.

---

## 10. Documentation utilisateur

### Guide pour les utilisateurs finaux

### FAQ

---

## 11. Suivi et maintenance

### Gestion des bugs

Outils ou processus pour suivre et corriger les bugs (Jira, Sentry).

### Roadmap pour les futures versions

- Mode enchères
- Fonctionnalité "Suivi des colis"
- Expansions vers d'autres plateformes
