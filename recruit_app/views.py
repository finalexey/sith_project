from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import RecruitForm, SithForm


def landing(request):
    return render(request, 'landing/landing.html', locals())


def forsith(request):
    name = 'ForSiths'
    form = SithForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        print(form.cleaned_data)
        added_sithname = (form.cleaned_data['name'])[0]
        print(added_sithname)
        return HttpResponseRedirect(reverse('testedrecr'))

    return render(request, 'landing/forsith.html', locals())


def forrecr(request):
    name = 'ForRecruits'
    form = RecruitForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        print(form.cleaned_data)
        new_form = form.save()
        request.session['recruit_email'] = form.cleaned_data['email']
        return HttpResponseRedirect(reverse('polls_list'))

    return render(request, 'landing/forrecr.html', locals())
