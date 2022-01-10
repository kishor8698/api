from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("stuinfo/<int:pk>",views.student_detail),
    path("stuinfo/",views.student_list),
    path("stucreate/",views.student_create),
    #path("studentapi/",views.ListCreateStudent.as_view()),
    #path("studentapi/<int:pk>",views.RetrieveUPdateDestroyStudent.as_view()),
]
