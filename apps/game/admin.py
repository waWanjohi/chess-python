from django.contrib import admin

from apps.game.models import Capture, Game, Move


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    pass


@admin.register(Capture)
class CaptureAdmin(admin.ModelAdmin):
    pass
