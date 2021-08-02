from django.shortcuts import render,redirect,get_object_or_404
from store.models import ArtWorks
from store.form import ArtWorksForm
from bson.objectid import ObjectId
import base64

# Create your views here.
def home(request):
    context= {}
    return render(request,'home.html',context)

def store(request):
    context={}
    return render(request,'store.html',context)

def contact(request):
    context={}
    return render(request,'contact.html',context)

#def adminsm(request):
#    context={}
#    return render(request,'adminsm.html',context)

def artwork_list(request):
    artworks= ArtWorks.objects.all()
    return render(request,'adminsm.html',{'artworks':artworks})

def artwork_detail(request, id):
    print(ObjectId(id))
    art = ArtWorks.objects.get(id=id)
    print(art)
    print(art.painting_photo.read())
    print(type(art.painting_photo.read()))
    print(base64.b64encode(art.painting_photo.read()))
  
    #pic=art.painting_photo.read()
    print("This is nidhi")
    #for i in art:
    print(art.artname)
    print(art.description)
    print(art.available)
   # print(art.artname)
    return render(request, 'artwork_detail.html', {'art': art})

def artwork_new(request):
    if request.method == "POST":
        tag=request.POST.get('tags')
        form = ArtWorksForm(request.POST,request.FILES)
        if form.is_valid():
            newart = form.save(commit=False)
            newart.tags=tag.split(',')
            newart.artsizeInch={"height":request.POST.get('height'), "width":request.POST.get('width')}
            #newart.published_date = timezone.now()
            newart.painting_photo=request.FILES.get('painting_photo')
            newart.save()
            return redirect('artwork_detail', id=newart.id)
    else:
        form = ArtWorksForm()
    return render(request, 'artwork_edit.html', {'form': form})

def artwork_edit(request, id):
    art = get_object_or_404(ArtWorks, id=id)
    if request.method == "POST":
        tag=request.POST.get('tags')
        print(tag)
        form = ArtWorksForm(request.POST, request.FILES, instance=art)
        #print(form.artname)
        if form.is_valid():
            art = form.save(commit=False)
            art.tags=tag.split(',')
            art.artsizeInch={"height":request.POST.get('height'), "width":request.POST.get('width')}
            #art.painting_photo.put(open(""))
            #post.author = request.user
            #post.published_date = timezone.now()
            art.save()
            return redirect('artwork_detail', id=art.id)
    else:
        form = ArtWorksForm(instance=art)
    return render(request, 'artwork_edit.html', {'form': form})