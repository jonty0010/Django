from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path,include,re_path
from .import views

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('studata/',views.StudentList,name='Home'),
    path('stupost/',views.StudentPost,name='Home1'),
    path('studelete/<int:pk>/',views.StudentDelete,name='Home2'),
   #  path('stuupdate/<int:pk>/',views.StudentUpdate,name='Home3'),
   #  path('stuupdate1/<int:pk>/',views.my_model_update,name='Home4'),
   path('stuupdate/<int:pk>/',views.update_data,name='Home5'),

    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]