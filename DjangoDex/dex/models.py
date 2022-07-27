from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models

# Create your models here.


class ElementType(models.Model):
    name = models.CharField(max_length=30, unique=True)
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
    name = models.CharField(max_length=50, unique=True)
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
        super(Ability, self).save(*args, **kwargs)


class Move(models.Model):
    move_name = models.CharField(max_length=50)
    move_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ["move_name"]

    def __str__(self) -> str:
        return self.move_name

    def get_absolute_url(self):
        return reverse("ability-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.move_name)
        super(Move, self).save(*args, **kwargs)


class MoveByLevel(models.Model):
    learned_level = models.IntegerField()
    learned_move = models.ForeignKey(Move, on_delete=models.CASCADE)

    class Meta:
        ordering = ["learned_level"]

    def __str__(self) -> str:
        return self.learned_move.move_name


class Pokemon(models.Model):
    poke_id = models.IntegerField(null=False, blank=True, unique=True)
    name = models.CharField(max_length=50)
    xp = models.IntegerField()
    image_url = models.URLField()
    poke_url = models.URLField()
    abilities = models.ManyToManyField(Ability)
    hidden_ability = models.ForeignKey(
        Ability,
        on_delete=models.CASCADE,
        null=True,
        related_name="hidden_ability",
    )
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
    max_status = models.IntegerField()

    move_by_level = models.ManyToManyField(MoveByLevel)

    class Meta:
        ordering = ["poke_id"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse(
            "pokemon-detail", kwargs={"slug": self.slug, "poke_id": self.id}
        )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        self.max_status = max(
            self.hp,
            self.attack,
            self.defense,
            self.special_attack,
            self.special_defense,
            self.speed,
        )
        super(Pokemon, self).save(*args, **kwargs)
