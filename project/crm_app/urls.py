from django.urls import path
from crm_app.views import *

urlpatterns = [
    path('', index),
    path('contragents/', contragents),
    path('cats/', cats),
]
