from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify


class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    meta_description = models.TextField(max_length=155, null=True, blank=True)
    ordre = models.IntegerField(null=True, blank=True, default=10)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Categorie, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nom


class Question(models.Model):
    question = models.TextField(verbose_name='Votre question',
                                default="Question...")
    question_courte = models.CharField(
        max_length=50, default=None, null=True, blank=True)
    categorie = models.ForeignKey(Categorie, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    meta_description = models.TextField(max_length=155, null=True, blank=True)
    reponse = models.TextField(null=True, blank=True)
    repondue = models.NullBooleanField(default=False)
    affichage = models.NullBooleanField(default=False)
    mail_demande = models.EmailField(
        blank=True, null=True, verbose_name='Votre mail',
        default="exemple@mail.com")
    ordre = models.IntegerField(null=True, blank=True, default=10)

    def get_absolute_url(self):
        return "/questions/"+str(self.slug)

    def save(self, *args, **kwargs):
        if (self.question_courte == "") or (len(self.question_courte) > 47):
            if len(self.question) > 47:
                self.question_courte = self.question[:45]+"..."
            else:
                self.question_courte = self.question
        else:
            pass
        self.slug = slugify(self.question_courte)
        super(Question, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.question
