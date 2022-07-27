from dex.models import ElementType, Ability, Pokemon, Move, MoveByLevel
from django.contrib import admin


class MembershipElemntTypeInline(admin.TabularInline):
    model = Pokemon.types.through
    can_delete: bool = False
    extra = 0


class MembershipAbilitiesInline(admin.TabularInline):
    model = Pokemon.abilities.through
    can_delete: bool = False
    extra = 0


class MembershipMoveByLevelInline(admin.TabularInline):
    model = Pokemon.move_by_level.through
    fields = [
        "move_level",
        "move_name",
    ]
    readonly_fields = [
        "move_level",
        "move_name",
    ]
    can_delete: bool = False
    extra = 0

    def move_level(self, obj):
        return obj.movebylevel.learned_level

    def move_name(self, obj):
        return obj.movebylevel.learned_move.move_name


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
                    "max_status",
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

    search_fields = (
        "poke_id",
        "name",
        "types__name",
        "abilities__name",
    )
    inlines = [
        MembershipAbilitiesInline,
        MembershipElemntTypeInline,
        MembershipMoveByLevelInline,
    ]
    list_display = (
        "name",
        "poke_id",
    )
    empty_value_display = "-empty-"


@admin.register(Move)
class AdminMoves(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": (
                    "move_name",
                    "move_description",
                    "category",
                    "power",
                    "accuracy",
                    "pp",
                    "probability",
                    "element_type",
                )
            },
        ),
    ]

    list_display = (
        "move_name",
        "move_description",
    )
    search_fields = ("move_name",)
    empty_value_display = "-empty-"


@admin.register(MoveByLevel)
class AdminMovesByLevel(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": (
                    "learned_level",
                    "learned_move",
                ),
            },
        )
    ]

    list_display = (
        "learned_level",
        "get_name",
    )
    search_fields = (
        "learned_level",
        "learned_move__move_name",
    )
    empty_value_display = "-empty-"

    @admin.display
    def get_name(self, obj):
        return obj.learned_move.move_name
