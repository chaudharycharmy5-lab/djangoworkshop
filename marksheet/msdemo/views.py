from django.shortcuts import render

def msheet(request):

    if request.method == "POST":

        a = request.POST["name"]
        b = request.POST["id"]
        c = request.POST["course"]

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

    return render(request, "marksheet.html")