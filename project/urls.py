
from django.contrib import admin
from django.urls import path,include
#from api.views import Product_crud, Blog_crud
#from rest_framework.routers import DefaultRouter


#router = DefaultRouter()
#router.register('product', views.Product_crud)
#router.register('blog', views.Blog_crud)

urlpatterns = [
    path('admin/', admin.site.urls),
   path('api/', include('api.urls')),
    
]
