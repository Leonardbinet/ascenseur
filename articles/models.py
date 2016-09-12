from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Categorie(models.Model):
    name_db = models.CharField(max_length=50)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    meta_description = models.TextField(max_length=155, null=True)
    def __unicode__(self):
        return self.nom

class Article(models.Model):
    name_db = models.CharField(max_length=50)
    titre_article = models.CharField(max_length=200)
    description = models.TextField()
    body = models.TextField()
    categorie = models.ForeignKey(Categorie)
    slug = models.SlugField()
    meta_description = models.TextField(max_length=155, null=True)

    def get_absolute_url(self):
        return "/articles/"+str(self.slug)

    def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
            self.slug = slugify(self.titre_article)
            super(Article, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titre_article

