from django.contrib import admin
from dex.models import ElementType, Ability, Pokemon

# Register your models here.


class MembershipElemntTypeInline(admin.TabularInline):
    model = Pokemon.types.through
    can_delete: bool = False
    extra = 0


class MembershipAbilitiesInline(admin.TabularInline):
    model = Pokemon.abilities.through
    can_delete: bool = False
    extra = 0


@admin.register(ElementType)
class AdminElementType(admin.ModelAdmin):
    fields = ("name",)
    search_fields = ("name",)
    list_display = ("name",)
    empty_value_display = "-empty-"


@admin.register(Ability)
class AdminAbility(admin.ModelAdmin):
    fields = ("name", "description")
    search_fields = ("name",)
    list_display = ("name",)
    empty_value_display = "-empty-"


@admin.register(Pokemon)
class AdminPokemon(admin.ModelAdmin):

    fieldsets = [
        (
            None,
            {
                "fields": (
                    "poke_id",
                    "name",
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
                    "height",
                    "weight",
                ),
            },
        ),
        (
            "Abilities",
            {
                "fields": ("hidden_ability",),
            },
        ),
    ]

    inlines = [
        MembershipAbilitiesInline,
        MembershipElemntTypeInline,
    ]
    search_fields = ("poke_id", "name", "types", "abilities")
    list_display = ("name", "poke_id")
    empty_value_display = "-empty-"
