import datetime

from polls.models import QuestionTuple, Choice


def meal441():
    print("++++++++++++++++++++++++")
    question_tuple = QuestionTuple.objects.get(pk=441)
    questions = question_tuple.question_set.all()
    now = datetime.datetime.now()
    print("Time: " + str(now))
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    if 21 >= now.hour >= 20:
        for q in questions:
            choices = Choice.objects.filter(question_id=q.id).all()
            choices.update(votes=0)
        question_tuple.tuple_name = "Eat or not: " + str(tomorrow.day) + "th lunch"
        question_tuple.pub_date = datetime.datetime.now()
    elif 13 <= now.hour <= 14:
        for q in questions:
            choices = Choice.objects.filter(question_id=q.id).all()
            choices.update(votes=0)
        question_tuple.tuple_name = "Eat or not: " + str(today.day) + "th dinner"
        question_tuple.pub_date = datetime.datetime.now()
    question_tuple.save()
    print("Name: " + QuestionTuple.objects.get(pk=441).tuple_name)
