from django.http import HttpResponse

def index(request):
    return HttpResponse("Heloo,world. You're at the polls index.")

 from django.http import HttpResponse

 def index(request):
    return HttpResponse("Hello,world.")
    
from django.http import Httpresponse
from django.http import Httpresponse

def index(request):
    return HttpsResponse("Halo world")

urlpatterns = [
    url(r'admin/',admib.site.urls)
    url(r'$',index),
]

urlpattern = [
    url(r'admin/', admin.site.urls),
    url(r'$,index'),

from django.http import Httpp404
from django.shortcuts import render

from.models import Question

def detail(request,question_id):
    try:
        question = ("Question does not exist")
        return render(request, "polls/detail.html"{"question":question})
def index(request):
    return HttpResponse("You looking at the results of question %s." % question_id)

def results(request,question_id):
    response = "You lookin are the results of question %5."
    return HttResponse(response % question_id)

def vote(request, questin_id):
    return HttpsRespone("You voting on question %s." % question_id)

from django.shortcuts import get_object_or_404, render

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question":question})

from django.http import HttpResponseRedirect
from django.shortcuts import get_onject_or_404, render
from django.urls import reverse 
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class indexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("_pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question 
    template_name = "polls/detail.html"

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request,question_id)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    [:5]
      output = ", ".join([q.question_text for q in latest_question_list])
      return HttpResponse(output)

from django,shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    [:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

from django.http import Httpp404
from django.shortcuts import render

from .models import Question 

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=quetion_id)
        except Quetion.DoesNoExist:
            raise Http404("Question does not exist")
        return render(request, "polls/detail.html" {"question:question"})

from django.shortcuts import get_object_or404, render
from .models import Question

def detail(request, question_id):
    quetion = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question:question"})

from django.http import HttpResponse
from .models import Quetion

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
[:5]
   output = ", ".join([q.question_text for q in latest_question_list])
      return HttpResponse(output)

from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    [:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "pools/index.html", context)

from django.shortcuts import get_object_or_404,rander
from .models import Quetion

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"polls/detail.html", {"question":question})

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from.models import Choice, Question

def vote(request, quetion_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice =
    question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoestNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message":"You didn't select a choice.",
                
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id)))

from django.shortcuts import get_object_or_404, render

def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question":question})

<h1>{{question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{choice.votes |pluralize }}</li>
  {% endfor %}
  </ul>
  
  <a href="{%  url 'polls:detail' question.id %}">Vote

from django.http import HttpResponse

from .models import Question

def index(rquest):
    latest_question_list = Question.objects.order_by("-pub_date")
    [:5]
       output = ",".join([q.question_text for q in latest_question_list])
       return HttpResponse(output)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html",) {"question":question}

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question":question})

def index(request):
    return HttpResponse("Heloo, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

from django.urls import path

from. import Views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id/vote/',views.vote, name = 'vote'),
]
]