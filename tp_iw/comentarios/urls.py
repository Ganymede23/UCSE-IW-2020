from django.urls import path

from .comentarios_views import delete_comment,denuncia_comment,mostrar_denuncias, delete_denuncias, delete_comment_denunciado

urlpatterns = [
    path('comment/<int:pk>/delete/', delete_comment, name='comment_delete'),
    path('comment/<int:pk>/denuncia/', denuncia_comment, name='comment_denuncia'),

    path('denuncias/', mostrar_denuncias, name='mostrar_denuncias'),
    path('denuncias/<int:pk>/delete/', delete_denuncias, name='denuncias_delete'),

    path('commentdenunciado/<int:pk>/delete/', delete_comment_denunciado, name='comment_denunciado_delete')
]
