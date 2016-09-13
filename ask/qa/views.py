from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from models import Question

def myviews(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit',10))
    except ValueError:
        limit = 5
    limit = limit if limit > 100 else 5

    try:
        page = int(request.GET.get('page',1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs,limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page

@require_GET
def new(request, *args, **kwargs):
    questions = Question.objects.new_question().all()
    page = paginate(request, questions)
    return render(request,'new.html',{'questions': page.object_list, 'page':page})

@require_GET
def popular(request, *args, **kwargs):
    questions = Question.objects.popular_question().all()
    page = paginate(request, questions)
    return render(request,'popular.html',{'questions': page.object_list, 'page':page})

@require_GET
def question(request, id):
    question = get_object_or_404(Question,pk=id)
    answer = question.answer_set.all()
    return render(request,'question.html',{'question': question, 'answer':answer})
