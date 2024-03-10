from django.contrib import admin
from .models import Position,Squad,Adress,Clubs,Matches,Table,Fans,FanPicture
# Register your models here.
admin.site.register(Position)
admin.site.register(Table)
admin.site.register(Squad)
admin.site.register(Adress)
admin.site.register(Clubs)
admin.site.register(Matches)
admin.site.register(Fans)
admin.site.register(FanPicture)