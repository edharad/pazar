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
- **Livrables** :
  - Application opérationnelle en local avec le backend, frontend, et bases de données fonctionnels.

### Phase 3 : Tests et validation *(1 semaine)*

- **Objectifs** :
  - Tester les fonctionnalités du MVP (tests unitaires, intégration, end-to-end).
  - Valider les performances sous charge.
- **Livrables** :
  - Rapport des tests et correctifs appliqués.

### Phase 4 : Déploiement *(1 semaine)*

- **Objectifs** :
  - Déployer l’application en production (local ou cloud).
- **Livrables** :
  - Application déployée et accessible à des utilisateurs réels.

---

## Détail des tâches par phase

### Phase 2 : Développement du MVP

#### **Tâche 1 : Authentification utilisateur**

- **Description** : Implémenter le service d'authentification avec gestion des utilisateurs.
- **Technologies/Services** : Django, PostgreSQL.
- **Sous-tâches** :
  - [ ] Créer un modèle utilisateur.
  - [ ] Implémenter les APIs de connexion et d'inscription.
  - [ ] Ajouter le support pour le KYC via Onfido.

#### **Tâche 2 : Création et gestion des annonces**

- **Description** : Permettre aux utilisateurs de publier et gérer des annonces.
- **Technologies/Services** : Django, PostgreSQL, AWS S3 (pour le stockage des médias).
- **Sous-tâches** :
  - [ ] Créer un modèle d'annonce avec champs nécessaires (titre, description, prix).
  - [ ] Implémenter les APIs pour créer, modifier, supprimer une annonce.
  - [ ] Gérer le stockage des images via AWS S3.

#### **Tâche 3 : Feed personnalisé**

- **Description** : Afficher un feed d'annonces personnalisé pour chaque utilisateur.
- **Technologies/Services** : Amazon Personalize, Redis.
- **Sous-tâches** :
  - [ ] Configurer Amazon Personalize.
  - [ ] Implémenter une API pour récupérer les recommandations.
  - [ ] Intégrer les résultats au frontend.

#### **Tâche 4 : Recherche avancée**

- **Description** : Permettre aux utilisateurs de rechercher des annonces par critères.
- **Technologies/Services** : Elasticsearch.
- **Sous-tâches** :
  - [ ] Configurer Elasticsearch pour l'indexation des annonces.
  - [ ] Implémenter les APIs de recherche avec filtres.
  - [ ] Intégrer une barre de recherche avancée dans le frontend.

#### **Tâche 5 : Messagerie privée**

- **Description** : Permettre aux utilisateurs de communiquer en temps réel.
- **Technologies/Services** : Node.js, WebSocket, Redis.
- **Sous-tâches** :
  - [ ] Configurer WebSocket pour la messagerie.
  - [ ] Créer une interface utilisateur pour le chat.
  - [ ] Ajouter la prise en charge des pièces jointes.

#### **Tâche 6 : Paiements sécurisés**

- **Description** : Implémenter les paiements via Stripe.
- **Technologies/Services** : Node.js, Stripe.
- **Sous-tâches** :
  - [ ] Configurer l'intégration Stripe.
  - [ ] Implémenter les APIs pour créer et gérer des paiements.
  - [ ] Ajouter une interface utilisateur pour le processus de paiement.

---

### Phase 3 : Tests et validation

#### **Tâche 1 : Tests unitaires**

- **Description** : Vérifier que chaque unité de code fonctionne correctement.
- **Outils** : Jest (frontend), Pytest (backend).
- **Sous-tâches** :
  - [ ] Rédiger des tests pour le backend (authentification, annonces).
  - [ ] Rédiger des tests pour le frontend (composants React).

#### **Tâche 2 : Tests d'intégration**

- **Description** : S'assurer que les modules communiquent correctement.
- **Outils** : Cypress.
- **Sous-tâches** :
  - [ ] Tester les interactions entre l'API et le frontend.
  - [ ] Vérifier les flux complets comme la création d'annonce.

#### **Tâche 3 : Tests end-to-end (E2E)**

- **Description** : Simuler les parcours utilisateurs du début à la fin.
- **Outils** : Selenium.
- **Sous-tâches** :
  - [ ] Tester le parcours d'inscription et d'achat.
  - [ ] Tester les recherches avancées.

---

### Phase 4 : Déploiement

#### **Tâche 1 : Préparation du déploiement local**

- **Description** : S'assurer que l'application est fonctionnelle sur la machine locale.
- **Sous-tâches** :
  - [ ] Vérifier la compatibilité Docker.
  - [ ] Lancer tous les services via Docker Compose.

#### **Tâche 2 : Déploiement sur le cloud**

- **Description** : Automatiser le déploiement avec Terraform.
- **Sous-tâches** :
  - [ ] Configurer les ressources cloud nécessaires (bases de données, stockage).
  - [ ] Déployer les conteneurs sur un cluster Kubernetes.

---

## Jalons

| Jalons                   | Date limite    | Statut          |
|--------------------------|----------------|-----------------|
| Authentification prête   | Fin semaine 1  | En attente      |
| Feed et annonces prêts   | Fin semaine 2  | En attente      |
| Tests terminés           | Fin semaine 3  | En attente      |
| Déploiement en ligne     | Fin semaine 4  | En attente      |

---

## Section récapitulative

- **Progrès hebdomadaire :** Ajouter un résumé des tâches terminées.
- **Retour sur les tests :** Notez les corrections appliquées.
