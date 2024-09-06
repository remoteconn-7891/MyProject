from django.db import models
from .arborist_model import Arborist
from .homeowner_model import Homeowner


class ArboristReview(models.Model):
    arborist = models.ForeignKey(Arborist, on_delete=models.CASCADE)
    user = models.ForeignKey(Homeowner, on_delete=models.CASCADE)
    one_star = models.PositiveIntegerField(default=0, null=True, blank=True)
    two_stars = models.PositiveIntegerField(default=0, null=True, blank=True)
    three_stars = models.PositiveIntegerField(default=0, null=True, blank=True)
    four_stars = models.PositiveIntegerField(default=0, null=True, blank=True)
    five_stars = models.PositiveIntegerField(default=0, null=True, blank=True)
    review_by_homeowner = models.CharField(max_length=300)

    # Metadata for ArboristReview Models

    def __str__(self):
        return f'{self.user.one_star} ArboristReview'

        