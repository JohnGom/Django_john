from django.http import HttpResponse
from .models import Question


def index(request):
	lasted_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in lasted_question_list])
	return HttpResponse(output)


def detail(request, question_id):
	return HttpResponse("Usted se encuentra en la pregunta %s." % question_id)


def results(request, question_id):
	response = "Se encuentra en los resultados de la pregunta %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("Usted esta votando en la pregunta %s. % question_id")