# Pazar

## Présentation du projet

L'objectif de l'application "Pazar" est de fournir une place de marché en ligne sécurisée pour le commerce entre particuliers. Notamment la vente et l'achat de biens entre particuliers. Cette place de marché se présente sous la forme d'un réseau social semblable aux applications déjà existantes. Cependant, tous les utilisateurs doivent passer une procédure de vérification d'identité (KYC) afin de vendre ou d'acheter sur la plateforme. L'application répond au besoin croissant de garantir la sécurité des achats et des ventes au sein de relations commerciales de tout type (C2C, B2C, B2B, etc.). Pazar souhaite s'étendre globalement sur toute la planète afin de promouvoir les circuits économiques courts.

Pazar sera une application multiplatform que l'on pourra retrouver en tant que webapp avec accès par nom de domaine, en application mobile et tablette pour les iOS, Android etc, et d'autres supports si cela est intéressant pour l'expansion du projet.

### Dans ce fichier sont présentés

- L'utilisation dynamique du fichier README en tant que journal de bord
- Les fonctionnalités de l'application
- Les technologies, frameworks et languages utilisés
- Les documents annexes et ce qu'ils contiennent
- L'architecture de l'application
- Les bases de données
- Le déploiement et l'hébergement
- L'UX/UI
- Les services tiers

## Journal de bord

Le présent fichier (README) fait office de journal de bord afin de présenter les fonctionnalités de l'application, mais aussi avoir un suivi sur son développement, son déploiement, sa maintenance, sa gestion et sa mise à jour. Des fichiers annexes tels que CONTRIBUTING.md, CHANGELOG.md, ROADMAP.md seront également crées et mis à jour en fonction de l'avancée du projet. README sera le fichier de référence pour l'ensemble de l'application car l'utilisation du format markdown permet une navigation facilitée entre les différentes parties du projet et le README est également soumis au versioning liés au commits. Il nous est donc simple de suivre les changements qui ont eu lieu au sein du projet.

## Architecture de l'application

### Déploiement et hébergement

### Bases de données

## Technologies, frameworks et languages

## User Experience (UX) et User Interface (UI)

L'expérience utilisateur diffère en fonction de la plateforme sur laquelle l'application est lancée. Ici, nous allons différencier 3 versions d'application. Webapp, iOS et android. D'autres versions pourront être développées ultérieurement. Elles partageront les mêmes données mais il y aura quelques différences en termes d'interface mais ce point sera traité dans la section UI. Les différences en terme d'expérience utilisateur seront traitées ici.

### Version webapp

#### Landing page via URL (ex: pazar.com)

L'utilisateur arrive sur une interface où il lui est demandé de s'inscrire ou de se connecter. Si il choisit de s'inscrire il passe par le processus d'inscription. S'il choisit de se connecter, arrive dans le processus de connexion. Il faut savoir que pour l'un ou pour l'autre nous pourrions faire appel à service tiers pour l'authentication ou le configurer nous même.

#### 1. Processus d'inscription

##### 1.1. Informations

Lors de la première partie de l'inscription, l'utilisateur pourra passer directement par une inscription par email ou numero de téléphone. Les étapes sont numérotées ci-dessous. Lorsqu'on passe d'une étape à l'autre cela signifie qu'un évènement ou un déclencheur a eu lieu tel qu'un clique sur un bouton par exemple. Ainsi, les évènements seront mentionnés de la façon suivante : ==EVENT==

##### 1.2. Formulaire d'inscription simple

- Adresse email ou numéro de téléphone (Numéro reconnu selon le lieu de connexion. Choix de l'indicatif si nécessaire)
- Nom
- Prénom
- Date de naissance
- Pays de résidence
- Nom d'utilisateur (avec proposition d'alternative)

(Une info est présente sur un component où il doit cocher qui stipule qu'en s'inscrivant, il accepte nos conditions générales d'utilisation et la politique de confidentialité)

==CLIQUE BOUTON SUIVANT==

##### 1.3. Validation avec code reçu

Un mail ou un sms, en fonction de ce qu'il a entré, lui est envoyé avec un code de vérification afin de finaliser cette première inscription dans l'écosystème et activer le compte. L'utilisateur est face à un component qui lui demande d'entrer le code. Lorsque le code est entré, cette phase de l'inscription est terminée et on peut passer à la suite. A cette étape, nous avons dores et déjà des données sur cet utilisateur confirmé. L'adresse email et/ou le numéro de téléphone.

==CLIQUE BOUTON VALIDATION===

##### 1.4. KYC

Cette partie est très semblable à ce que l'on retrouve sur les plateformes de trading de cryptomonnaies telle que binance ou kraken. L'utilisateur est face à un component qui l'informe que pazar a pour but de mettre à disposition de ses utilisateurs un réseau social commercial afin que les utilisateurs puissent acheter et vendre de façon sécurisée et vérifiée. Par conséquent, il est essentiel que chaque utilisateur vérifie son identité. Un lien vers la politique de confidentialité est présent afin que les utilisateurs sache de quelle façon les données sont traitées.

==CLIQUE BOUTON SUIVANT==

L'utilisateur arrive face à un componant qui contient un formulaire muni d'un bouton suivant. Ce formulaire est la première étape du KYC, si il n'est pas dûment rempli, l'utilisateur ne peut pas poursuivre en cliquant sur suivant et un message d'erreur demandant de remplir correctement le formulaire s'affiche. Tous les champs sont obligatoires initialement. On changera si c'est nécessaire.

1. Il est demandé au client de remplir un formulaire dans lequel il se doit de nous faire part de son nom et prénoms (au pluriel) tels qu'inscrits sur sa carte d'identité ou permis de conduire. Il doit aussi inscrire son adresse, code postale, ville et numero de téléphone. Ensuite un bouton 

##### 1.5. Accueil (Feed)

L'utilisateur arrive sur l'accueil. Autrement dit le feed principal où, de la même façon que sur instagram, s'affichent les annonces publiées par les autres utilisateurs. Les annonces peuvent être celles publiées par les abonnés/abonnements ou peuvent être celles proposées par le système de recommandation. L'utilisateur a la possibilité de scroller afin de faire défiler le feed et consulter les annonces. Le feed est configuré via un système de recommandation que l'on retrouve en tant que service sur AWS et nommé Amazon Personalize et qui prend en compte énormement de parametres liés à l'utilisateur.

Comme l'utilisateur n'a pas d'abonnés ni d'abonnements, l'utilisateur a la possibilité, grâce à l'apparition d'un component sur la partie superieur de la section où se situe le feed, d'appuyer sur un bouton afin de trouver des ami(e)s et par cela d'accéder à une partie de l'app d'ajouter des ami(e)s qui lui sont suggerés en fonction des données transmises ou du système de suggestion, qu'il faudra également configuré. Mais il peut également inviter ses contacts à rejoindre l'application.

## User Interface (UI)

Sachant qu'il y a deux versions de l'application il faut tenir compte de certains aspects important qui affecteront l'interface. Un premier point concerne la distinction des version web et mobile. La web app sera bien entendu responsive en fonction de la taille de la fenêtre du navigateur et certains composants n'auront pas le même rendu en fonction de la taille. En ce qui concerne la version mobile, celle-ci sera également responsive en fonction de la taille.

## Fonctionnalités

### KYC

### Dashboard

### Feed

### Explorer

### Chat

### Boutique

### Communautés

### Panier

### Wallet

### Comparateur

### Liste d'abonnés et d'abonnements

### Publication de réels et stories

### Systéme de promotion et de ads pour les produits à vendre
