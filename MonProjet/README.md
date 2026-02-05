# MonProjet Django

## Description
Site web avec 3 pages : Accueil, À propos, Contact.

## Installation
1. python -m venv venv
2. venv\Scripts\activate  (Windows)
   source venv/bin/activate  (Mac/Linux)
3. pip install django==4.2.0
4. python manage.py migrate
5. python manage.py runserver

## Pages
- Accueil : http://127.0.0.1:8000/
- À propos : http://127.0.0.1:8000/a-propos/
- Contact : http://127.0.0.1:8000/contact/

## Structure
- monapp/ : mon application
- MonProjet/ : configuration
- templates/ : pages HTML
- static/ : CSS

## Structure du projet
MonProjet/
├── monapp/               # Mon application
├── MonProjet/          # Configuration
├── manage.py
├── requirements.txt    # Dépendances
└── README.md          # Ce fichier

## Difficultés rencontrées
- Erreur Python : Résolu en désactivant l'alias Windows

- Templates non trouvés : Résolu en plaçant fichiers dans bon dossier

- Django non installé : Résolu en activant environnement virtuel

- GitHub main/master : Résolu en utilisant master au lieu de main

## Fonctionnalités
- 3 pages web
- Menu de navigation
- Design CSS
- Templates Django

## Structure du projet
MonProjet/
├── monapp/               # Mon application
├── MonProjet/          # Configuration
├── manage.py
├── requirements.txt    # Dépendances
└── README.md          # Ce fichier

## Difficultés rencontrées
- Erreur Python : Résolu en désactivant l'alias Windows

- Templates non trouvés : Résolu en plaçant fichiers dans bon dossier

- Django non installé : Résolu en activant environnement virtuel

- GitHub main/master : Résolu en utilisant master au lieu de main
