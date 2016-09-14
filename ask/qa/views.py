from django.core.paginator import Paginator, EmptyPage
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from qa.models import Question
from qa.forms import AskForm, AnswerForm
from django.views.decorators.csrf import csrf_exempt


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
    form = AnswerForm(initial={'question': question.pk})
    return render(request,'question.html',{'question': question, 'answer':answer, 'form':form})
@csrf_exempt
def ask(request, *args, **kwargs):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()
    return render(request, 'ask.html',{'form': form})

@require_POST
def answer(request, *args, **kwargs):
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save()
        return HttpResponseRedirect(answer.question.get_url())
    return render(request, 'ask.html',{'form': form})