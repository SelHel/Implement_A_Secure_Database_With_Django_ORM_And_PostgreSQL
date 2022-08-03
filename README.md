# Mettre en œuvre une base de données sécurisée avec Django ORM et PostgreSQL
## Description

**Epic Events** est une entreprise de conseil et de gestion dans l'événementiel qui souhaite développer un système CRM sécurisé interne à l'entreprise.<br>
Ce logiciel doit permettre aux membres des différentes équipes (gestion, vente et support) de créer et de gérer leurs clients ainsi que les contrats et les évènements liés à ceux-ci.

Ma mission était d'élaborer un diagramme entité-relation (ERD) puis de développer une application devant fournir un ensemble d’endpoints sécurisés pour l’API à l'aide du framework Django REST et d'une base de données PostgreSQL.<br>

L'interface utilisateur a été créée à l'aide du site d'administration Django, celle-ci permet aux utilisateurs autorisés d'effectuer différentes opérations CRUD (créer, lire, mettre à jour et supprimer) appliquées aux divers objets CRM.<br>

## Diagramme ERD
![alt tag](https://github.com/SelHel/Implement_A_Secure_Database_With_Django_ORM_And_PostgreSQL/files/9243575/Helaoui_Selim_1_ERD_072022.pdf)

## Documentation

* Lien vers la documentation Postman de l'API, contenant des détails sur chaque point de terminaison : <https://documenter.getpostman.com/view/20587842/Uze1x4nZ>

## Prérequis
* Python 3.9 (lien de téléchargement: <https://www.python.org/downloads>)
* PostgreSQL (lien de téléchargement: <https://www.postgresql.org/download>)

## Base de données

La base de données contient les tables suivantes :

* Clients (stock les données des clients)
* Contracts (stock les données des contrats liés aux clients)
* Events (stock les données des évènements liés aux contrats)
* Users (stock les données des utilisateurs)

## Installation de l'application

* Cloner le dépôt en utilisant le terminal sous Mac/Linux ou l'invite de commandes sous Windows :<br>

	```
	git clone https://github.com/SelHel/Implement_A_Secure_Database_With_Django_ORM_And_PostgreSQL.git
	```

* Ensuite, placez vous dans le dossier courant :

	```
	cd Implement_A_Secure_Database_With_Django_ORM_And_PostgreSQL-master
	```
* Puis créez un environnement virtuel :

	```
	python -m venv <your-virtual-env-name>
	```

* Activez votre environnement virtuel :

	```
	<your-virtual-env-name>\Scripts\activate.bat (sous Windows)
	```
	ou
	
	```
	source <your-virtual-env-name>/bin/activate (sous Mac/Linux)
	```

* Installer les dépendances avec la commande suivante :

	```
	pip install -r requirements.txt
	```
## Exécution de l'application
* Pour exécuter l'application toujours dans le terminal sous Mac/Linux ou l'invite de commandes sous Windows lancez le serveur de développement en utilisant la commande :

	```
	python manage.py runserver
	```

* Pour accéder à la page d'accueil et naviguer dans l'application coller cette adresse dans votre navigateur :
	
	```
	http://127.0.0.1:8000/
	```
* Pour accéder au site d'administration de Django et pouvoir effectué des opérations CRUD coller cette adresse dans votre navigateur :

	```
	 http://127.0.0.1:8000/admin/
	```
* Connectez-vous en utilisant le nom d'utilisateur `admin` et le mot de passe `admin`.

## Auteur
**Selim Helaoui**