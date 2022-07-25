from django.conf.urls import url 
from bitcoinrate import views 
 
urlpatterns = [ 
    url(r'^api/v1/quotes$', views.rateandprice),
]