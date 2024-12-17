from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kursning nomi")
    description = models.TextField(verbose_name="Kursning tavsifi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Oxirgi tahrirlangan vaqti")

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Talabaning ismi")
    email = models.EmailField(unique=True, verbose_name="Email manzili")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan vaqti")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students", verbose_name="Kurs")

    def __str__(self):
        return self.name