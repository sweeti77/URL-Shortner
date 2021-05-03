from django.shortcuts import redirect, render
from .models import Url
import uuid

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method=='POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:7]
        new_url = Url(title=url,uuid=uid)
        new_url.save()
        return render(request, 'index.html',
                        context = {'getLink':url, 'shortenLink' : "localhost:8000/"+uid})

def go(request, pk):
    url_detail = Url.objects.get(uuid=pk)
    link = url_detail.title
    return redirect(link)
