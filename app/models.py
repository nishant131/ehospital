from django.db import models

#ate your models here.
class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    patient_disease = models.CharField(max_length=100)
    patient_Mobileno = models.CharField(max_length=10)
    patient_address = models.CharField(max_length=100)
    patient_email = models.CharField(max_length=100)

class Medicine(models.Model):
    expirydate = models.DateField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    medicine_name = models.CharField(primary_key=True,max_length=100)

class Employee(models.Model):
    e_id = models.CharField(primary_key=True,max_length=20)
    e_password = models.CharField(max_length=8)
    e_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    Mobile_no = models.CharField(max_length=10)
    e_address = models.CharField(max_length=100)
    e_type = models.CharField(max_length=100)

class WorkingHours(models.Model):
    e_id = models.ForeignKey('Employee',on_delete='true')
    NoOfWorkinghours = models.IntegerField()

class Doctor(models.Model):
    designation = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    d_name = models.CharField(max_length=100,primary_key=True)

class Salary(models.Model):
    e_id = models.ForeignKey('Employee',on_delete='true')
    NoOfWorkinghours = models.IntegerField()

class Bill(models.Model):
    patient_id = models.ForeignKey('Appointment', on_delete='true')
    medicine_bill = models.IntegerField()
    others = models.IntegerField()

class Appointment(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    date = models.DateField()
    patient_address = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)