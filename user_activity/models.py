from django.db import models

class EmailSubscription(models.Model):
    email = models.EmailField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.email)

class Newsletter(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class FAQ(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class TermsCondition(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1500, blank=False)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class StoreInfo(models.Model):    
    about = models.TextField(max_length=2000)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.address
    class Meta:
        verbose_name_plural = 'StoreAddress'

class ContactUs(models.Model):
    name = models.CharField(max_length=40,blank=False)
    email = models.EmailField(max_length=50)
    subject = models.EmailField(max_length=50,blank=False)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us"
