# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from django.urls import reverse
from django.views import generic


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # return HttpResponse("You're looking at the results of question_id %s")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s", question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(slef):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def upload_file(request):
    print('hello')
    # 请求方法为POST时，进行处理
    if request.method == "POST":
        # 获取上传文件，如果没有文件，则默认为None
        file = request.FILES.get("file", None)
        if file is None:
            return HttpResponse("no files for upload!")
        else:
            # 打开特定的文件进行二进制的写操作
            with open("/tmp/%s" % file.name, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
                    print('hello')
            # return render(request, 'upload_file.html')
            return HttpResponse()
    else:
        # url = request.META['HTTP_HOST']+reverse('polls:upload_file')
        return render(request, 'upload_file.html')


def get_txt(request):
    with open('/tmp/data.txt', 'r') as f:
        lines = f.readlines()
        print lines
        return HttpResponse(lines)


def upload_page(request):
    return render(request,'upload_file_tmp.html')   #这里upload_page便是上面的前端html文件


def upload(request):
    file = request.FILES   #一定要调用上传的文件（不管你干嘛，保存也好，啥也不干也好，反正不调用就出错了，估计是默认不调用就不接收吧。。）才能用ajax上传成功，否则报错，原因不明
    return HttpResponse()
