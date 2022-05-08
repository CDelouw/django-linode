from django.db import models
from django.core.validators import MaxValueValidator, MaxLengthValidator


class WorkModel(models.Model):
    # blank=True -> Field is not compulsory
    type_job = models.IntegerField()  # 1:Construction, 2:Cleaning, 3:Other
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)  # ToDo: use phonenumber_field
    salary = models.FloatField(validators=[MaxValueValidator(99.99)], blank=True,)
    language_french = models.BooleanField(blank=True)
    language_english = models.BooleanField(blank=True)
    language_dutch = models.BooleanField(blank=True)
    drivers_license = models.BooleanField(blank=True)
    description = models.TextField(max_length=1000, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (
            f"Tipo {self.type_job}, em {self.date} {self.name} {self.contact}, procura por um {self.profession}, pagando "
            f"€{self.salary} a hora"
        )
