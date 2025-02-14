from django.shortcuts import render

def lista_tarefas(request):
    tarefas = [
        {'descricao': 'Comprar Sal picão', 'concluida': False},
        {'descricao': 'Ver anime Demon Slayer', 'concluida': True},
        {'descricao': 'Comprar suco natural de fruta', 'concluida': False},
    ]
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})
