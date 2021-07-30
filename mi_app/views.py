from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime


def index(request):
    return HttpResponse("Hola querido curso :)")


def other_func(request):
    return HttpResponse("Esta es otra función diferente")


def saludar(request, nombre):
    return HttpResponse(f"Hola {nombre}. Como estas?")


def home(request, video):
    context = {
        'video': video,
        'mostrar': True,
        'banderas': [
            'https://www.banderas-mundo.es/data/flags/w580/cl.png',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Flag_of_Peru_%28state%29.svg/270px-Flag_of_Peru_%28state%29.svg.png',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Flag_of_Ecuador_%281900%E2%80%932009%29.svg/300px-Flag_of_Ecuador_%281900%E2%80%932009%29.svg.png',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Uruguay.svg/270px-Flag_of_Uruguay.svg.png'
        ]
    }
    return render(request, 'home.html', context)


def time(request):
    context = {
        'time': strftime('%Y-%m-%d %H:%M:%S', localtime())
    }

    return render(request, 'time.html', context)

def login(request):
    # si llega un GET, cargamos el formulario
    if request.method == 'GET':
        return render(request, 'login.html')

    # si llega un POST, logueamos al usuarios
    else:
        print('Nombre: ', request.POST['nombre'])
        print('Pass: ', request.POST['password'])

        # guardamos el nombre del usuario en Session
        request.session['nombre'] = request.POST['nombre']
        
        # redirigimos a una página interna
        return redirect('/time')
        # return HttpResponse('Logueando al usuario')
