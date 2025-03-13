from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.listar_alunos),
    path('alunos/criar/<int:pk>', views.criar_aluno),
    path('alunos/alterar/<int:pk>',views.alterar_aluno),
    path('alunos/deletar/<int:pk',views.deletar_informações),
    path('fazAlgo/<str:texto',views.macharete),
    

]