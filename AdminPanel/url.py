from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from AdminPanel.views import ViewSew

app_name = 'AdminPanel'

urlpatterns = [
    path('',ViewSew.login ,name="login"),
    path('home/',ViewSew.home , name="home"),
    path('design/',ViewSew.design , name="design"),
    path('design_update',ViewSew.update_design ,name="design_update"),
    path('edit_design/<int:id>',ViewSew.edit_design , name="edit_design"),
    path('category',ViewSew.Category,name="category"),
    path('category_upadte',ViewSew.update_category ,name="category_update"),
    path('edit_category/<int:id>',ViewSew.edit_category ,name="edit_category"),
    path('fabric_type',ViewSew.fabric_type,name="fabric_type"),
    path('fabric_update', ViewSew.update_fabric_type, name="fabric_update"),
    path('edit_fabric/<int:id>', ViewSew.edit_fabric_type, name="edit_fabric"),
    path('fabric', ViewSew.fabric, name="fabric"),
    path('fab_update', ViewSew.update_fabrics, name="fab_update"),
    path('edit_fab/<int:id>',ViewSew.edit_fab ,name="edit_fab"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
