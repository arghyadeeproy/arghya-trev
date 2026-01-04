from django.db import models

class Hotels(models.Model):
    property_type = models.CharField(max_length=100)
    property_name = models.CharField(max_length=200)
    place_name = models.CharField(max_length=200)

    price = models.PositiveIntegerField()
    guest_count = models.PositiveIntegerField()
    bedroom_count = models.PositiveIntegerField()
    bathroom_count = models.PositiveIntegerField()

    star_rating = models.PositiveSmallIntegerField(
        choices=[
            (1, '1 Star'),
            (2, '2 Stars'),
            (3, '3 Stars'),
            (4, '4 Stars'),
            (5, '5 Stars'),
        ]
    )

    map_location = models.CharField(max_length=255)

    def __str__(self):
        return self.property_name
