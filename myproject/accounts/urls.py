from django.contrib import admin
from django.urls import path
from . import views
  
urlpatterns = [
    path('', veiws.home), 
    path('product/',veiws.product),
    path('coustomer/',veiws.coustomer)
    path()
] 
#we need to talk about this path and urls later on tgis 
