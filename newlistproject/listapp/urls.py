
from django.urls import path
from . import views
app_name='listapp'
urlpatterns = [


path('',views.index,name='index'),
path('carlist/<int:carlist_id>/',views.detail, name='detail'),
path('add/',views.add_car,name='add_car'),
path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]