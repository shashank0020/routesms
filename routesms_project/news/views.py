from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

###############MY MODELS####################
from .models import Question,template_name,comment


############################################
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
############################### non GENERIC VIEWS################
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
# 
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
# 
# 
# 
# def vote(request):
#     
#     latest_question_list = Question.objects.values_list('question_text',flat=True)
#     context = RequestContext(request, {
#         'latest_question_list': latest_question_list,
#     })
#     return render(request, 'news/index.html', context)
#     return HttpResponse(template.render(context))
# 
# 
# 
# def details(request):
#     import ipdb;ipdb.set_trace()
#     #print quest
#     #latest_question_list = Question.objects.values_list('question_text',flat=True)
#     context = RequestContext(request,
#     )
#     return render(request, 'news/details.html', context)
#     return HttpResponse(template.render(context))
# 
# def index(request):
#     
#     return HttpResponse("Hello, world. You're at the polls index.")


##########################GERNERIC  VIEWS################################

#sign in page##
class SignIn(generic.ListView):
    
    '''RENDER SIGN IN PAGE '''
    template_name = 'news/sign_in_up.html'
    
    #context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return values from Models."""
        pass
        #return Question
 
#sigup in page##
class SignUp(generic.ListView):
    
    '''RENDER SIGN UP PAGE '''
    
    template_name = 'news/register.html'
    #context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return values from Models."""
        pass
        #return Question
 

class HomePageView(generic.ListView):
    
    '''RENDER HOME PAGE OF ROUTSMS NEWS '''
    
    template_name = 'news/posts.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return values from Models."""
        pass
        #return Question
        
        
class WebkitXlsView(generic.ListView):
    
    '''RENDER TO WEBKIT XLS REPORT POST '''
    
    #template_name = 'news/read_post_base.html'
    template_name = 'news/webkit_xls_report.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return values from Models."""
        pass
        #return Question        
        

class BankAccountView(generic.ListView):
    
    '''RENDER TO BANK ACCOUNT POST '''
    
    
    template_name = 'news/bank_account.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return values from Models."""
        pass
        #return Question        
        



    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'news/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request):

    return HttpResponse("Hello, world. You're at the polls index.")
    