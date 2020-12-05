from django.shortcuts import render,redirect
from maker.models import Menu

# Create your views here.
def makerDash(request):
    # return render(request, 'maker/makerDashboard.html')
    menuData = Menu.objects.all()
    for student in menuData:
        print(student.quantity)
    tableData = {'data':menuData}    
    return render(request, 'maker/makerDashboard.html', tableData)
def addMaker(request):
    if request.method == "POST":
        name = request.POST.get("menuInputName")
        quantity = request.POST.get("menuQuantity")
        price = request.POST.get("menuPrice")
        tmp = Menu(name = name, quantity = quantity, price = price)
        tmp.save()
    return render(request, 'maker/addMenu.html')

def editMenuData(request, menuId):
    data = Menu.objects.get(menuId = menuId)
    tableData = {'data' : data}
    if(request.method == "POST"):
        name = request.POST.get("menuInputName")
        quantity = request.POST.get("menuQuantity")
        price = request.POST.get("menuPrice")
        # tmp = Menu(name = name, quantity = quantity, price = price)
        data.name = name
        data.quantity = quantity
        data.price = price
        data.save()
        return redirect('makerDash')
    return render(request, 'maker/editMenu.html', tableData)

def deleteMenuData(request, menuId):
    data = Menu.objects.get(menuId = menuId)
    data.delete()
    return redirect('makerDash')