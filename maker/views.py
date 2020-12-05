from django.shortcuts import render
from maker.models import Menu

# Create your views here.
def makerDash(request):
    return render(request, 'maker/makerDashboard.html')
def addMaker(request):
    if request.method == "POST":
        name = request.POST.get("menuInputName")
        quantity = request.POST.get("menuQuantity")
        price = request.POST.get("menuPrice")
        tmp = Menu(name = name, quantity = quantity, price = price)
        tmp.save()
    return render(request, 'maker/addMenu.html')

