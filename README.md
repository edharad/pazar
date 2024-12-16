# Pazar 0.0.0

![Version](https://img.shields.io/badge/version-0.0.0-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

## Introduction

Pazar est une application de marché en ligne sécurisée pour le commerce entre particuliers, intégrant des fonctionnalités de réseau social et une procédure de vérification d'identité (KYC).

## Table des matières

1. [Présentation](#présentation)
2. [Journal de bord](#journal-de-bord)
3. [Architecture](#architecture)
   - [Déploiement et hébergement](#déploiement-et-hébergement)
   - [Bases de données](#bases-de-données)
4. [Technologies](#technologies)
   - [Frontend](#frontend)
   - [Backend](#backend)
   - [Base de données](#base-de-données)
   - [Authentification et Autorisation](#authentification-et-autorisation)
   - [Stockage de fichiers](#stockage-de-fichiers)
   - [Messagerie et Notifications](#messagerie-et-notifications)
   - [Système de recommandation](#système-de-recommandation)
   - [CI/CD](#cicd)
   - [Monitoring](#monitoring)
   - [Logging](#logging)
5. [UX & UI](#ux--ui)
   - [Introduction UX/UI](#introduction-uxui)
   - [Landing UX/UI](#landing-uxui)
   - [Inscription et connexion UX/UI](#inscription-et-connexion-uxui)
   - [Layout UI](#layout-ui)
   - [Feed principal (Accueil) UX/UI](#feed-principal-accueil-uxui)
6. [Fonctionnalités](#fonctionnalités)
7. [Installation et déploiement](#installation-et-déploiement)
8. [Contributions](#contributions)
9. [Licences et crédits](#licences-et-crédits)

## Présentation

L'application "Pazar" a pour objectif de fournir une place de marché en ligne sécurisée pour le commerce entre particuliers, facilitant la vente et l'achat de biens. Elle se distingue par son intégration de fonctionnalités de réseau social et une procédure de vérification d'identité (KYC) obligatoire pour tous les utilisateurs souhaitant vendre ou acheter des produits. Cette procédure, similaire à celle utilisée par les applications de trading de cryptomonnaie, vise à garantir la sécurité des transactions.

Pazar répond à un besoin croissant de sécurité dans les relations commerciales de tout type (C2C, B2C, B2B, etc.) et ambitionne de promouvoir les circuits économiques courts à l'échelle mondiale. L'application sera disponible sur plusieurs plateformes : en tant que webapp accessible via URL, en application mobile et tablette pour iOS et Android, et potentiellement sur d'autres supports en fonction des opportunités d'expansion du projet.

## Journal de bord

Le présent fichier (README) fait office de journal de bord afin de présenter les fonctionnalités de l'application, mais aussi avoir un suivi sur son développement, son déploiement, sa maintenance, sa gestion et sa mise à jour. Des fichiers annexes tels que [CONTRIBUTING.md](CONTRIBUTING.md), [CHANGELOG.md](CHANGELOG.md), [ROADMAP.md](ROADMAP.md) seront également créés et mis à jour en fonction de l'avancée du projet. README sera le fichier de référence pour l'ensemble de l'application car il permet d'être versionné et d'être consulté de façon dynamique.

## Architecture

L'architecture de l'application "Pazar" est basée sur une approche microservices pour assurer la scalabilité, la maintenabilité et la résilience.

### Déploiement et hébergement

L'application sera déployée sur une infrastructure basée sur Kubernetes pour l'orchestration des conteneurs et Docker pour la conteneurisation. Cela permettra une gestion efficace des déploiements, une scalabilité automatique et une tolérance aux pannes.

### Bases de données

L'application utilisera PostgreSQL pour les données relationnelles et MongoDB pour les données non relationnelles. Cela permettra de gérer efficacement les différentes types de données et d'assurer une haute disponibilité et une performance optimale.

## Technologies

### Frontend

- **Webapp** : React.js ou Vue.js
- **Applications mobiles** : React Native ou Flutter

### Backend

- **Microservices** : Node.js avec Express.js ou NestJS
- **API** : GraphQL pour les requêtes et mutations

### Base de données

- **Relationnelle** : PostgreSQL
- **Non relationnelle** : MongoDB

### Authentification et Autorisation

- **Technologies** : OAuth 2.0, JWT (JSON Web Tokens)

### Stockage de fichiers

- **Technologies** : AWS S3 ou Google Cloud Storage

### Messagerie et Notifications

- **Messagerie en temps réel** : WebSockets
- **Notifications push** : Firebase Cloud Messaging (FCM)

### Système de recommandation

- **Technologies** : Amazon Personalize ou un moteur de recommandation personnalisé

### CI/CD

- **Technologies** : GitHub Actions, Jenkins ou GitLab CI/CD

### Monitoring

- **Technologies** : Prometheus, Grafana

### Logging

- **Technologies** : ELK Stack (Elasticsearch, Logstash, Kibana)

## UX & UI

### Important

Chacun des points susmentionnés sera essentiel afin de choisir les composants à développer, déterminer l'architecture optimale de l'application, faciliter la programmation des tests unitaires et des tests fonctionnels, savoir quels frameworks, langages ou services tiers doivent être utilisés, et isoler les problèmes potentiels liés à la sécurité. Par conséquent cette partie du README sera mise à jour continuellement en fonction des décisions technologiques qui seront prises durant le développement et les mises à jour de l'application.

### Introduction UX/UI

La webapp se distingue en 3 tailles et pour chacune des tailles, la disposition et la visibilité des composants seront différentes pour des questions de responsive. Par conséquent, il sera nécessaire de montrer où se trouvent les composants en fonction de chaque taille pour chaque situation. Les tailles en question sont les suivantes :

```css
/* Mobile */
@media (max-width: 480px) {
  /* Styles pour petits mobiles */
}

/* Tablette */
@media (min-width: 481px) and (max-width: 1024px) {
  /* Styles pour tablettes */
}

/* Desktop */
@media (min-width: 1025px) {
  /* Styles pour desktops */
}
```

Le rendu en fonction des tailles ne devrait pas radicalement différer entre la version webapp taille mobile et la version mobile de l'application. Par conséquent, lorsqu'il y aura une différence entre les deux nous la mentionnerons directement en image et textuellement. Ici nous allons d'abord aborder chaque étape de l'expérience utilisateur en partant initialement de son inscription jusqu'à l'utilisation de chaque fonctionnalité de l'application pour chaque version de l'application. A savoir les versions webapp, mobile et tablette. Bien qu'il n'y ait pas trop de différences, nous souhaitons tout de même présenter les éléments suivants:

- Une maquette de l'interface développée sur figma sera jointe au point.
- Explication de l'expérience de l'utilisateur avec chaque élément de l'interface.
- Redirections et changement en cas de succès ou d'erreurs.

### Landing UX/UI

--> IMAGE LANDING PAGE WEB DESKTOP, MOBILE, TABLETTE

#### 1.1. Page de connexion (Landing) - Taille Desktop UX/UI

La page de connexion (Landing) pour la version desktop de l'application "Pazar" s'inspire du layout de la page de connexion de la webapp d'Instagram. Voici les principaux composants et leur disposition :

- **Container principal** :
  - Divisé en deux sections principales : une image de présentation à gauche et le formulaire de connexion à droite.

- **Section gauche** :
  - Affiche une image ou une série d'images en rotation pour présenter les fonctionnalités de l'application.

- **Section droite** :
  - **Logo** : Affiché en haut du formulaire de connexion.
  - **Formulaire de connexion** :
    - Champs pour le nom d'utilisateur et le mot de passe.
    - Bouton de connexion.
    - Lien "Mot de passe oublié ?" pour récupérer le mot de passe.
  - **Ou** : Une ligne de séparation avec le mot "Ou" pour indiquer une alternative.
  - **Connexion avec les réseaux sociaux** : Bouton pour se connecter avec un compte de réseau social (par exemple, Facebook).
  - **Inscription** : Lien vers la page d'inscription pour les nouveaux utilisateurs.

- **Footer** :
  - Liens vers les pages importantes (À propos, Contact, FAQ, etc.), les réseaux sociaux, et les informations légales.

#### 1.2. Landing - Taille Tablette UX/UI

La page de connexion (Landing) pour la version tablette de l'application "Pazar" s'inspire également du layout de la page de connexion de la webapp d'Instagram, mais avec des ajustements pour une meilleure expérience utilisateur sur les écrans de taille moyenne. Voici les principaux composants et leur disposition :

- **Container principal** :
  - Divisé en deux sections principales : une image de présentation en haut et le formulaire de connexion en bas.

- **Section supérieure** :
  - Affiche une image ou une série d'images en rotation pour présenter les fonctionnalités de l'application. L'image occupe environ la moitié de l'écran.

- **Section inférieure** :
  - **Logo** : Affiché en haut du formulaire de connexion.
  - **Formulaire de connexion** :
    - Champs pour le nom d'utilisateur et le mot de passe.
    - Bouton de connexion.
    - Lien "Mot de passe oublié ?" pour récupérer le mot de passe.
  - **Ou** : Une ligne de séparation avec le mot "Ou" pour indiquer une alternative.
  - **Connexion avec les réseaux sociaux** : Bouton pour se connecter avec un compte de réseau social (par exemple, Facebook).
  - **Inscription** : Lien vers la page d'inscription pour les nouveaux utilisateurs.

- **Footer** :
  - Liens vers les pages importantes (À propos, Contact, FAQ, etc.), les réseaux sociaux, et les informations légales.

#### 1.2. Landing - Taille Mobile UX/UI

La page de connexion (Landing) pour la version mobile de l'application "Pazar" s'inspire du layout de la page de connexion de la webapp d'Instagram, mais avec des ajustements pour une meilleure expérience utilisateur sur les petits écrans. Voici les principaux composants et leur disposition :

- **Container principal** :
  - Une seule colonne avec le formulaire de connexion en haut et une image de présentation en bas.

- **Section supérieure** :
  - **Logo** : Affiché en haut du formulaire de connexion.
  - **Formulaire de connexion** :
    - Champs pour le nom d'utilisateur et le mot de passe.
    - Bouton de connexion.
    - Lien "Mot de passe oublié ?" pour récupérer le mot de passe.
  - **Ou** : Une ligne de séparation avec le mot "Ou" pour indiquer une alternative.
  - **Connexion avec les réseaux sociaux** : Bouton pour se connecter avec un compte de réseau social (par exemple, Facebook).
  - **Inscription** : Lien vers la page d'inscription pour les nouveaux utilisateurs.

- **Section inférieure** :
  - Affiche une image ou une série d'images en rotation pour présenter les fonctionnalités de l'application.

- **Footer** :
  - Liens vers les pages importantes (À propos, Contact, FAQ, etc.), les réseaux sociaux, et les informations légales.

### Inscription et connexion UX/UI

#### 2.1. Introduction - Inscription et connexion UX/UI

#### 2.2. Formulaire d'inscription simple - Inscription et connexion UX/UI

--> IMAGES DE L'INTERFACE FORMULAIRE INSCRIPTION

Suite à la demande d'inscription, l'utilisateur

- Adresse email ou numéro de téléphone (Numéro reconnu selon le lieu de connexion. Choix de l'indicatif si nécessaire)
- Nom
- Prénom
- Date de naissance
- Pays de résidence
- Nom d'utilisateur (avec proposition d'alternative)
- Mot de passe avec conditions (ex: nombre de caractères minimum, chiffres, majuscules, minuscules). Il doit pouvoir enregistrer le mot de passe si il le souhaite et l'authentification à deux facteurs, avec envoie du code par sms ou par email a lieu d'office. Sur mobile, il pourra choisir de se connecter de façon biometrique. Sur ordinateur aussi mais c'est une fonctionnalité propre a la reconnaissance digital sur macbook par exemple.
- Une case à cocher qui stipule que l'utilisateur accepte nos conditions d'utilisation, notre charte de confidentialité et notre politique des données. Il peut les consulter en cliquant dessus.

Lorsqu'il a terminé d'entrer toutes les infromations, il passe à la suite en envoyant ses donnés via le bouton.

#### 2.3. Validation avec code reçu UX/UI

--> IMAGE DE L'INTERFACE VALIDATION CODE

Un mail ou un sms, en fonction de ce qu'il a entré, lui est envoyé avec un code de vérification afin de finaliser cette première inscription dans l'écosystème et activer le compte. L'utilisateur est face à un component qui lui demande d'entrer le code. Lorsque le code est entré, cette phase de l'inscription est terminée et on peut passer à la suite. A cette étape, nous avons dores et déjà des données sur cet utilisateur confirmé. L'adresse email et/ou le numéro de téléphone.

#### 2.4. KYC - Procédure complète UX/UI

INFORMATION : il est possible que pour le KYC l'application fasse appel à un service tiers déjà programmé.

##### 2.3.1. KYC - INFORMATIONS ET CONDITIONS DU KYC UX/UI

--> IMAGE DE LA PREMIÈRE ÉTAPE DU KYC INFORMATIONS ET CONDITIONS DU KYC

C'est un point central de l'application car ce processus doit être rapide et facile pour l'utilisateur. Autrement dit très pédagogique. Cette partie est très semblable à ce que l'on retrouve sur les plateformes de trading de cryptomonnaies telles que binance ou kraken. L'utilisateur est face à un component qui l'informe que Pazar a pour but de mettre à disposition de ses utilisateurs un réseau social commercial afin que les utilisateurs puissent acheter et vendre de façon sécurisée et vérifiée. Par conséquent, il est essentiel que chaque utilisateur vérifie son identité. Un lien vers la politique de confidentialité est présent afin que les utilisateurs sache de quelle façon les données sont traitées.

Lui sera également demandé d'accepter le suivi de la localisation afin d'affiner les recommandations pour lui. Donc un popup s'ouvrira qu'il pourra accepter ou non pour le suivi de la localisation juste après qu'il est appuyer sur le bouton accepter pour débuter le KYC et juste avant l'étape du formulaire complet.

--> IMAGE POPUP LOCALISATION

##### 2.3.2. KYC - FORMULAIRE D'INSCRIPTION COMPLET UX/UI

--> IMAGE DE LA DEUXIÈME ETAPE DU KYC > FORMULAIRE

L'utilisateur arrive face à un componant qui contient un formulaire muni d'un bouton suivant. Ce formulaire est la première étape du KYC, si il n'est pas dûment rempli, l'utilisateur ne peut pas poursuivre en cliquant sur le bouton suivant et un message d'erreur demandant de remplir correctement le formulaire s'affiche. Tous les champs sont obligatoires initialement. Il est demandé au client de remplir le formulaire dans lequel les champs sont les suivants : nom et prénoms (au pluriel) tels qu'inscrits sur sa carte d'identité ou permis de conduire, son pays de résidence, son adresse, code postale, ville et numero de téléphone.
Si la procédure est interrompue avant la fin, une sauvegarde de l'état et de l'étape du processus d'inscription a lieu et si il revient sur l'appli, il pourra poursuivre son inscription où il en était avec un message qui lui dira "Vous êtes de retour pour finaliser votre inscription etc...".

##### 2.3.3. KYC - UPLOAD ID CARD OR LICENSE UX/UI

--> IMAGE DE LA TROISIÈME ETAPE DU KYC - UPLOAD DE L'ID

L'utilisateur arrive sur un component qui lui demande de upload une photo de sa carte d'identité nationale ou de son permis de conduire, recto et verso. Une fois cela fait il peut cliquer sur le bouton suivant.

##### 2.3.4. KYC - UPLOAD OFFICAL DOCUMENT, ADRESS VERIFICATION OR BIOMETRIC VERIFICATION UX/UI

--> IMAGE DES DEUX OPTIONS DE VERIFICATION
--> IMAGE DE LA QUATRIÈME ETAPE DU KYC - UPLOAD DE DOCUMENT OFFICIEL
--> IMAGE INTERFACE FACE ID VERIFICATION

L'utilisateur arrive ensuite, sachant qu'il a fait l'incription sur la webapp, il lui est demandé de fournir la copie d'un document officiel qui prouve qu'il est bien le détenteur de cette identité. Cela n'aura pas lieu sur la version mobile ou si la webapp est sur un navigateur sur mobile ou tablette car la reconnaissance faciale prendra le relai à cette étape là. Donc j'imagine que sur la version webapp desktop, ne seront acceptées que les factures de téléphone ou une facture de l'assurance maladie. Cependant, il faudra proposer les deux options à l'utilisateur. Vérifier par facture ou vérifier par face ID.

##### 2.3.5. KYC - VERIFICATION EN COURS UX/UI

--> IMAGE DE LA CINQUIÈME ÉTAPE DU KYC - VÉRIFICATION ET REDIRECTION

L'utilisateur est maintenant face à un component qui montre un cercle en chargement afin de lui montrer que l'analyse de sa procédure de KYC est en cours. Si c'est valide le cercle se transforme en cercle avec un vu et un message de succès. S'il y a une erreur l'état du component change et affiche le message d'erreur. Le message d'erreur s'affiche à l'utilisateur. L'info retourne un cliquable afin de corriger le point si cela est possible. Alors l'utilisateur retourne à l'étape du KYC où il peut corriger ce qu'il a fait, corrige, clique sur suivan, arrive à l'étape suivante qu'il faut corriger s'il y en a encore ou arrive à la fin de la procédure de KYC. L'analyse a lieu à nouveau, s'il n'y a pas d'autres étapes à corriger. Si c'est une erreur qui ne peut être corrigé telle qu'une interdiction quelconque ou légale nous informons l'utilisateur que pour ces raisons nous ne pouvons poursuivre son inscription.
En cas de réussite, le component change d'état, affiche un vu vert ou autre chose qui confirme l'inscription et l'utilisateur est redirigé automatiquement vers l'étape du choix des centres d'intérets.

#### 2.5. Centres d'intérêts UX/UI

--> IMAGE DE L'INTERFACE AFFICHANT LE COMPONENT CENTRE D'INTÉRETS

Durant cette étape, lui sont proposées des catégories de produits ou des centres d'intérêts. Par exemple, il peut y avoir le sport, le fitness, les automobiles, la construction, les biens immobiliers etc. Le choix de ces centres d'intérêts se devra d'être au minimum de 5 obligatoires. Cette étape est cruciale afin d'initialiser le feed. Bien entendu le système de recommandation étant bien plus technique et dynamique que cela, le contenu du feed dépendera de bien plus de facteurs que ce qu'il aura choisi comme centres d'intérêts. Nous nous y attarderons dans le point spécifique au développement du feed et de l'intégration du système de recommandation avec le traitement des données générées par l'utilisateur.

#### 2.6. Activation de l'authentification à 2 facteurs (2FA) ou authentication biométrique UX/UI

--> IMAGE DE L'INTERFACE AFFICHANT LA PROPOSITION D'ACTIVATION DE L'AUTHENTIFICATION A DEUX FACTEURS

Cette étape précède la finalisation de l'inscription et demande à l'utilisateur s'il souhaite activer l'authentification à deux facteurs pour des raisons de sécurité. S'il souhaite le faire, il peut choisir de le faire via application d'authentication, numéro de téléphone. Il peut également choisir de le faire de façon biométrique. Il peut accepter et configurer ou refuser et passer à la suite.

### Layout UI

#### 3.1. Layout - Global (accueil)

--> IMAGES DU LAYOUT GLOBAL ACCUEIL (desktop, tablette, mobile)
--> IMAGES DU LAYOUT DE LA VERSION MOBILE ET DIFFERENCES AVEC WEBAPP MOBILE

Une brève présentation générale s'impose afin de rapidement connaitre les sections du layout général et différencier celles qui sont visibles en fonction de la taille de l'écran.

Ci-dessous une liste simplifiée des sections visibles et invisibles en fonction de la taille de l'écran.

| Components    | Desktop ≥ 1025px      | Tablette ≥ 481px && ≤ 1024px | Mobile ≤ 480px  |
| ------------- | --------------------- | ---------------------------- | --------------- |
| SideNav       | ✔️                     | ✔️                            | ❌              |
| Logo Text     | ✔️                     | ❌                           | ❌              |
| Logo Icon     | ❌                    | ✔️                            | ✔️               |
| TopNav        | ❌                    | ❌                           | ✔️               |
| BottomNav     | ❌                    | ❌                           | ✔️               |
| SearchBar     | ❌                    | ❌                           | ✔️               |
| Suggest Sec   | ✔️                     | ❌                           | ❌              |

##### 3.1.1. Layout global taille desktop

Celle qui comprend le plus d'éléments ou plutôt le plus de détails on peut constater trois sections majeures, la nav bar verticale (sidenav) à gauche qui contient le logo textuel mais pas icone, les éléments du menu, le menu hamburger contenant le bouton des paramètres et autres. Puis il y a section principale et centrale qui elle contient une sorte de div ou section qui contient les medaillons relatifs aux abonnements afin de visuliser leurs storys et que l'on peut scroller horizontalement. Je pense que ce dernier sera un div sachant que si l'élément actif du menu change, la barre de storys disparait. En dessous de cette barre on retrouve le le feed principal où apparaitront les annonces. Feed que l'on peut scroller verticalement.  Puis il y a la section secondaire qui elle contient les suggestions d'amis ou de communautés auxquelles on peut s'abonner.

##### 3.1.2. Layout global taille tablette

La nav bar verticale (sidenav) moins large qu'en taille desktop à gauche. Cette dernière comprend le logo icone masi pa textuel, les éléments du menu mais sans les titres, le menu hamburger contenant le bouton des paramètres et autres. Puis il y a section principale et centrale qui elle contient le contenu relatif à l'élément du menu actif. A droite il n'y a pas la section secondaire. Celle-ci a disparu au profit de la section principale qui prend désormais le reste de la largeur.

##### 3.1.3. Layout global taille mobile

La nav bar verticale (sidenav) n'est plus visible. A la place elle s'est séparée en deux. Une topbar et une bottombar. Les deux sont horizontal, une positionnée en bordure supérieur et l'autre en bordure inferieur. Celle en bordure superieur contient en partant de la gauche, le titre textuel, une barre de recherche et le bouton de notification mais seulement l'icone du bouton, pas le texte. Celle en bordure inférieur contient seulement les icones des éléments de menu suivants : Accueil, Explorer, Boutique, Panier, Messages, Profil. Puis il y a section principale et centrale qui elle contient le contenu relatif à l'élément du menu actif et qui se trouve entre les deux navbar. Le menu secondaire est quant à lui invisible. **Il est important de savoir que les éléments visible dans la disposition en taille mobile de la webapp ne sont pas les mêmes que ceux en mobile app.**

#### 3.2. Layout - Navbar(s) et menu

--> IMAGE DES NAVBARS SELON CHAQUE TAILLE

La navbar est un élément du layout qui est essentiel pour la navigation de l'utilisateur. Les éléments du menu sont listés dans le tableau ci-dessous. Comme vous pouvez le voir, certains éléments sont visibles et d'autres ne le sont pas suivant la taille de l'écran. Les points suivants expliqueront de quelle façon sont disposés les éléments du menu suivant l'écran.

| Menu items    | Desktop ≥ 1025px      | Tablette ≥ 481px && ≤ 1024px | Mobile ≤ 480px  |
| ------------- | --------------------- | ---------------------------- | --------------- |
| Logo textuel  | ✔️                     | ✔️                            | ❌              |
| Logo icone    | ❌                    | ✔️                            | ❌              |
| Accueil       | ✔️                     | ✔️                            | ✔️               |
| Recherche     | ✔️                     | ✔️                            | ✔️               |
| Explorer      | ✔️                     | ✔️                            | ✔️               |
| Boutique      | ✔️                     | ✔️                            | ✔️               |
| Panier        | ✔️                     | ✔️                            | ✔️               |
| Messages      | ✔️                     | ✔️                            | ✔️               |
| Dashboard     | ✔️                     | ✔️                            | ✔️               |
| Communautés   | ✔️                     | ✔️                            | ✔️               |
| Notifications | ✔️                     | ✔️                            | ✔️               |
| Créer         | ✔️                     | ✔️                            | ✔️               |
| Profil        | ✔️                     | ✔️                            | ✔️               |
| Paramètres    | ✔️                     | ❌                           | ❌              |
| Titles        | ✔️                     | ❌                           | ❌              |

##### 3.2.1. Layout Navbar - taille desktop

--> IMAGE DE LA DISPOSITION DE LA NAVBAR EN TAILLE DESKTOP

Comme on peut le constater sur l'image pour la taille desktop, on retrouve la navbar disposée verticalement et située à gauche. C'est une side nav bar. On y trouve les icones de menus ainsi que les titres qui forments des éléments cliquables qui nous permettent de naviguer sur Pazar.

La diposition est la suivante :

Titre de l'application (image du logo textuel)

--espace--

- (Icone maison)       Accueil
- (Icone loupe)        Recherche
- (Icone globe)        Explorer
- (Icone Boutique)     Boutique
- (Icone Panier)       Panier
- (Icone avion papier) Messages
- (Icone de moniteur)  Dashboard
- (Icone communauté)   Communautés
- (Icon notification)  Notifications
- (Icone paramètres)   Créer
- (Icone profile)      Profil

--espace--

Proche du bord inférieur, le menu hamburger qui une fois cliquée affiche un menu déroulant vers le haut qui contient d'autres options :

- (Icone roue dentée)  Paramètres
- (Icone d'activité)   Votre activité
- (Icone lune)         Changer de thème

##### 3.2.2. Layout Navbar - Taille tablette

--> IMAGE DE LA DISPOSITION DE LA NAVBAR EN TAILLE TABLETTE

Ici rien n'est très différent de la taille desktop hormis le fait qu'il n'y a pas le texte lié aux éléments du menu.

##### 3.2.3. Layout Navbar - Taille mobile

--> IMAGE DE LA DISPOSITION DE LA NAVBAR EN TAILLE MOBILE

#### 3.3. Layout - Section principale

--> IMAGES DE LA SECTION PRINCIPALE AVEC ET SANS ABONNEMENTS POUR TOUTES LES TAILLES

L'utilisateur arrive sur l'accueil. Autrement dit le feed principal où s'affichent les annonces publiées par les autres utilisateurs. Les annonces peuvent être celles publiées par les abonnés/abonnements ou peuvent être celles proposées par le système de recommandation. L'utilisateur a la possibilité de scroller vers le bas afin de faire défiler le feed et consulter les annonces. Le feed est configuré via un système de recommandation que l'on retrouve en tant que service sur AWS et nommé Amazon Personalize et qui prend en compte une multitude de paramètres liés à l'utilisateur et l'écosystème.

Comme l'utilisateur n'a pas d'abonnés ni d'abonnements initialement, il a la possibilité, grâce à l'apparition d'un component situé sur la partie superieur de la section où se situe le feed et qui normalement contient le flux des storys des abonnements, de cliquer sur un bouton afin de changer le contenu du flux principale en dessous et s'abonner à d'autres utlisateurs via suggestion ou d'inviter ses contacts. D'ajouter des ami(e)s qui lui sont suggerés en fonction des données transmises ou du système de suggestion, qu'il faudra également configuré. Mais il peut également inviter ses contacts à rejoindre l'application.

##### 3.3.1. Layout Section principale - Taille desktop

##### 3.3.2. Layout Section principale - Taille Tablette

##### 3.3.3. Layout Section principale - Taille Mobile

--> IMAGE DU FLUX DE SUGGESTION
--> IMAGE DE L'INVITATION DES AMIS ET SUGGESTION ET POPUP DE DEMANDE D'ACCÈS AUX CONTACTS POUR LA VERSION MOBILE

#### 3.4. Layout - Section secondaire

--> IMAGE DE LA SECTION SECONDAIRE DE SUGGESTION D'AMIS ET PROFIL PERSO

Cette section comporte trois parties, une avec la photo profil de l'utilisateur et son nom d'utilisateur. Il peut cliquer dessus pour accéder à son propre profil. La deuxième en dessous liste un extrait des profils (photo profil et nom d'utilisateurs) d'autres utilisateurs et la troisième en dessous liste un extrait de communautés auxquelles il peut également demander de s'abonner affiché de la même façon. Comme dit précédemment, cette section n'est pas visible sur la version taille tablette et mobile.

### Feed principal (Accueil) UX/UI

## Fonctionnalités

### Authentication & KYC

### Boutique

### Chat

### Communautés

### Comparateur

### Dashboard

### Explorer

### Feed

### Liste d'abonnés et d'abonnements

### Panier

### Publication de réels et stories

### Système de promotion et de publicités pour les produits à vendre

## Installation et déploiement

## Contributions

## Licences et crédits

En résumé :

- Accueil : via l'icône home avec un service feed personnalisé en fonction d'un système de recommandation. J'aimerais utiliser initialement celui d'Amazon, Amazon Personalize. Si je ne me trompe pas, il permet de mettre en place un système de recommandation. Ce feed se composera d'annonces postées par les utilisateurs et les abonnements de l'utilisateur.
- Explorer : accès au marketplace global via l'icône explorer pour la recherche active des produits. Affiche en vrac des images ou vidéos d'annonces en fonction du système de recommandation, mais permet aussi de faire une recherche simple ou une recherche complexe via le choix de catégories de produit, localisation, dimensions, fourchette de prix.
- Recherche : accessible via l'icône de la loupe pour rechercher d'autres utilisateurs en fonction de leur nom, prénom, nom d'utilisateur, etc.
- Boutique : via l'icône boutique personnalisée qui n'est pas le profil de l'utilisateur mais qui affiche les annonces de produits que celui-ci met en vente.
- Panier : via l'icône panier qui regroupe les produits qu'il a mis dedans.
- Dashboard : via l'icône dashboard qui permet de visualiser ses ventes, la liste des produits qu'il vend, éditer ses annonces.
- Annonces : créer de nouvelles annonces via le menu icône + comme sur Instagram.
- Messagerie : pour communiquer avec les autres utilisateurs via le menu icône avion en papier.
- Profil : utilisateur via l'icône photo de profil sur lequel il y a sa photo de profil, etc. Comme sur Instagram, mais nous allons changer le contenu de ce qu'on trouve sur le profil pour les abonnés et ce qu'on y trouve pour l'utilisateur lui-même.
- Communautés : unique via l'icône communauté. Les communautés seront uniques et par région avec des règles de gouvernance imposées par Pazar. Nous ne voulons pas 400 communautés qui parlent de chasse et de pêche, par exemple, mais une seule par région. Non hiérarchique mais structuré en arborescence.
- Paramètres : via l'icône roue dentée pour éditer le nom d'utilisateur, son mot de passe, gérer son compte en général.
- Mode sombre et clair.
- Notifications : via l'icône de notification en cas d'ajout d'abonnement, etc.

Le autres fonctionnalités sont liés a chacun des services :

- Système de recommandation annonces et suggestions d'amis ou de communauté
- Système de paiement groupé avec distribution vers les vendeurs
- Sécurité des paiements
- Catégorisation de produit pour la rechercher et le postage d'annonce. Catégorisation exhaustive avec choix des dimensions et identification de produit ou de biens pour connaitre les caractéristiques.
- Calculs des frais de livraison en fonction du pays et des caractéristiques du produit.
- Confirmation d'envoi du colis avec identification du produit et suivi. Voir lien avec la poste.
- Sécurité de la livraison, choix de la livraison en main propre ou autre
- Système de mise aux enchères.
- Feed personnalisé pour les communautés
- Commentaires, likes, partages des annonces, signaler, possibilité de noter le vendeur en cas d'achat avec justification de la note, et autres modes d'interaction avec les annonces.
- Un chat avec la possibilité d'envoyer des pièces jointes
- Graphiques , données, comptabilisation pour le dashboard
- Liste d'abonnements et d'abonnés
- Générateur de contrat avec signature électronique
