from django.shortcuts import render
from msg_test.models import msg_test
from django.http import HttpResponseRedirect
# Create your views here.


def msgbox(request):
    
    msgs=msg_test.objects.all()
    
  
    if request.method=="POST":
        post_msg=request.POST['msg']
        if(post_msg!=""):
            unit=msg_test.objects.create(msg=post_msg)
            unit.save()
            return HttpResponseRedirect(".")
            
            
        
        
        
    return render(request,"msgbox_base.html",locals())

