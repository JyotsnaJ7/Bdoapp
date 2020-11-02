from django.db import models
import datetime
# from django.core.exceptions import ValidationError

# Create your models here.
class Lead(models.Model):
    leadId = models.CharField(max_length=50,unique=True,blank=False,help_text='Add unique Lead Id')
    leadName = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,unique=True,blank=False)
    phone1 = models.CharField(max_length=12,unique=True)
    choice = (
        ('Open', 'Open'),
        ('Open-Attempted to Contact', 'Open-Attempted to Contact'),
        ('Open-In Contact', 'Open-In Contact'),
        ('Closed-Succesfully', 'Closed-Succesfully'),
        ('Closed-Not Relevant', 'Closed-Not Relevant')
    )
    status = models.CharField(max_length=30, choices=choice,blank=False)
    picture = models.ImageField(upload_to='images',blank=False)
    company = models.CharField(max_length=100,blank=False)
    contactPerson = models.CharField(max_length=100,blank=False)
    location = models.CharField(max_length=200,blank=False)
    leadRegisterDate = models.DateField(null=True,blank=False)
    phone2 = models.CharField(max_length=12,unique=True)
    websiteAddress = models.URLField(max_length=200,unique=True,blank=False)
    leadSource = models.CharField(max_length=100,blank=False)
    leadIndustry = models.CharField(max_length=100,blank=False)
    leadtype_choice = (
        ('Architecture Consultant', 'Architecture Consultant'),
        ('Client', 'Client')
    )
    leadType = models.CharField(max_length=30, choices=leadtype_choice,blank=False)
    officeAddress = models.CharField(max_length=200,blank=False)
    additionalNotes = models.TextField(max_length=100,blank=False)
    followupDate = models.DateField(default=datetime.date.today(),blank=False)
    # def save(self,*args,**kwargs):
    #     if self.date<datetime.date.today():
    #         raise ValidationError('The date cannot be in the past!')
    #     super(Event,self).save(*args,**kwargs)
    contact_choice = (
        ('Phone', 'Phone'),
        ('E-mail', 'E-mail'),
        ('Direct Meeting', 'Direct Meeting')
    )
    contactSource = models.CharField(max_length=30, choices=contact_choice,blank=False)
    description = models.CharField(max_length=200,blank=False)
    notes = models.CharField(max_length=200,blank=False,help_text='Extra notes')

    def __str__(self):
        return self.leadName
