# Mettre en œuvre une base de données sécurisée avec Django ORM et PostgreSQL
## Description

**Epic Events** est une entreprise de conseil et de gestion dans l'événementiel qui souhaite développer un système CRM sécurisé interne à l'entreprise.<br>
Ce logiciel doit permettre aux membres des différentes équipes (gestion, vente et support) de créer et de gérer leurs clients ainsi que les contrats et les évènements liés à ceux-ci.

Ma mission était d'élaborer un diagramme entité-relation (ERD) puis de développer une application devant fournir un ensemble d’endpoints sécurisés pour l’API à l'aide du framework Django REST et d'une base de données PostgreSQL.<br>

L'interface utilisateur a été créée à l'aide du site d'administration Django, celle-ci permet aux utilisateurs autorisés d'effectuer différentes opérations CRUD (créer, lire, mettre à jour et supprimer) appliquées aux divers objets CRM.<br>

## Diagramme ERD
![alt tag](https://github.com/SelHel/Implement_A_Secure_Database_With_Django_ORM_And_PostgreSQL/files/9243575/Helaoui_Selim_1_ERD_072022.pdf)


## Prérequis
* Python 3.9 (lien de téléchargement: <https://www.python.org/downloads>)
* PostgreSQL (lien de téléchargement: <https://www.postgresql.org/download>)


## Installation de l'application

* Cloner le dépôt en utilisant le terminal sous Mac/Linux ou l'invite de commandes sous Windows :<br>

	```
	git@github.com:SelHel/Implement_A_Secure_Database_With_Django_ORM_And_PostgreSQL.git
	```

* Ensuite, placez vous dans le dossier courant :

	```
	cd Implement_A_Secure_Database_With_Django_ORM_And_PostgreSQL-master
	```
* Puis créez votre environnement virtuel :

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

* Installez les dépendances avec la commande suivante :

	```
	pip install -r requirements.txt
	```
* Puis placez vous dans le dossier **epicevents** du projet et créez un fichier settings.ini avec le contenu suivant :
* 
	```
	[settings]
	SECRET_KEY='YOUR SECRET KEY'
	DEBUG=True
	DB_NAME='YOUR DB NAME'
	DB_USER='YOUR PSQL USERNAME'
	DB_PASSWORD='YOUR PSQL PASSWORD'
	DB_HOST='localhost'
	DB_PORT='5432'
	```
* Assurez-vous que PostgreSQL est bien installé sur votre machine et référez vous à [cette documentation](https://www.postgresql.org/docs/) pour le lancement du serveur.

* Dans le SQL Shell vous devez créer la base de données en utilisant le même nom que vous avez indiqué dans le fichier settings.ini :

	```
	CREATE DATABASE 'YOUR DB NAME';
	```
* Ensuite vous devez créer un utilisateur en utilisant le même nom que vous avez indiqué dans le fichier settings.ini :

	```
	CREATE USER 'YOUR PSQL USERNAME' WITH PASSWORD 'YOUR PSQL PASSWORD';
	```
* Pour finir vous devez accorder tous les droits à votre nouvel utilisateur :
   
   ```
   GRANT ALL PRIVILEGES ON DATABASE 'YOUR DB NAME' TO 'YOUR PSQL USERNAME';
   ```

## Exécution de l'application
* Dans le terminal sous Mac/Linux ou l'invite de commandes sous Windows, placez vous dans le dossier de l'application puis activez votre environnement virtuel si ce n'est pas déjà fait :

	```
	<your-virtual-env-name>\Scripts\activate.bat (sous Windows)
	```
	ou
	
	```
	source <your-virtual-env-name>/bin/activate (sous Mac/Linux)
	```

* Ensuite effectuez les migrations de la base de données :

	```
	python manage.py migrate
	```
* Puis Créez un superuser :

	```
	python manage.py createsuperuser
	```

* Enfin lancez le serveur de développement en utilisant la commande :

	```
	python manage.py runserver
	```

## Utilisation du site d'administration de Django
* Seul les SuperUser et les membres de l'équipe de gestion peuvent accéder au site d'administration de Django via cette url :

	```
	 http://localhost:8000/admin/
	```

## Documentation

* Lien vers la documentation Postman de l'API contenant les détails sur chaque point de terminaison et sur les différentes permissions : <https://documenter.getpostman.com/view/20587842/Uze1x4nZ>

## Auteur
**Selim Helaoui**