from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    if request.method =="POST":
        num1 = request.POST['number1']
        num2 = request.POST['number2']
        print(num1)
        add = int(num1) + int(num2)
        data={
            "num1":num1,
            "num2":num2,
            "result": add,

        }
        return render(request,'index.html',{"fromdata":data})
    return_data = "<h1>First Django project</h1>"
    return HttpResponse(return_data)

todos = [
        {"todo": "Test Todo 1"},
        {"todo": "Test Todo 2"},
        {"todo": "Test Todo 3"},
        {"todo": "Test Todo 4"},
        {"todo": "Test Todo 5"}


    ]

def FirstPage(request):
    user = "Ishtiaq Ahmad Shohan"
    return render(request,'index.html',{"data":todos})