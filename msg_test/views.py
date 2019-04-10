from django.shortcuts import render
from msg_test.models import msg_test

# Create your views here.


def msgbox(request):
    
    msgs=msg_test.objects.all()
    
  
    if request.method=="POST":
        unit=msg_test.objects.create(msg=request.POST['msg'])
        unit.save()
    return render(request,"msgbox_base.html",locals())

