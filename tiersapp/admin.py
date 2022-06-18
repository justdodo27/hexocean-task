from django.contrib import admin
from .models import ThumbnailType, Tier

# Register your models here.

@admin.register(ThumbnailType)
class ThumnbnailAdmin(admin.ModelAdmin):
    fields = ('name', 'height')
    list_display = ('name',)

class ThumbnailsInline(admin.StackedInline):
    model = Tier.thumbnails.through

@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    fields = ('name', 'original_link_visible', 'expireable')
    list_display = ('name',)
    inlines = [ThumbnailsInline]
    exclude = ('thumbnails',)
