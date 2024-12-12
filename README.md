# Pazar 0.0.0

## Présentation

L'objectif de l'application "Pazar" est de fournir une place de marché en ligne sécurisée pour le commerce entre particuliers. Notamment la vente et l'achat de biens entre particuliers. Cette place de marché se présente sous la forme d'un réseau social semblable aux applications déjà existantes. Cependant, tous les utilisateurs doivent passer une procédure de vérification d'identité (KYC) afin de vendre ou d'acheter des produits sur la plateforme. Cette procédure est semblable à celle des applications de trading de cryptomonnaie. L'application répond au besoin croissant de garantir la sécurité des achats et des ventes au sein de relations commerciales de tout type (C2C, B2C, B2B, etc.). Pazar souhaite s'étendre globalement dans le monde afin de promouvoir les circuits économiques courts.

Pazar sera une application multiplatformes que l'on pourra retrouver en tant que webapp avec accès par URL, en application mobile et tablette pour les iOS, Android etc, et d'autres supports si cela est intéressant pour l'expansion du projet. Voici une liste non exhaustive des points abordés dans ce document :

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

Le présent fichier (README) fait office de journal de bord afin de présenter les fonctionnalités de l'application, mais aussi avoir un suivi sur son développement, son déploiement, sa maintenance, sa gestion et sa mise à jour. Des fichiers annexes tels que CONTRIBUTING.md, CHANGELOG.md, ROADMAP.md seront également crées et mis à jour en fonction de l'avancée du projet. README sera le fichier de référence pour l'ensemble de l'application car il permet d'être versionné et d'être consulté de façon dynamique.

## Architecture de l'application

### Déploiement et hébergement

### Bases de données

## Technologies, frameworks, languages, services tiers

## User Experience (UX) & User Interface (UI)

### Introduction WebApp UX/UI

L'expérience utilisateur diffère en fonction de la plateforme sur laquelle l'application est lancée. Ici, nous allons différencier 3 versions d'application. Webapp, iOS et android. D'autres versions pourront être développées ultérieurement. Elles partageront les mêmes données mais il y aura quelques différences en termes d'interface. Ces aspects seront clarifiés dans les explications relatives à l'UI.

La webapp se distingue en 3 tailles et pour chacune des tailles, la dispositon et la visibilité des composants seront différentes pour des question de responsive. Par conséquent, il sera nécessaire de montrer où se trouvent les composants en fonction de chaque taille pour chaque situation. Les tailles en question sont les suivantes :

1. Une taille desktop: ≥ 1025px
2. Une taille tablette: ≥ 481px && ≤ 1024px
3. Une taille mobile: ≤ 480px

Le rendu en fonction des tailles ne devrait pas radicalement différer entre la version webapp taille mobile et la version mobile de l'application.

Par conséquent, ici nous allons aborder chaque étape de l'expérience utilisateur en partant initialement de son inscription jusqu'à l'utilisation de chaque fonctionnalité de l'application pour chaque version de l'application. A savoir les versions webapp et mobile.

Pour chaque utilisation, fonctionnalité ou changement au niveau de l'interface:

- Une maquette de l'interface développée sur figma sera jointe au point.
- Explication de l'expérience de l'utilisateur avec chaque élément de l'interface.
- Redirections et changement en cas de succès ou d'erreurs.

Aussi pour faciliter les choses nous allons à chaque fois montrer la différence en terme de rendu, si il y en a, de la dipositiond des éléments en fonction de la taille.

**Informations importantes:**

Chacun des points susmentionnés sera essentiel afin de choisir les composants à développer, déterminer l'architecture optimale de l'application, faciliter la programmation des tests unitaires et des tests fonctionnels, savoir quels frameworks, langages ou services tiers doivent être utilisés, et isoler les problèmes potentiels liés à la sécurité. Par conséquent cette partie du README sera mise à jour continuellement en fonction des décisions technologiques qui seront prises durant le développement et les mises à jour de l'application.

### 1. Landing page via URL

--> IMAGE LANDING PAGE WEB DESKTOP, MOBILE, TABLETTE

### 2. Inscription

Lors de la première partie de l'inscription, l'utilisateur passera directement par une inscription par email ou numero de téléphone sur le formulaire de l'interface de la landing page. Les étapes sont numérotées ci-dessous. Lorsqu'on passe d'une étape à l'autre cela signifie qu'un évènement ou un déclencheur a eu lieu, tel qu'un clique sur un bouton par exemple.

#### 2.1. Formulaire d'inscription simple

--> IMAGES DE L'INTERFACE FORMULAIRE INSCRIPTION

Suite à la demande d'inscription, l'utilisateur

- Adresse email ou numéro de téléphone (Numéro reconnu selon le lieu de connexion. Choix de l'indicatif si nécessaire)
- Nom
- Prénom
- Date de naissance
- Pays de résidence
- Nom d'utilisateur (avec proposition d'alternative)
- Mot de passe avec conditions (ex: nombre de caractères minimum, chiffres, majuscules, minuscules). Il doit pouvoir enregistrer le mot de passe si il le souhaite et l'authentification à deux facteurs, avec envoie du code par sms ou par email a lieu d'office. Sur mobile, il pourra choisir de se connecter de façon biometrique. Sur ordinateur aussi mais c'est une fonctionnalité propre a la reconnaissance digital sur macbook par exemple.

(Une info est présente sur un component où il doit cocher qui stipule qu'en s'inscrivant, il accepte nos conditions générales d'utilisation et la politique de confidentialité)

#### 2.2. Validation avec code reçu

--> IMAGE DE L'INTERFACE VALIDATION CODE

Un mail ou un sms, en fonction de ce qu'il a entré, lui est envoyé avec un code de vérification afin de finaliser cette première inscription dans l'écosystème et activer le compte. L'utilisateur est face à un component qui lui demande d'entrer le code. Lorsque le code est entré, cette phase de l'inscription est terminée et on peut passer à la suite. A cette étape, nous avons dores et déjà des données sur cet utilisateur confirmé. L'adresse email et/ou le numéro de téléphone.

#### 2.3. KYC - ALL PROCEDURE

INFORMATION : il est possible que pour le KYC l'application fasse appel à un service tiers déjà programmé.

##### 2.3.1 KYC - INFORMATIONS ET CONDITIONS DU KYC

--> IMAGE DE LA PREMIÈRE ÉTAPE DU KYC INFORMATIONS ET CONDITIONS DU KYC

C'est un point central de l'application car ce processus doit être rapide et facile pour l'utilisateur. Autrement dit très pédagogique. Cette partie est très semblable à ce que l'on retrouve sur les plateformes de trading de cryptomonnaies telles que binance ou kraken. L'utilisateur est face à un component qui l'informe que Pazar a pour but de mettre à disposition de ses utilisateurs un réseau social commercial afin que les utilisateurs puissent acheter et vendre de façon sécurisée et vérifiée. Par conséquent, il est essentiel que chaque utilisateur vérifie son identité. Un lien vers la politique de confidentialité est présent afin que les utilisateurs sache de quelle façon les données sont traitées.

##### 2.3.2 KYC - FORMULAIRE D'INSCRIPTION COMPLET

--> IMAGE DE LA DEUXIÈME ETAPE DU KYC > FORMULAIRE

L'utilisateur arrive face à un componant qui contient un formulaire muni d'un bouton suivant. Ce formulaire est la première étape du KYC, si il n'est pas dûment rempli, l'utilisateur ne peut pas poursuivre en cliquant sur le bouton suivant et un message d'erreur demandant de remplir correctement le formulaire s'affiche. Tous les champs sont obligatoires initialement. Il est demandé au client de remplir le formulaire dans lequel les champs sont les suivants : nom et prénoms (au pluriel) tels qu'inscrits sur sa carte d'identité ou permis de conduire, son pays de résidence, son adresse, code postale, ville et numero de téléphone.
Si la procédure est interrompue avant la fin, une sauvegarde de l'état et de l'étape du processus d'inscription a lieu et si il revient sur l'appli, il pourra poursuivre son inscription où il en était avec un message qui lui dira "Vous êtes de retour pour finaliser votre inscription etc...".

##### 2.3.3. KYC - UPLOAD ID CARD OR LICENSE

--> IMAGE DE LA TROISIÈME ETAPE DU KYC - UPLOAD DE L'ID

L'utilisateur arrive sur un component qui lui demande de upload une photo de sa carte d'identité nationale ou de son permis de conduire, recto et verso. Une fois cela fait il peut cliquer sur le bouton suivant.

##### 2.3.4 KYC - UPLOAD OFFICAL DOCUMENT & ADRESS VERIFICATION

--> IMAGE DE LA QUATRIÈME ETAPE DU KYC - UPLOAD DE DOCUMENT OFFICIEL

L'utilisateur arrive ensuite, sachant qu'il a fait l'incription sur la webapp, il lui est demandé de fournir la copie d'un document officiel qui prouve qu'il est bien le détenteur de cette identité. Cela n'aura pas lieu sur la version mobile ou si la webapp est sur un navigateur sur mobile ou tablette car la reconnaissance faciale prendra le relai à cette étape là. Donc j'imagine que sur la version webapp desktop, ne seront acceptées que les factures de téléphone ou une facture de l'assurance maladie.

##### 2.3.5 KYC - VERIFICATION EN COURS

--> IMAGE DE LA CINQUIÈME ÉTAPE DU KYC - VÉRIFICATION ET REDIRECTION

L'utilisateur est maintenant face à un component qui charge afin de lui montrer que l'anayse de sa procédure de KYC est en cours. Si il y a une erreur l'état du component change et mentionne à l'utilisateur ce qui ne va pas. Un bouton apparait afin de corriger le point si cela est possible. Si c'est possible, l'utilisateur retourne à l'étape du KYC, clique sur suivant et arrive directement à l'étape suivante qu'il faut corriger ou à la fin de la procédure de KYC où l'analyse a lieu si il n'y a pas d'autres étapes à corriger. Si c'est une erreur qui ne peut être corrigé telle qu'une interdiction quelconque ou légale nous informons l'utilisateur que pour ces raisons nous ne pouvons poursuivre son inscription.
En cas de réussite, le component change d'état, affiche un vu vert ou autre chose qui confirme l'inscription et l'utilisateur est redirigé automatiquement sur l'accueil et l'inscription est finalisée.

### 3. Accueil (Feed)

--> IMAGE DE L'INTERFACE DE L'ACCUEIL

Comme on peut le constater sur l'image, l'interface

- (Icone maison) Accueil
- (Icone globe) Explorer
- (Icone Boutique) Boutique
- (Icone avion papier) Messagerie
- (Icone profile) Profile
- (Icone communauté) Communautés
- (Icon notification) Notifications
- (Icone paramètres) Paramètres

L'utilisateur arrive sur l'accueil. Autrement dit le feed principal où, de la même façon que sur instagram, s'affichent les annonces publiées par les autres utilisateurs. Les annonces peuvent être celles publiées par les abonnés/abonnements ou peuvent être celles proposées par le système de recommandation. L'utilisateur a la possibilité de scroller afin de faire défiler le feed et consulter les annonces. Le feed est configuré via un système de recommandation que l'on retrouve en tant que service sur AWS et nommé Amazon Personalize et qui prend en compte une multitude de parametres liés à l'utilisateur.

Comme l'utilisateur n'a pas d'abonnés ni d'abonnements, l'utilisateur a la possibilité, grâce à l'apparition d'un component situé sur la partie superieur de la section où se situe le feed, qui contient du texte informant de la possibilité de s'abonner à d'autres utlisateurs ou d'inviter ses contacts, d'appuyer sur un bouton afin de trouver des ami(e)s. En cliquant sur le bouton il peut accéder à une partie de l'app où s'affiche une liste d'utilisateurs en fonction du système de suggestion. d'ajouter des ami(e)s qui lui sont suggerés en fonction des données transmises ou du système de suggestion, qu'il faudra également configuré. Mais il peut également inviter ses contacts à rejoindre l'application.

### 2. Webapp taille tablette UX/UI

### 3. Webapp taille mobile UX/UI

### 4. Mobile app UX/UI

### 5. Mobile app UX/UI

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

### Systéme de promotion et de ads pour les produits à vendre

### Wallet
