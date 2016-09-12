from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify


class Categorie(models.Model):
    name_db = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    meta_description = models.TextField(max_length=155, null=True)
    def __unicode__(self):
        return self.nom

class Question(models.Model):
    name_db = models.CharField(max_length=50, primary_key=True)
    question = models.TextField()
    categorie = models.ForeignKey(Categorie, null=True)
    slug = models.SlugField(null=True)
    meta_description = models.TextField(max_length=155, null=True)
    reponse = models.TextField(null=True)
    repondue = models.NullBooleanField(default=False)
    affichage = models.NullBooleanField(default=False)

    def get_absolute_url(self):
        return "/questions/"+str(self.slug)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.titre_article)
            super(Question, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.question