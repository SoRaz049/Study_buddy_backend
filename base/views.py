from django.shortcuts import render


rooms= [
    {'id':1, 'name': "Hello this is me!"},
    {'id':2, 'name': "Hello this is the development part"},
    {'id':3, 'name': "Thanks for landing here!!!"}, 
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room' : room}
    return render(request, 'room.html', context)


