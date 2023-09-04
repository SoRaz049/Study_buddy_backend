from django.shortcuts import render


rooms= [
    {'id':'1', 'name': "Hello this is me!"},
    {'id':'2', 'name': "Hello this is the development part"},
    {'id':'3', 'name': "Thanks for landing here!!!"}, 
]

def home(request):
    return render(request,'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')

def test():
    return 1
