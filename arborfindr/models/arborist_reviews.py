from django.db import models
from .homeowner_model import Homeowner


class ArboristReview(models.Model):
    arborist_company = models.ForeignKey('ArboristCompany', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Homeowner, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, f'{i} Star') for i in range(1,6)], default =3)
    review_text = models.CharField(max_length=250)
    reviewed_on = models.DateTimeField(auto_now_add=True)

    # Metadata for ArboristReview Models
    class Meta:
        db_table = 'arborfindr_arboristreview'

def __str__(self):
        return f'{self.rating} ArboristReview'

        