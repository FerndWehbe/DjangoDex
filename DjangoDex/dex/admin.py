from django.contrib import admin
from dex.models import ElementType, Ability, Pokemon

# Register your models here.


class MembershipElemntTypeInline(admin.TabularInline):
    model = Pokemon.types.through
    fields = (
        "name",
        "types",
    )
    # readonly_fields = fields
    extra = 0


class MembershipAbilitiesInline(admin.TabularInline):
    model = Pokemon.abilities.through
    fields = ("name", "abilities", "hidden")
    # readonly_fields = fields
    extra = 0


@admin.register(ElementType)
class AdminElementType(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
    empty_value_display = "-empty-"


@admin.register(Ability)
class AdminAbility(admin.ModelAdmin):
    search_fields = ("name", "hidden")
    list_display = ("name",)
    empty_value_display = "-empty-"


@admin.register(Pokemon)
class AdminPokemon(admin.ModelAdmin):

    fieldsets = [
        (
            None,
            {
                "fields": (
                    "name",
                    "types",
                    "hp",
                    "attack",
                    "defense",
                    "special_attack",
                    "special_defense",
                    "speed",
                )
            },
        ),
        (
            "Advanced options",
            {
                "classes": ("collapse",),
                "fields": (
                    "xp",
                    "image_url",
                    "poke_url",
                    "abilities",
                    "height",
                    "weight",
                ),
            },
        ),
    ]

    inlines = [
        MembershipElemntTypeInline,
        MembershipAbilitiesInline,
    ]
    search_fields = ("id", "name", "types", "abilities")
    list_display = ("id", "name")
    empty_value_display = "-empty-"
