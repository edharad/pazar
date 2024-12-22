# Roadmap du développement de l'application

## Phases principales

### Phase 1 : Recherche et conception *(finalisée)*

- **Objectifs** :
  - Valider les choix technologiques.
  - Structurer le journal de bord.
- **Livrables** :
  - Journal de bord complet et validé.

### Phase 2 : Développement du MVP *(2 semaines)*

- **Objectifs** :
  - Implémenter les fonctionnalités principales du MVP.
  - Assurer l'intégration entre les différents services et bases de données.
  - Conteneuriser les services pour faciliter le déploiement et la gestion.
- **Livrables** :
  - Application opérationnelle en local avec le backend, frontend, et bases de données fonctionnels.
  - Documentation technique pour les développeurs.
  - Fichiers Docker pour chaque service.

#### **Tâche 1 : Authentification utilisateur**

- **Description** : Implémenter le service d'authentification avec gestion des utilisateurs.
- **Technologies/Services** : Django, PostgreSQL.
- **Sous-tâches** :
  - [ ] Créer un modèle utilisateur.
  - [ ] Implémenter les APIs de connexion et d'inscription.
  - [ ] Ajouter le support pour le KYC via Onfido.
  - [ ] Configurer les tests unitaires pour l'authentification.
  - [ ] Créer un fichier Docker pour le service d'authentification.
  - [ ] Implémenter la gestion des sessions et des tokens JWT.
  - [ ] Ajouter la fonctionnalité de réinitialisation de mot de passe.
  - [ ] Mettre en place la validation des emails.
  - [ ] Gérer les autorisations et permissions (admin, vendeur, acheteur).
  - [ ] Documenter les endpoints API pour l'authentification.

#### **Tâche 2 : Création et gestion des annonces**

- **Description** : Permettre aux utilisateurs de publier et gérer des annonces.
- **Pourquoi ?** : Les utilisateurs doivent facilement poster des produits à vendre et gérer tout leur contenu.
- **Comment ?**
  - Utiliser Django pour définir le modèle d’annonce (title, description, price).
  - Créer des endpoints REST pour l’ajout et la suppression des annonces.
  - Recourir à AWS S3 pour le stockage des photos.
- **Technologies/Services** : Django, PostgreSQL, AWS S3
- **Sous-tâches** :
  - [ ] Créer le modèle d'annonce.
  - [ ] Implémenter les APIs de création, modification, suppression.
  - [ ] Configurer le stockage des images (AWS S3).
  - [ ] Créer un fichier Docker pour le service des annonces.
  - [ ] Ajouter la gestion des catégories d'annonces.
  - [ ] Mettre en place la validation des annonces avant publication.
  - [ ] Gérer les annonces expirées ou archivées.
  - [ ] Documenter les endpoints API pour la gestion des annonces.

#### **Tâche 3 : Feed personnalisé**

- **Description** : Afficher un feed d'annonces personnalisé pour chaque utilisateur.
- **Technologies/Services** : Amazon Personalize, Redis.
- **Sous-tâches** :
  - [ ] Configurer Amazon Personalize.
  - [ ] Implémenter une API pour récupérer les recommandations.
  - [ ] Intégrer les résultats au frontend.
  - [ ] Configurer les tests unitaires pour le feed personnalisé.
  - [ ] Créer un fichier Docker pour le service de feed personnalisé.
  - [ ] Ajouter la gestion des préférences utilisateur pour le feed.
  - [ ] Collecter les données de comportement utilisateur pour Amazon Personalize.
  - [ ] Documenter les endpoints API pour le feed personnalisé.

#### **Tâche 4 : Recherche avancée**

- **Description** : Permettre aux utilisateurs de rechercher des annonces par critères.
- **Technologies/Services** : Elasticsearch.
- **Sous-tâches** :
  - [ ] Configurer Elasticsearch pour l'indexation des annonces.
  - [ ] Implémenter les APIs de recherche avec filtres.
  - [ ] Intégrer une barre de recherche avancée dans le frontend.
  - [ ] Configurer les tests unitaires pour la recherche avancée.
  - [ ] Créer un fichier Docker pour le service de recherche avancée.
  - [ ] Ajouter la gestion des filtres de recherche (catégorie, prix, localisation).
  - [ ] Ajouter des filtres dynamiques basés sur les catégories disponibles.
  - [ ] Documenter les endpoints API pour la recherche avancée.

#### **Tâche 5 : Messagerie privée**

- **Description** : Permettre aux utilisateurs de communiquer en temps réel.
- **Technologies/Services** : Node.js, WebSocket, Redis.
- **Sous-tâches** :
  - [ ] Configurer WebSocket pour la messagerie.
  - [ ] Créer une interface utilisateur pour le chat.
  - [ ] Ajouter la prise en charge des pièces jointes.
  - [ ] Configurer les tests unitaires pour la messagerie.
  - [ ] Créer un fichier Docker pour le service de messagerie.
  - [ ] Ajouter la gestion des notifications en temps réel.
  - [ ] Chiffrer les messages stockés pour la confidentialité.
  - [ ] Documenter les endpoints API pour la messagerie.

#### **Tâche 6 : Paiements sécurisés**

- **Description** : Implémenter les paiements via Stripe.
- **Technologies/Services** : Node.js, Stripe.
- **Sous-tâches** :
  - [ ] Configurer l'intégration Stripe.
  - [ ] Implémenter les APIs pour créer et gérer des paiements.
  - [ ] Ajouter une interface utilisateur pour le processus de paiement.
  - [ ] Configurer les tests unitaires pour les paiements.
  - [ ] Créer un fichier Docker pour le service de paiements.
  - [ ] Ajouter la gestion des remboursements.
  - [ ] Gérer les erreurs de paiement et informer les utilisateurs.
  - [ ] Documenter les endpoints API pour les paiements.

#### **Tâche 7 : Coordination des conteneurs Docker**

- **Description** : Centraliser la configuration Docker pour le monolithe (authentification, annonces) et les microservices (messagerie, feed).
- **Comment ?**  
  - Créer un fichier Docker Compose unifié.
  - Gérer des variables d’environnement (base de données, clés API, etc.).
- **Pourquoi ?**  
  - Simplifier le démarrage et la maintenance.
  - Faciliter la mise en place d’environnements de dev/test.
- **Technologies/Services** : Docker Compose, fichiers .env
- **Sous-tâches** :
  - [ ] Rédiger la documentation sur la structure monolithique vs microservices.
  - [ ] Configurer un Dockerfile unique pour le monolithe.
  - [ ] Ajouter ou ajuster les Dockerfiles pour les microservices Node.js.
  - [ ] Tester l’orchestration locale avec Docker Compose.

#### **Tâche 8 : Développement des composants UI**

- **Description** : Créer les composants React nécessaires pour chaque fonctionnalité.
- **Technologies/Services** : React.js, TypeScript.
- **Sous-tâches** :
  - [ ] Créer les composants pour l'authentification (login, signup).
  - [ ] Créer les composants pour la gestion des annonces (création, modification, suppression).
  - [ ] Créer les composants pour le feed personnalisé.
  - [ ] Créer les composants pour la recherche avancée.
  - [ ] Créer les composants pour la messagerie privée.
  - [ ] Créer les composants pour les paiements sécurisés.
  - [ ] Ajouter la gestion des erreurs et des messages de succès.
  - [ ] Documenter les composants UI.

#### **Tâche 9 : Intégration des APIs**

- **Description** : Connecter les composants frontend aux endpoints backend.
- **Technologies/Services** : Axios, React.js.
- **Sous-tâches** :
  - [ ] Intégrer les APIs d'authentification.
  - [ ] Intégrer les APIs de gestion des annonces.
  - [ ] Intégrer les APIs du feed personnalisé.
  - [ ] Intégrer les APIs de recherche avancée.
  - [ ] Intégrer les APIs de messagerie privée.
  - [ ] Intégrer les APIs de paiements sécurisés.
  - [ ] Ajouter la gestion des erreurs et des messages de succès pour les appels API.
  - [ ] Documenter les intégrations API.

#### **Tâche 10 : Styling et Responsiveness**

- **Description** : Assurer que l'application est responsive et bien stylée.
- **Technologies/Services** : CSS, Sass, Styled-components.
- **Sous-tâches** :
  - [ ] Appliquer le design mobile-first.
  - [ ] Assurer la compatibilité avec les tablettes et desktops.
  - [ ] Utiliser des breakpoints pour ajuster le design.
  - [ ] Ajouter des animations et des transitions pour améliorer l'expérience utilisateur.
  - [ ] Documenter les styles et les composants responsives.

### Phase 3 : Tests et validation *(1 semaine)*

#### **Tâche 1 : Tests unitaires**

- **Description** : Vérifier que chaque unité de code fonctionne correctement.
- **Outils** : Jest (frontend), Pytest (backend).
- **Sous-tâches** :
  - [ ] Rédiger des tests pour le backend (authentification, annonces).
  - [ ] Rédiger des tests pour le frontend (composants React).
  - [ ] Automatiser l'exécution des tests unitaires avec GitHub Actions.

#### **Tâche 2 : Tests d'intégration**

- **Description** : S'assurer que les modules communiquent correctement.
- **Outils** : Cypress.
- **Sous-tâches** :
  - [ ] Tester les interactions entre l'API et le frontend.
  - [ ] Vérifier les flux complets comme la création d'annonce.
  - [ ] Automatiser l'exécution des tests d'intégration avec GitHub Actions.

#### **Tâche 3 : Tests end-to-end (E2E)**

- **Description** : Simuler les parcours utilisateurs du début à la fin.
- **Outils** : Selenium.
- **Sous-tâches** :
  - [ ] Tester le parcours d'inscription et d'achat.
  - [ ] Tester les recherches avancées.
  - [ ] Automatiser l'exécution des tests E2E avec GitHub Actions.

#### **Tâche 4 : Configuration du pipeline CI/CD**

- **Description** : Mettre en place un pipeline CI/CD pour automatiser les builds, tests et déploiements.
- **Technologies/Services** : GitHub Actions (ou Jenkins), Docker, Terraform.
- **Sous-tâches** :
  - [ ] Définir un workflow pour exécuter les tests unitaires et d’intégration à chaque commit.
  - [ ] Automatiser la génération des images Docker et leur push vers un registre.
  - [ ] Configurer des règles de déploiement (staging, production) avec Terraform (ou scripts).
  - [ ] Générer des rapports de test pour l’équipe (logs, alertes Slack ou email).

#### **Tâche 5 : Tests sur environnement Cloud (staging)**

- **Description** : Vérifier le bon fonctionnement de l’application sur une infrastructure Cloud avant la mise en production.
- **Sous-tâches** :
  - [ ] Déployer l’application sur un environnement de staging (Kubernetes, Docker).
  - [ ] Ré-exécuter les tests d’intégration et end-to-end pour valider la configuration cloud.
  - [ ] Ajuster la configuration (variables d’environnement, secrets) si nécessaire.
  - [ ] Tester les performances sous charge (Locust, Apache JMeter).

### Phase 4 : Déploiement *(1 semaine)*

#### **Tâche 1 : Préparation du déploiement local**

- **Description** : S'assurer que l'application est fonctionnelle sur la machine locale.
- **Sous-tâches** :
  - [ ] Vérifier la compatibilité Docker.
  - [ ] Lancer tous les services via Docker Compose.
  - [ ] Documenter le processus de déploiement local.

#### **Tâche 2 : Déploiement sur le cloud**

- **Description** : Automatiser le déploiement avec Terraform.
- **Sous-tâches** :
  - [ ] Configurer les ressources cloud nécessaires (bases de données, stockage).
  - [ ] Déployer les conteneurs sur un cluster Kubernetes.
  - [ ] Configurer la surveillance et les alertes pour les services en production.
  - [ ] Configurer des backups automatiques de la base de données et des fichiers.
  - [ ] Documenter le processus de déploiement sur le cloud.

---

## Jalons

| Jalons                   | Date limite    | Statut          |
|--------------------------|----------------|-----------------|
| Authentification prête   | Fin semaine 1  | En attente      |
| Feed et annonces prêts   | Fin semaine 2  | En attente      |
| Tests terminés           | Fin semaine 3  | En attente      |
| Déploiement en ligne     | Fin semaine 4  | En attente      |

---

## Gestion des risques

### Risques potentiels

- **Dépendance aux services tiers** : Problèmes avec Amazon Personalize, Stripe, Onfido, ou AWS S3.
- **Scalabilité** : Difficulté à gérer une augmentation rapide du nombre d'utilisateurs.
- **Sécurité** : Vulnérabilités potentielles dans les systèmes d'authentification et de paiement.

### Stratégies de mitigation

- **Dépendance aux services tiers** : Prévoir des alternatives pour chaque service critique.
- **Scalabilité** : Effectuer des tests de charge réguliers et optimiser les performances.
- **Sécurité** : Effectuer des audits de sécurité réguliers et appliquer les meilleures pratiques de sécurité.

---

## Section récapitulative

- **Progrès hebdomadaire :** Ajouter un résumé des tâches terminées.
- **Retour sur les tests :** Notez les corrections appliquées.
- **Gestion des risques :** Suivre les risques identifiés et les stratégies de mitigation.
