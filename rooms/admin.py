from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    # list_display = ("name", "used_by",)

    # def used_by(self, obj):
    #     return obj.rooms.count()

    pass


# class PhotoInline(admin.TabularInline):

#     model = models.Photo

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """  """
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass
