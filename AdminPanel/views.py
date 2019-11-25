from django.shortcuts import render
from django.shortcuts import render, redirect
from AdminPanel.models import *
from django.core.files.storage import FileSystemStorage
# Create your views here.


class ViewSew:

    def login(self):
        if self.method == "POST":
            try:


                username=self.POST.get('username')
                password=self.POST.get('pass')

                result=Admin.objects.get(username=username,password=password,is_active=1)

                if result:

                    self.session['user_name'] = result.username
                    self.session['user_id'] =result.admin_id


                    try:

                        design = Admin_Design.objects.all()
                        fabrics = Admin_fabrics.objects.all()

                    except:

                        design, fabrics = [], []

                    return render(self, 'admin/home.html', {'design': design,'fabrics': fabrics})

            except:

                 return (self,'admin/login.html',{'message':'Invalid credentials'})

        else:
           return render(self,'admin/login.html')


    def home(self):
        design = Admin_Design.objects.all()
        fabrics = Admin_fabrics.objects.all()
        return render(self,'admin/home.html',{'design':design,'fabrics':fabrics})

    def design(self):
         if self.method == "POST":
             try:
                 if self.session['user_id']:

                    try:

                         des_object = { 'description': self.POST.get("description"), 'price': self.POST.get("price"),'code':self.POST.get("code")}
                         type=self.POST.get('category_type')

                         d=type.split('-')[0]

                         image=self.FILES['design']
                         fs = FileSystemStorage()
                         filename = fs.save(image.name, image)

                         adm_id=Admin.objects.get(admin_id=int(self.session['user_id']))
                         cat_id=Admin_Category.objects.get(id=d)



                         Admin_Design.objects.create(design=filename,design_description=des_object['description'],
                                       design_price=des_object['price'],design_code=cat_id,adm_des_id=adm_id,
                                       created_at=models.DateTimeField(auto_now_add=True))

                         message ="Created successfully"

                    except:

                         message="Error ocurred"
                    result = Admin_Design.objects.all()
                    return render(self, 'admin/Design.html', {'message': message, 'result': result})

             except:

                 return render(self, 'admin/login.html', {'message': 'session expire'})
         else:

             try:
                 result=Admin_Design.objects.all()
                 category=Admin_Category.objects.all()
             except:

                  result,category ={},{}

             return render(self, 'admin/Design.html',{'result':result,'category':category})


    def edit_design(self,id):
        result=Admin_Design.objects.get(id=id)
        category=Admin_Category.objects.all()
        return render(self,'admin/edit_design.html',{'result':result,'category':category})

    def update_design(self):
        if self.session['user_id']:
             try:
                des_object = { 'description': self.POST.get("description"), 'price': self.POST.get("price")}

                type = self.POST.get('category_type')
                id=self.POST.get('id')
                d = type.split('-')[0]

                cat_id = Admin_Category.objects.get(id=d)

                if self.FILES.get('design', False):
                    image = self.FILES['design']
                    fs = FileSystemStorage()
                    filename = fs.save(image.name, image)

                    Admin_Design.objects.filter(id=id).update(design=filename,design_description=des_object['description'],
                                       design_price=des_object['price'],design_code=cat_id)
                else:

                    Admin_Design.objects.filter(id=id).update(design_description=des_object['description'],
                                       design_price=des_object['price'],design_code=cat_id)


                message="Update Successfull"

             except:

                 message ="Some errror occured"

             result = Admin_Design.objects.all()
             category = Admin_Category.objects.all()
             return render(self, 'admin/Design.html', {'message': message,'result':result,'category':category})
        else:
            return render(self, 'admin/login.html', {'message': 'session expire'})

    def Category(self):
        if self.method == "POST":
            try:
                if self.session['user_id']:

                    try:

                        des_object = {'dress_code': self.POST.get("code"), 'wear_type': self.POST.get("type")}

                        adm_id = Admin.objects.get(admin_id=self.session['user_id'])

                        Admin_Category.objects.create(adm_cat_id=adm_id,dress_code=des_object['dress_code'],
                                                      type_of_wear=des_object['wear_type'],created_at=models.DateTimeField(auto_now_add=True))

                        message = "Created successfully"

                    except:
                        message = "error occured "

                    result=Admin_Category.objects.all()
                    return render(self, 'admin/category.html', {'message': message,'result':result})
            except:
                return render(self, 'admin/login.html', {'message': 'session expire'})

        else:
            result=Admin_Category.objects.all()
            return render(self, 'admin/category.html',{'result':result})


    def edit_category(self,id):
        result=Admin_Category.objects.get(id=id)
        return render(self,'admin/edit_category.html',{'result':result})

    def update_category(self):
        if self.session['user_id']:

                des_object = {'dress_code': self.POST.get("code"), 'wear_type': self.POST.get("type"),
                              'id':self.POST.get("id")}

                Admin_Category.objects.filter(id=des_object['id']).update(dress_code=des_object['dress_code'],
                                              type_of_wear=des_object['wear_type'])

                message = "Update successfull"



                result=Admin_Category.objects.all()
                return render(self, 'admin/category.html', {'message': message,'result':result})
        else:
            return render(self, 'admin/login.html', {'message': 'session expire'})


    def fabric_type(self):
        if self.method == "POST":
            try:
                if self.session['user_id']:

                    try:

                        feb_object = {'fabric_name': self.POST.get("name"), 'fabric_description': self.POST.get("description")}


                        Admin_Fabric_Type.objects.create(fabric_name=feb_object['fabric_name'],fabric_description=feb_object['fabric_description'])

                        message = "Created successfully"

                    except:
                        message = "error occured "

                    result=Admin_Fabric_Type.objects.all()
                    return render(self, 'admin/fabric_type.html', {'message': message,'result':result})
            except:
                return render(self, 'admin/login.html', {'message': 'session expire'})

        else:
            result = Admin_Fabric_Type.objects.all()
            return render(self, 'admin/fabric_type.html',{'result':result})




    def edit_fabric_type(self,id):
        result=Admin_Fabric_Type.objects.get(fabric_id=id)
        return render(self,'admin/edit_fabric.html',{'result':result})


    def update_fabric_type(self):
        if self.session['user_id']:
            try:

                feb_object = {'fabric_name': self.POST.get("name"), 'fabric_description': self.POST.get("description"),
                              'id':self.POST.get("id")}

                Admin_Fabric_Type.objects.filter(fabric_id=feb_object['id']).update(fabric_name=feb_object['fabric_name'],
                                                 fabric_description=feb_object['fabric_description'])

                message = "Update successfull"

            except:
                message = "some error occured"

            result = Admin_Fabric_Type.objects.all()
            return render(self, 'admin/fabric_type.html', {'message': message,'result':result})
        else:
            return render(self, 'admin/login.html', {'message': 'session expire'})


    def fabric(self):
        if self.method == "POST":
            try:
                if self.session['user_id']:

                    try:

                        feb_object = {'fabric_description': self.POST.get("description"),'fabric_price': self.POST.get("price"),
                                      'fabric_category': self.POST.get("category")}

                        val = self.POST.get('category_type')
                        d = val.split('-')[0]

                        image = self.FILES['design']
                        fs = FileSystemStorage()
                        filename = fs.save(image.name, image)

                        adm_id = Admin.objects.get(admin_id=self.session['user_id'])
                        fab_id = Admin_Fabric_Type.objects.get(fabric_id=d)

                        Admin_fabrics.objects.create(adm_fab_id=adm_id,fabrics_type=filename,
                                                     fabrics_description=feb_object['fabric_description'],
                                                     fabrics_price=feb_object['fabric_price'],
                                                     fabrics_category=fab_id,
                                                     created_at=models.DateTimeField(auto_now_add=True))

                        message = "Created successfully"

                    except:
                        message = "error occured "

                    result=Admin_fabrics.objects.all()
                    type=Admin_Fabric_Type.objects.all()
                    return render(self, 'admin/fabrics.html', {'message': message,'result':result,'type':type})
            except:
                return render(self, 'admin/login.html', {'message': 'session expire'})

        else:
            result = Admin_fabrics.objects.all()
            type = Admin_Fabric_Type.objects.all()
            return render(self, 'admin/fabrics.html', {'result': result, 'type': type})



    def edit_fab(self,id):
        result = Admin_fabrics.objects.get(id=id)
        type = Admin_Fabric_Type.objects.all()
        return render(self, 'admin/Edit_fab.html', {'result': result, 'type': type})

    def update_fabrics(self):
        if self.method == "POST":
            try:
                if self.session['user_id']:

                    try:

                        feb_object = { 'fabric_description': self.POST.get("description"),'fabric_price': self.POST.get("price")}

                        type = self.POST.get('category_type')
                        id = self.POST.get('id')
                        d = type.split('-')[0]
                        fab_id = Admin_Fabric_Type.objects.get(fabric_id=d)

                        if self.FILES.get('design', False):
                            image = self.FILES['design']
                            fs = FileSystemStorage()
                            filename = fs.save(image.name, image)



                            Admin_fabrics.objects.filter(id=id).update(fabrics_type=filename,
                                                         fabrics_description=feb_object['fabric_description'],
                                                         fabrics_price=feb_object['fabric_price'],
                                                         fabrics_category=fab_id)

                        else:
                            Admin_fabrics.objects.filter(id=id).update( fabrics_description=feb_object['fabric_description'],
                                                         fabrics_price=feb_object['fabric_price'],
                                                         fabrics_category=fab_id)

                        message = "update successfully"

                    except:
                        message = "error occured "

                    result = Admin_fabrics.objects.all()
                    type = Admin_Fabric_Type.objects.all()
                    return render(self, 'admin/fabrics.html', {'message': message,'result':result,'type':type})
            except:
                return render(self, 'admin/login.html', {'message': 'session expire'})


