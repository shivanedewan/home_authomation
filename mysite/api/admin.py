from django.contrib import admin
from .models import Board, Pin

class PinAdmin(admin.ModelAdmin):
    list_display    = ('name', 'pin_no', 'board', 'status')
    search_fields   = ('name', 'pin_no', 'board')
    list_filter     = ('board', 'status')

    ordering        = ('pin_no',)


class PinInline(admin.TabularInline):
    model    = Pin
    extra    = 1
    ordering = ['pin_no', ]
    

class BoardAdmin(admin.ModelAdmin):
    list_display    = ('name', 'id', 'active_pins')
    search_fields   = ('name', 'id')
    inlines         = [PinInline]

    def active_pins(self, obj):
        return obj.pin_set.filter(status=True).count()

admin.site.register(Pin, PinAdmin)
admin.site.register(Board, BoardAdmin)
