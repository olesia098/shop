from django.urls import path

from applications.product.views import ListCreateView

urlpatterns = [
    path('', ListCreateView()),
    path('<int:pk>/',DeleteUpdateRetriveVier)
]