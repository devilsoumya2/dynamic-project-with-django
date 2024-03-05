from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from.forms import usersform
from services.models import Service
from news.models import News
from contactenquiry.models import contactEnquiry
from django.core.paginator import Paginator
def homepage(request):
    newsdata=News.objects.all()
    Servicedata=Service.objects.all().order_by('service_head')
    data={
      'servicedata':Servicedata,
      'newsdata':newsdata
    }
    return render(request,"index.html",data)

def newsDeatatils(request,slug):
     newsdetails=News.objects.get(news_slug=slug)
     data={
          'newsdetails':newsdetails
     }
     return render(request,"newsdetails.html",data)

def submitform(request):
    try:
        if request.method == "POST":
                 n1 = int(request.POST.get('num1'))
                 n2 = int(request.POST.get('num2'))
                 n3 = int(request.POST.get('num3'))
                 finalans= n1 + n2 + n3
            
                 data={
                     'n1':n1,
                     'n2':n2,
                     'n3':n3,
                     'output':finalans
                 }
                
                 return HttpResponse(finalans)
    except:
        pass

def aboutUs(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"about.html",{'output':output})
def blog(request):
    return render(request,"blog.html")
def contact(request):
    return  render(request,"contact.html")

def saveEnquiry(request):
     n=''
     if request.method=="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          number=request.POST.get('number')
          data=contactEnquiry(name=name,email=email,phone=number)
          data.save()
          n='data inserted'
     return  render(request,"contact.html",{'n':n})

def menu(request):
    return render(request,"menu.html")
def products(request):
    return render(request,"products.html")
def review(request):
     Servicedata=Service.objects.all()
     paginator=Paginator(Servicedata,1)
     page_number=request.GET.get('page')
     Servicedatafinal=paginator.get_page(page_number)
     totalpage=Servicedatafinal.paginator.num_pages
     data={
      'servicedata': Servicedatafinal,
      'lastpage':totalpage,
      'totalpagelist':[n+1 for n in range(totalpage)]
    }
     return render(request,"review.html",data)
def courseDetails(request,courseid):
    return HttpResponse(courseid)
def userform(request):
    fn=usersform()
    data={'form':fn}
    finalans=0
    try:
        if request.method == "POST":
                 n1 = int(request.POST.get('num1'))
                 n2 = int(request.POST.get('num2'))
                 finalans= n1 + n2
            
                 data={
                    #  'n1':n1,
                    #  'n2':n2,
                    #  'output':finalans
                      'form':fn,
                      'output':finalans

                 }
                 url="/about/?output={}".format(finalans)
                 return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"userform.html",data)

def calculator(request):
    c=''
    try:
         if request.method=="POST":
              if request.POST.get('num1')=="":
                    return render(request,"calculator.html",{'error':True})
              elif request.POST.get('num2')=="": 
                   return render(request,"calculator.html",{'error':True})  
                   
              n1=eval(request.POST.get('num1'))
              n2=eval(request.POST.get('num2'))
              opr=request.POST.get('opr')
              if opr=="+":
                   c=n1+n2
              elif opr=="-":
                   c=n1-n2
              elif opr=="*":
                   c=n1*n2
              elif opr=="/":
                   c=n1/n2
    except:
         c="invalid opr..."
    print(c)
    return render(request,"calculator.html",{'c':c})


def evenodd(request):
    c=''
    if request.method=="POST":
         if request.POST.get('num1')=="":
              return render(request,"evenodd.html",{'error':True})
     
         n=eval(request.POST.get('num1'))
         if n%2==0:
              c="Even number"
         else:
              c="odd number"
    return render(request,"evenodd.html",{'c':c})

def marksheet(request):
    if request.method=="POST":
         if request.POST.get('Subject1')=="":
               return render(request,"marksheet.html",{'error':True})
         elif request.POST.get('Subject2')=="":
               return render(request,"marksheet.html",{'error':True})
         elif request.POST.get('Subject3')=="":
               return render(request,"marksheet.html",{'error':True})
         elif request.POST.get('Subject4')=="":
               return render(request,"marksheet.html",{'error':True})
         elif request.POST.get('Subject5')=="":
               return render(request,"marksheet.html",{'error':True})
              
         s1=eval(request.POST.get('Subject1'))
         s2=eval(request.POST.get('Subject2'))
         s3=eval(request.POST.get('Subject3'))
         s4=eval(request.POST.get('Subject4'))
         s5=eval(request.POST.get('Subject5'))
         t=s1+s2+s3+s4+s5
         p=t*100/500
         if p>=60:
              d="first division"
         elif p>=48:
              d="second division"
         elif p>=35:
              d="third division"
         else:
              d="fail"
         data={
              'total':t,
              'per':p,
              'div':d
         }
         return render(request,"marksheet.html",data)
    return render(request,"marksheet.html")