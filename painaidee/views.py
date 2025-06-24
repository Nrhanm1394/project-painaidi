from django.shortcuts import render
# Create your views here.
def home (request):
    return render(request,'frontend/home.html')
def about (request):
    return render(request,'frontend/about.html')
def region (request):
    return render(request,'frontend/region.html')
def group (request):
    return render(request,'frontend/group.html')
def q (request):
    return render(request,'frontend/q.html')
def signin (request):
    return render(request,'frontend/signin.html')
def contact (request):
    return render(request,'frontend/contact.html')

def camping (request):
    return render(request,'frontend/camping.html')
def nature (request):
    return render(request,'frontend/nature.html')
def photograph (request):
    return render(request,'frontend/photograph.html')
def sea (request):
    return render(request,'frontend/sea.html')

def south (request):
    return render(request,'frontend/south/south.html')
def s1 (request):
    return render(request,'frontend/south/s1.html')
def s2 (request):
    return render(request,'frontend/south/s2.html')
def s3 (request):
    return render(request,'frontend/south/s3.html')
def s4 (request):
    return render(request,'frontend/south/s4.html')
def s5 (request):
    return render(request,'frontend/south/s5.html')
def s6 (request):
    return render(request,'frontend/south/s6.html')


def north (request):
    return render(request,'frontend/north/north.html')
def n3 (request):
    return render(request,'frontend/north/n3.html')
def n4 (request):
    return render(request,'frontend/north/n4.html')
def n5 (request):
    return render(request,'frontend/north/n5.html')
def n6 (request):
    return render(request,'frontend/north/n6.html')

def northeast (request):
    return render(request,'frontend/northeast/northeast.html')
def ne1 (request):
    return render(request,'frontend/northeast/ne1.html')
def ne2 (request):
    return render(request,'frontend/northeast/ne2.html')
def ne3 (request):
    return render(request,'frontend/northeast/ne3.html')

def central (request):
    return render(request,'frontend/central/central.html')
def c1 (request):
    return render(request,'frontend/central/c1.html')
def c2 (request):
    return render(request,'frontend/central/c2.html')
def c3 (request):
    return render(request,'frontend/central/c3.html')
def c4 (request):
    return render(request,'frontend/central/c4.html')
def c5 (request):
    return render(request,'frontend/central/c5.html')

def c7 (request):
    return render(request,'frontend/central/c7.html')
 

def c11 (request):
    return render(request,'frontend/central/c11.html')
def c12 (request):
    return render(request,'frontend/central/c12.html')