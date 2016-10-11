from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify


class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    meta_description = models.TextField(max_length=155, blank=True)

    def __unicode__(self):
        return self.nom


class Article(models.Model):
    titre_article = models.CharField(max_length=300)
    titre_court = models.CharField(max_length=60, blank=True, default=None,
                                   null=True)
    description = models.TextField()
    body = models.TextField()
    categorie = models.ForeignKey(Categorie)
    slug = models.SlugField(null=True, blank=True)
    meta_description = models.TextField(max_length=155, blank=True)

    def get_absolute_url(self):
        return "/articles/" + str(self.slug)

    def save(self, *args, **kwargs):
        if (self.titre_court == "") or (len(self.titre_court) > 47):
            if len(self.titre_article) > 47:
                self.titre_court = self.titre_article[:45] + "..."
            else:
                self.titre_court = self.titre_article
        else:
            pass
        self.slug = slugify(self.titre_court)
        super(Article, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titre_article
