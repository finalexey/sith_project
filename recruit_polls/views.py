from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from recruit_polls.models import *
from recruit_app.models import *


def polls_list(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request, 'landing/polls/polls_list.html', context)


def poll(request, id=None):
    if request.method == 'GET':
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context = {}
        context['question'] = question
        return render(request, 'landing/polls/poll.html', context)
    if request.method == 'POST':

        # form = AnswerForm(request.POST or None)
        # print('_____', form.cleaned_data)
        #
        # rec_name = request.session['recruit_name']
        # recruit = Recruit.objects.filter(name=rec_name).first()
        # answer = Answer(question=form.cleaned_data['question'],
        #                 recruit=recruit,
        #                 answer=form.cleaned_data['answer'])
        # answer.save()

        recruit_id = 1
        data = request.POST
        ret = Answer.objects.create(recruit_id=recruit_id, choice_id=data['choice'])
        if ret:
            return HttpResponseRedirect(reverse('polls/polls_list'))
        else:
            return HttpResponse('Your vote is not done successful')
