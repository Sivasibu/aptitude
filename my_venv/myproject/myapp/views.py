from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator
# Create your views here.
from myapp.models import Exam
            
def exam(request):
    # queryset = Exam.objects.all()
          
    # # Filter by department
    # department = request.GET.get('department')
    # if department:
    #     queryset = queryset.filter(department__icontains=department)

    # # Filter by role
    # role = request.GET.get('role')
    # if role:
    #     queryset = queryset.filter(role_icontains = role)

    # # Filter by topic
    # topic = request.GET.get('topic')
    # if topic:
    #     queryset = queryset.filter(topic__icontains=topic)

    # Add other filters here as needed

    return render(request,'exam.html')

# def question(request):
#     return render(request,"question.html")

def index(request):
    return render(request,"index.html")

#Login,Reigster,Logout Forms

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
          
            user = form.save()
            user.is_staff= True
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'registration.html',{'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('start')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def result(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Exam.objects.all()
        score=0
        wrong=0
        correct=0
        total=questions.count()
        for q in questions:
            if q.answeroption ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = (score/(total*10)) *100
        context = {
            'score':score,
            'time_taken': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        return redirect('question')
    
def question(request):
  
    questions = Exam.objects.all()
    paginator = Paginator(questions, 10)  # Show 10 questions per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'question.html', context)

      
def start(request):
     return render(request,'start.html')
         
