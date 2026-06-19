from django.shortcuts import render


def home(request):
    return render(request, "marksheet.html")
    
def msheet(request):
    a = request.POST.get("name")
    b = request.POST.get("id")
    c = request.POST.get("course")

    sub1 = int(request.POST["python"])
    sub2 = int(request.POST["c"])
    sub3 = int(request.POST["cl"])
    sub4 = int(request.POST["php"])
    sub5 = int(request.POST["laravel"])

    tm = sub1 + sub2 + sub3 + sub4 + sub5
    per = tm * 100 / 500

    if per >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    return render(request, "output.html", {
        'nm': a,
        'i': b,
        'cou': c,
        'py': sub1,
        'cc': sub2,
        'ccl': sub3,
        'ph': sub4,
        'la': sub5,
        'total': tm,
        'percen': per,
        'res': result
    })