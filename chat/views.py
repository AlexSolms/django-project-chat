from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        print("Received data " + request.POST['textMessage'])
    return render(request, 'chat/index.html', {'username': 'Alex'})
