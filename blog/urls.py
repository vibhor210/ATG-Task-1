from django.urls import path
from . import views
urlpatterns = [
    path('add-blog',views.create,name="CreateBlog" ),
    path('blogs',views.blogs,name="Blogs" ),
    path('disaply-blog/<str:pk>/',views.displayBlog,name="DisplayBlog" ),
]