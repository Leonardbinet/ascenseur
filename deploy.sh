#!/bin/bash


#PREPROCESSING
echo -e "\n \n ### PREPROCESSING \nLancement du déploiement du site ascenseur"
echo -e "Vous avez lancé $0 avec $# paramètres \n"

onyva=1

## VERIF 1 VARIABLES ENVIRONNEMENT
echo -e "Préparation 1: \nVérification de la variable d'environnement DJANGO_SETTINGS_MODULE: dev ou prod?"
if [ -z $DJANGO_SETTINGS_MODULE ];
then
  echo "Il n'y a malheureusement pas de variable d'environnement nommée \$DJANGO_SETTINGS_MODULE";
  onyva=0
else
  echo "Nous sommes dans un environnement de type: \$DJANGO_SETTINGS_MODULE = $DJANGO_SETTINGS_MODULE";
fi
echo -e ''

## VERIF 2 ENVIRONNEMENT PYTHON
echo -e "Préparation 2: \nVérification de l'environnement python"
if [ ! -z $WORKON_HOME ]
then
  echo -e "Il semble que virtualenvwrapper est installé."
  if [ ! -z $VIRTUAL_ENV ]
  then
    echo -e "Et que nous sommes dans l'environnement $VIRTUAL_ENV."
  else
    echo -e "Je n'ai pas trouvé l'environnement utilisé."
    onyva=0
  fi
else
  echo -e "Je n'ai pas trouvé d'environnement virtual, êtes vous sûr que
  virtualenvwrapper est utilisé, ou Anaconda?"
  onyva=0
fi
## VERIF DES REQUIREMENTS : a voir: http://www.pindi.us/blog/automating-pip-and-virtualenv-shell-scripts


## VERIF 3 AVANCEMENT BRANCHES GIT http://stackoverflow.com/questions/3258243/check-if-pull-needed-in-git
echo -e "Préparation 3: \nVérification des branches de GIT"

# VERIF PRESENCE D'UN REPO, et mise à jour
DIRECTORY=.git
if [ ! -d "$DIRECTORY" ]; then
  echo "Il n'y a pas de dossier .git dans ce répertoire."
else
  echo "Le dossier .git existe, lancement d'une requête 'git remote update'"
  git remote update
fi

#
UPSTREAM=${1:-'@{u}'}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")
echo $LOCAL $REMOTE $BASE
if [ $LOCAL = $REMOTE ]; then
    echo "A jour"
    onyva=0

elif [ $LOCAL = $BASE ]; then
    echo "Besoin de mettre à jour"
elif [ $REMOTE = $BASE ]; then
    echo "Besoin de push"
    onyva=0
else
    echo "Divergence entre branches"
    onyva=0
fi

echo -e '\n##### FIN PREPROCESSING #####\n'


### ARRET DU PROGRAMME SI TOUT N'EST PAS OK
if [ $onyva == 0 ]
then
  echo "Toutes les conditions ne sont pas requises pour lancer le script"
  kill -INT $$
else
  echo "Tout semble correct pour l'instant"
fi
## REALISATION DES OPERATIONS
echo "1- Git merge sur le master"
git merge origin/master

#si changement de schéma de BDD: réalise les migrations de schéma sur la bdd de production
echo "2- Migration des schémas de base de données."
NEED_MIGRATION=python manage.py showmigrations | grep '\[ \]'
echo "Les migrations à réaliser sont (rien si vide): $NEED_MIGRATION"
if [ $NEED_MIGRATION]
  echo "Application des migrations avec la commande manage.py migrate."
  python manage.py migrate
else
  echo "Il ne semble pas qu'une migration est nécessaire"

echo "3-Rassemblement des fichiers statiques"
#collecte les fichiers statiques, au cas où les fichiers statiques ont changé,
python manage.py collectstatic
