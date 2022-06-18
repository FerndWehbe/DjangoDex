from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models

# Create your models here.


class ElementType(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("element_type-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(ElementType, self).save(*args, **kwargs)


class Ability(models.Model):
    name = models.CharField(max_length=50)
    hidden = models.BooleanField()
    slug = models.SlugField(null=False, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("ability-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(ElementType, self).save(*args, **kwargs)


class Pokemon(models.Model):
    id = models.IntegerField(
        primary_key=True, null=False, blank=True, unique=True
    )
    name = models.CharField(max_length=50)
    xp = models.IntegerField()
    image_url = models.URLField()
    poke_url = models.URLField()
    abilities = models.ManyToManyField(Ability)
    types = models.ManyToManyField(ElementType)
    height = models.IntegerField()
    weight = models.IntegerField()
    slug = models.SlugField(null=False, unique=True)
    ## Stats
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse(
            "pokemon-detail", kwargs={"slug": self.slug, "id": self.id}
        )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Pokemon, self).save(*args, **kwargs)
