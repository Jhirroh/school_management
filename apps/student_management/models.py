from django.db import models
from django_countries.fields import CountryField

class Student(models.Model):
    GENDER_TYPE = (('MALE', 'Male'), ('FEMALE', 'Female'))
    CITIZENSHIP_TYPE = (('SINGLE', 'Single'), ('MARRIED', 'Married'))

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name='Date of Birth')
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    religion = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=10, choices=CITIZENSHIP_TYPE)
    nationality = CountryField()

    def __str__(self):
        if self.middle_name == None:
            return f'{self.last_name}, {self.first_name}'
        else:
            return f'{self.last_name}, {self.first_name} {self.middle_name}'

class Address(models.Model):
    ADDRESS_TYPE = (('CURRENT', 'Current'), ('PERMANENT', 'Permanent'))

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, default='')
    type = models.CharField(max_length=10, choices=ADDRESS_TYPE, unique=True)
    address_1 = models.CharField(max_length=300)
    barangay = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    country = CountryField()

    def __str__(self):
        return f'{self.type} | {self.student.last_name}, {self.student.first_name}'
    

class Dependents(models.Model):
    DEPENDENT_TYPE = (('MOTHER', 'Mother'), ('FATHER', 'Father'), 
                    ('BROTHER', 'Brother'), ('Sister', 'Sister'),
                    ('GUARDIAN', 'Guardian'))

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, default='')
    type = models.CharField(max_length=20, choices=DEPENDENT_TYPE, unique=True)
    name = models.CharField(max_length=300)
    dob = models.DateField(verbose_name='Date of Birth')
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.type} | {self.student.last_name}, {self.student.first_name}'
    

class Education(models.Model):
    EDUCATION_TYPE = (('ELEMENTARY', 'Elementary'), ('SECONDARY', 'Secondary'))

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, default='')
    type = models.CharField(max_length=30, choices=EDUCATION_TYPE, unique=True)
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    year_start = models.IntegerField()
    year_end = models.IntegerField()

    def __str__(self):
        return f'{self.type} | {self.student.last_name}, {self.student.first_name}'