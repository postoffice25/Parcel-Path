import random
from django.db import models
# Create your models here.
class USER(models.Model):
    STATUS = (
        ('applied', 'Applied'),
        ('approved', 'Approved'),
        ('reject', 'Reject')
    )
    status = models.CharField(max_length=20, choices=STATUS, default='applied')
    username = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # ImageField configuration
    password = models.CharField(max_length=8)
    address = models.CharField(max_length=100)
    pincodeno = models.IntegerField()
    districtname = models.CharField(max_length=100)
    otp = models.IntegerField(null=True, blank=True)  # Store OTP for verification


    def generate_otp(self):
        self.otp = random.randint(100000, 999999)  # Generate 6-digit OTP
        self.save()
        return self.otp
class postman(models.Model):
    postman_id=models.IntegerField()
    name=models.CharField(max_length=255, null=False)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField(unique=True)
    image = models.ImageField(upload_to='postman_images/',blank=True,null=True)
    postoffice_name=models.CharField(max_length=100)
    #username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    otp = models.IntegerField(null=True, blank=True)  # Store OTP for verification


    def generate_otp(self):
        self.otp = random.randint(100000, 999999)  # Generate 6-digit OTP
        self.save()
        return self.otp
    
    
    
    
    
class postmodel(models.Model):
    post_id=models.IntegerField()
    parcel_id = models.IntegerField(unique=True)
    postoffice_choices=(
        ('mainpostoffice','Main_postoffice'),
        ('subpostoffice','Sub_postoffice')
    )
    postoffice=models.CharField(max_length=20,choices=postoffice_choices)
    sendername=models.CharField(max_length=100)
    sender_address=models.CharField(max_length=100)
    sender_contact = models.IntegerField(null=True, blank=True)
    receivername=models.CharField(max_length=100)
    receiver_address=models.CharField(max_length=100)
    receiver_email=models.EmailField(blank=True,null=True)
    receiver_postoffice=models.CharField(max_length=100)
    receiver_contact=models.IntegerField()
    posted_date=models.DateField()
    remarks=models.CharField(max_length=200)
    status_choices=(
        ('itempacked','item_packed'),
        ('itemdispatched','item_dispatched'),
        ('itemoutfordelivery','item_outfordelivery'),
        ('itemdelivered','item_delivered'),
        ('doorclosed', 'door_closed'),
        ('returned' , 'returned'),
        ('rescheduled','rescheduled')
    )
    status=models.CharField(max_length=100,choices=status_choices)
    weight=models.IntegerField()
    kms=models.IntegerField()
    price=models.IntegerField()
    screenshot=models.ImageField(upload_to='images/',blank=True,null=True)
    postman_name=models.CharField(max_length=100)
    reschedule_status=models.BooleanField(default=False,blank=True,null=True)
class Feedback(models.Model):
    RATING_CHOICES=[
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    feedback_text=models.TextField()
    rating=models.IntegerField(choices=RATING_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Rating: {self.rating},Feedback: {self.feedback_text[:50]}..."
#class price(models.Model):
   #weight_upto=models.IntegerField()
   #price=models.IntegerField()
   #Description=models.CharField(max_length=200)
class stamp(models.Model):
   cost=models.IntegerField()
   weight=models.IntegerField()
   stamp_name=models.CharField(max_length=100)
   image=models.ImageField(upload_to='images/',blank=True,null=True)
   description=models.CharField(max_length=100)
   release_date=models.DateField()
   status=models.CharField(max_length=100)
class postoffice(models.Model):
   postoffice_id=models.IntegerField()
   postoffice_name=models.CharField(max_length=100)
   image=models.ImageField(upload_to='images/',blank=True,null=True)
   district=models.CharField(max_length=100)
   description=models.CharField(max_length=200)
   stationmaster=models.CharField(max_length=100)
   contact=models.IntegerField()
   email=models.EmailField()
class Reschedule(models.Model):
    parcel = models.ForeignKey(postmodel, on_delete=models.CASCADE, to_field='parcel_id')
    rescheduled_date=models.DateField()
    is_approved=models.BooleanField(default=False)
    payment_status=models.BooleanField(blank=True,null=True,default=False)
    razorpay_order_id=models.CharField(max_length=20,blank=True,null=True)
    
