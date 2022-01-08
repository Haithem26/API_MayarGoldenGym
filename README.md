# wf_investissement
wf_investissement
env\Scripts\activate.bat
python -m pip install django
django-admin startproject workflow
python -m pip install mysql
python manage.py migrate
python manage.py createsuperuser
python -m pip install djangorestframework
python -m pip install django

python manage.py runserver
python manage.py startapp investissement


1/Creation d'un endpoint pour ajouter/modifier/supprimer un evennement spécial
    id de l'évennement
    nom de l'évennement
    photo de l'évennement
    description de l'évennemen
2/ Creation d'un endpoint pour ajouter/modifier/suprrimer un cours
    id
    titre,
    description
    photo

3/ Modifier les tarfis qui se trouve dans la page Tarifs

4/Ajouter un systeme d'authentification 

    