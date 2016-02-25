from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^$', views.index, name="Index"),
	# ejemplo localhost:8000/polls/5/
	#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# ejemplo localhost:8000/polls/5/results
	#url(r'^p<question_id>[0-9]+)/results/$', views.results, name='results'),
	# ejemplo localhost:8000/polls/5/vote
	#url(r'^p<question_id>[0-9]+)/vote/$', views.vote, name='results'),
]