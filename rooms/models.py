from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.related import ForeignKey
from core import models as core_models
from django_countries.fields import CountryField
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=120)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Amenity(AbstractItem):
    pass

    class Meta:
        verbose_name_plural = "Amenities"


class Roomtype(AbstractItem):
    pass

    class Meta:
        verbose_name = "Room Type"
        ordering = ["-created"]


class Facility(AbstractItem):
    pass

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    pass

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=120)
    file = models.ImageField()
    room = ForeignKey(
        "Room", on_delete=models.CASCADE
    )  # 파이썬은 수직방향으로 읽기때문에 오류가 생김 , 스트링으로 써줘도 인식 가능

    def __str__(self):
        return self.caption

    class Meta:
        pass


class Room(core_models.TimeStampedModel):
    """Room model"""

    name = models.CharField(max_length=20)
    description = models.TextField()
    country = CountryField()
    city = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField()
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(Roomtype, on_delete=SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)
