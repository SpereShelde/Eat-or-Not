from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.db.models import F
from django.urls import reverse

from polls.models import Choice, QuestionTuple


def index(request):
    return render(request, 'polls/index.html')

def detail(request):
    pin_id = request.POST['PINId']
    try:
        selected_question_tuple = QuestionTuple.objects.get(pk=pin_id)
    except (KeyError, QuestionTuple.DoesNotExist):
        return render(request, 'polls/index.html', {
            'error_message': "Poll doest not exist. Try another.",
        })
    else:
        return render(request, 'polls/detail.html', {'question_tuple': selected_question_tuple})

def shortcut(request, question_tuple_id):
    try:
        selected_question_tuple = QuestionTuple.objects.get(pk=question_tuple_id)
    except (KeyError, QuestionTuple.DoesNotExist):
        return render(request, 'polls/index.html', {
            'error_message': "Poll doest not exist. Try another.",
        })
    else:
        return render(request, 'polls/detail.html', {'question_tuple': selected_question_tuple})

def results(request):
    global question_tuple
    try:
        question_tuple = QuestionTuple.objects.get(pk=request.POST['question_tuple_id'])
        if request.POST['skip'] == "skip":
            return render(request, 'polls/results.html', {
                'question_tuple': question_tuple
            })
        radios = question_tuple.question_set.filter(type=1).all()
        for radio in radios:
            choice = Choice.objects.get(pk=request.POST['ration_group' + str(radio.id)])
            choice.votes = F('votes') + 1
            choice.save()
        check_box_list = request.POST.getlist('checkbox_group')
        for check_box in check_box_list:
            choice = Choice.objects.get(pk=check_box)
            choice.votes = F('votes') + 1
            choice.save()


    except (KeyError, Choice.DoesNotExist, QuestionTuple.DoesNotExist):
        return render(request, 'polls/index.html', {
            'error_message': "Hey, what are you doing?",
        })
    else:
        return render(request, 'polls/results.html', {
            'question_tuple': question_tuple
        })
