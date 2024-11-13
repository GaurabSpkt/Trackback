import os
import cv2
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from decouple import config

class ItemLost(models.Model):
    ItemID = models.AutoField(primary_key=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    found = models.BooleanField(default=False)
    location = models.TextField(max_length=100)
    lost_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='findme/images', default="")
    found_location = models.CharField(max_length=100, null=True, blank=True)
    item_found_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                      related_name="item_found_user")
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Added field
    email = models.EmailField(blank=True, null=True)  # Added field

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = cv2.imread(self.image.path, cv2.IMREAD_COLOR)
            down_width = 1000
            down_height = 1000
            down_points = (down_width, down_height)
            resized_down = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)
            cv2.imwrite(self.image.path, resized_down)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
