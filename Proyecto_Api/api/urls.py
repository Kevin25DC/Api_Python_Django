from django.urls import path
from .views import autorview,libroview,auto_librview

urlpatterns = [
    path('autor/', autorview.as_view(), name='autor_list'),
    path('libro/', libroview.as_view(), name='libro_list'),
    path('auto_libr/', auto_librview.as_view(), name='auto_libr_list'),
    path('autor/<int:id>', autorview.as_view(), name='autor_proceso')
]