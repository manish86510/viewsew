from django.db import models


class Admin(models.Model):
    admin_id=models.AutoField(primary_key=True)
    username= models.CharField(null=False,max_length=10)
    password=models.CharField(null=False,max_length=10)
    is_active = models.IntegerField(null=False,default=0)



class Admin_Category(models.Model):
    adm_cat_id=models.ForeignKey(Admin,on_delete=models.CASCADE)
    dress_code=models.CharField(max_length=20,default='') #top,bottom, one-piece
    type_of_wear=models.CharField(max_length=40,default='') #ethnic,casual
    created_at = models.DateTimeField(auto_now_add=True)


class Admin_Design(models.Model):
    adm_des_id=models.ForeignKey(Admin,on_delete=models.CASCADE)
    design=models.ImageField(upload_to='images/')
    design_description=models.TextField()
    design_price=models.FloatField(default=0.0)
    design_code=models.ForeignKey(Admin_Category,on_delete=models.CASCADE,default=1)
    created_at=models.DateTimeField(auto_now_add=True)


class Admin_Fabric_Type(models.Model):
    fabric_id=models.AutoField(primary_key=True)
    fabric_name=models.CharField(max_length=50,null=False,default='')
    fabric_description=models.CharField(max_length=200)


class Admin_fabrics(models.Model):
    adm_fab_id=models.ForeignKey(Admin,on_delete=models.CASCADE)
    fabrics_type=models.ImageField(upload_to='images/')
    fabrics_description=models.CharField(max_length=100)
    fabrics_price=models.FloatField(null=False,default=0.0)
    fabrics_category=models.ForeignKey(Admin_Fabric_Type,on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)


class Vendor_Details(models.Model):
    vendor_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,default='')
    dob = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    post_office = models.CharField(max_length=30, null=True)
    boutique_address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=80, null=True)
    pincode = models.IntegerField()


class Vendor(models.Model):
    vendor_key = models.ForeignKey(Vendor_Details,on_delete=models.CASCADE,default='')
    username = models.CharField(null=False,max_length=10)
    password = models.CharField(null=False,max_length=10)
    is_active = models.IntegerField(null=False,default=0)
    edit_content=models.BooleanField(default=False)
    offer=models.IntegerField(default=1)
    registration_date = models.DateTimeField(auto_now_add=True)


class Vendor_Design(models.Model):
    ven_des_id=models.ForeignKey(Vendor_Details,on_delete=models.CASCADE)
    design=models.ImageField(upload_to='images/')
    design_description=models.TextField()
    design_price=models.FloatField(default=0.0)
    design_code=models.ForeignKey(Admin_Category,on_delete=models.CASCADE,default=1)
    created_at=models.DateTimeField(auto_now_add=True)


class Vendor_fabrics(models.Model):
    ven_fab_id = models.ForeignKey(Vendor_Details, on_delete=models.CASCADE)
    fabrics_type=models.ImageField(upload_to='images/')
    fabrics_description=models.CharField(max_length=100)
    fabrics_price=models.FloatField(null=False,default=0.0)
    fabrics_category=models.ForeignKey(Admin_Fabric_Type,on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)




