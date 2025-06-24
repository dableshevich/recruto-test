from django.shortcuts import render


def hello(request):
    template = 'index.html'

    name = request.GET.get('name', 'Гость')
    message = request.GET.get('message', 'Привет!')

    context = {
        'name': name,
        'message': f'Hello, {name}! {message}!'
    }

    return render(request, template, context)
