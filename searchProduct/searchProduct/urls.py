from django.contrib import admin
from django.urls import path
from app.views import *
# allProduct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', allProduct, name='allProduct'),
    path('produto/', filteringProduct, name='filteringProduct'),

]
