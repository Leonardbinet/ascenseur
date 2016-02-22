from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models

# Create your models here.


class Type_prestataire(models.Model):
    nom_categorie = models.CharField(max_length=200)
    description = models.TextField()
    def __unicode__(self):
        return self.nom_categorie


class Prestataire(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.ForeignKey(Type_prestataire)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
            self.slug = slugify(self.titre_article)
            super(Prestataire, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom

