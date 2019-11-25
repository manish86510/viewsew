from django.shortcuts import render
from AdminPanel.models import *

# Create your views here.

class VendorSew:
    def login(self):
        if self.method == "POST":

          try:
                username=self.POST.get('username')
                password=self.POST.get('pass')

                result=Vendor.objects.get(username=username,password=password)

                if result.is_active == 1:

                    self.session['vendor_id'] = result.id
                    self.session['edit_code'] = result.edit_content

                    try:

                        design = Admin_Design.objects.all()
                        fabrics = Admin_fabrics.objects.all()

                    except:

                        design ,fabrics = [] ,[]

                    return render(self,'vendor/home.html', {'design':design,'fabrics':fabrics})

                else:

                    return render(self,'vendor/login.html',{'message':'Inactive'})
          except:

            return render(self, 'vendor/login.html', {'message': 'Invalid credential'})

        else:
           return render(self,'vendor/login.html')


    def home(self):
        design = Admin_Design.objects.all()
        fabrics = Admin_fabrics.objects.all()
        return render(self,'vendor/home.html',{'design':design,'fabrics':fabrics})

    def register(self):
        if self.method == "POST":

                vendor_object = {'dob': self.POST.get['dob'], 'mobile': self.POST.get("mobile"),
                                'city': self.POST.get("city"), 'state': self.POST.get("state"),
                                'post_office': self.POST.get("post_office"), 'boutique_address': self.POST.get("address"),
                                'landmark': self.POST.get("landmark"), 'pincode': self.POST.get("pincode"),
                                'name':self.POST.get("name")}

                try:
                       Vendor_Details.objects.create(
                           dob=vendor_object['dob'],
                           mobile = vendor_object['mobile'],
                           city = vendor_object['city'],
                           state = vendor_object['state'],
                           post_office = vendor_object['post_office'],
                           boutique_address = vendor_object['boutique_address'],
                           landmark = vendor_object['landmark'],
                           pincode = vendor_object['pincode'],
                           name=vendor_object['name']
                       )

                       message="Created Successfully"
                except:

                     message="Error occured"

                return render(self,'vendor/register.html',{'message':message})

        else:
            return render(self,'vendor/register.html')



    def edit(self):
        if self.method == "POST":

            if self.session['vendor_id'] is not None:

                vendor_object = {'dob': self.POST.get['dob'], 'mobile': self.POST.get("mobile"),
                                 'city': self.POST.get("city"), 'state': self.POST.get("state"),
                                 'post_office': self.POST.get("post_office"), 'boutique_address': self.POST.get("address"),
                                 'locality': self.POST.get("locality"), 'landmark': self.POST.get("landmark"),
                                 'pincode': self.POST.get("pincode"), }


                try:
                    Vendor_Details.objects.filter(vendor_id=int(self.session['vendor_id'])).update(
                        dob=vendor_object['dob'],
                        mobile=vendor_object['mobile'],
                        city=vendor_object['city'],
                        state=vendor_object['state'],
                        post_office=vendor_object['post_office'],
                        boutique_address=vendor_object['boutique_address'],
                        locality=vendor_object['locality'],
                        landmark=vendor_object['landmark'],
                        pincode=vendor_object['pincode']
                    )

                    message = "Updated Successfully"
                except:

                    message = "Error occured"

                return render(self, 'vendor/register.html', {'message': message})

            else:
                return render(self,'vendor/login.html',{'message':'Session Expire'})

    def vendor_design(self):
         if self.method == "POST":

                 if self.session['vendor_id'] is not None and self.session['edit_code'] != False:

                     try:

                         des_object = {'design': self.FILES['design'], 'description': self.POST.get("description"),
                                       'price': self.POST.get("price"),'code':self.POST.get("code")}

                         adm_id=Admin.objects.get(admin_id=self.session['user_id'])
                         cat_id=Admin_Category.objects.get(adm_cat_id=int(des_object['code']))

                         Vendor_Design.objects.create(design=des_object['design'],design_description=des_object['description'],
                                       design_price=des_object['price'],design_code=cat_id.adm_cat_id,ven_des_id=adm_id.admin_id,
                                       created_date=models.DateTimeField(auto_now_add=True))

                         message ="Created successfully"

                     except:
                         message = "error occured "

                     return render(self,'vendor/design.html',{'message':message})

                 else:

                     return render(self,'vendor/login.html',{'message':'Inactive'})


    def vendor_update_design(self,id):
        if self.session['vendor_id'] is not None and self.session['edit_code'] != False:
            try:
                des_object = {'design': self.FILES['design'], 'description': self.POST.get("description"),
                              'price': self.POST.get("price"), 'code': self.POST.get("code")}

                cat_id = Admin_Category.objects.get(adm_cat_id=int(des_object['code']))

                Vendor_Design.objects.filter(ven_des_id=id).update(design=des_object['design'],design_description=des_object['description'],
                                       design_price=des_object['price'],design_code=cat_id.adm_cat_id,
                                       created_date=models.DateTimeField(auto_now_add=True))

                message="Update Successfull"

            except :
                 message="some error occured"

            return render(self, 'vendor/design.html', {'message': message})
        else:
            return render(self, 'vendor/login.html', {'message': 'session expire'})


    def vendor_fabric(self):
        if self.method == "POST":

                if self.session['user_id'] is not None and self.session['edit_code'] != False:

                    try:

                        feb_object = {'fabric_image': self.FILES('image'), 'fabric_description': self.POST.get("description"),
                                      'fabric_price': self.POST.get("price"),'fabric_category': self.POST.get("category")}

                        adm_id = Admin.objects.get(admin_id=self.session['user_id'])
                        fab_id = Admin_Fabric_Type.objects.get(fabric_id=int(feb_object['fabric_category']))

                        Vendor_fabrics.objects.create(ven_fab_id=adm_id.admin_id,fabrics_type=feb_object['fabric_image'],
                                                     fabrics_description=feb_object['fabric_description'],
                                                     fabrics_price=feb_object['fabric_price'],
                                                     fabrics_category=fab_id.fabric_id)

                        message = "Created successfully"

                    except:
                        message = "error occured "

                    return render(self, 'vendor/fabrics.html', {'message': message})

                else:

                    return render(self, 'vendor/login.html', {'message': 'session expire'})


    def vendor_update_fabrics(self,id):
        if self.method == "POST":

                if self.session['user_id'] is not None and self.session['edit_code'] != False:

                    try:

                        feb_object = {'fabric_image': self.FILES('image'), 'fabric_description': self.POST.get("description"),
                                      'fabric_price': self.POST.get("price"),'fabric_category': self.POST.get("category")}

                        fab_id = Admin_Fabric_Type.objects.get(fabric_id=int(feb_object['fabric_category']))

                        Vendor_fabrics.objects.filter(ven_fab_id=id).update(fabrics_type=feb_object['fabric_image'],
                                                     fabrics_description=feb_object['fabric_description'],
                                                     fabrics_price=feb_object['fabric_price'],
                                                     fabrics_category=fab_id.fabric_id)

                        message = "update successfully"

                    except:
                        message = "error occured "

                    return render(self, 'vendor/fabrics.html', {'message': message})

                else:

                    return render(self, 'vendor/login.html', {'message': 'session expire'})