from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from VendorPanel.views import VendorSew

app_name = 'VendorPanel'

urlpatterns = [
    path('', VendorSew.login, name="login"),
    path('home/',VendorSew.home , name="home"),
    path('ven_design/', VendorSew.vendor_design, name="vendor_design"),
    path('ven_design_upadte/<int:id>', VendorSew.vendor_update_design, name="ven_design_upadte"),
    path('register', VendorSew.register, name="register"),
    path('edit/<int:id>', VendorSew.edit, name="edit"),
    path('van_fabric', VendorSew.vendor_fabric, name="van_fabric"),
    path('van_fab_update/<int:id>', VendorSew.vendor_update_fabrics, name="van_fab_update"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
