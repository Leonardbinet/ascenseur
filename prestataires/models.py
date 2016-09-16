# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models


class Type_prestataire(models.Model):
    nom_db= models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    meta_description = models.TextField(max_length=155, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    logo_defaut = models.ImageField(upload_to="logos/categorie/",blank=True,null=True, default=None)
    texte_page = models.TextField(blank=True,default="à remplir")


    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
                #self.slug = slugify(self.name)
        self.slug = slugify(self.nom)
        super(Type_prestataire, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nom



class liste_Prestataires(models.Model):
    nom_db = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.ForeignKey(Type_prestataire)
    slug = models.SlugField(null=True, blank=True)
    meta_description = models.TextField(max_length=155,null=True, blank=True)
    logo = models.ImageField(upload_to="logos/",blank=True,null=True, default=None)

    def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
            self.slug = slugify(self.nom)
            super(liste_Prestataires, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return "/prestataires/"+str(self.slug)

    def __str__(self):
        return self.nom
