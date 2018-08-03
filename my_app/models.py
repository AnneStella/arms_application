from django.db import models


# Create your models here.
# class ProfileInfo(models.Model):
#     user = models.OneToOneField(on_delete=models.CASCADE)

class Application(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=500)
    email = models.CharField(max_length=350)
    phone = models.IntegerField()
    address = models.CharField(max_length=400)
    university = models.CharField(max_length=100)
    course = models.CharField(max_length=700)
    essay = models.TextField(max_length=750)
    resume = models.FileField()
    cover_letter = models.FileField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.first_name + self.last_name + self.email + self.phone + self.address + self.university + self.course + self.essay + self.resume + self.cover_letter
