from django.urls import path

from . import views

app_name = "paginas"

urlpatterns = [
    path("", views.pagina_inicial, name="inicio"),
]
