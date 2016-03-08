from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models

# Create your models here.


class Type_prestataire(models.Model):
    nom_categorie = models.CharField(max_length=200)
    description = models.TextField()
    def __unicode__(self):
        return self.nom_categorie


class liste_Prestataires(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.ForeignKey(Type_prestataire)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
            self.slug = slugify(self.titre_article)
            super(liste_Prestataires, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom



class pre_Categorie(models.Model):
    name_db = models.CharField(max_length=50)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    def __unicode__(self):
        return self.nom

class pre_Article(models.Model):
    name_db = models.CharField(max_length=50)
    titre_article = models.CharField(max_length=200)
    description = models.TextField()
    body = models.TextField()
    categorie = models.ForeignKey(pre_Categorie)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
            self.slug = slugify(self.titre_article)
            super(pre_Article, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titre_article