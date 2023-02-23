from django.urls import path 
from .views import renderHtml, buscarCita
from .views import (
    CitasView, CategoriasView,
    ActualizarCategoriasView, OrdenesView
)
urlpatterns = [
    path('citas', renderHtml),
    path('citas/<int:cita_id>', buscarCita),
    path('citas/listar', CitasView.as_view()),
    path('categorias/listar/', CategoriasView.as_view()),
    path('categorias/actualizar/<int:categoria_id>', ActualizarCategoriasView.as_view()),
    path('ordenes/crear', OrdenesView.as_view())
]