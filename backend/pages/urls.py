from django.urls import path
from .views import (
	HomePageView, 
# 	# DashboardPageView,
# 	# LoginPageView,
# 	# RegCustomerPageView,
# 	# RegProductPageView,
# 	# TableCustomerPageView,
# 	# TableProductPageView,
# 	# TableOrderPageView,
# 	# ErrorPageView
	MainView,
	RequestSchedView,
	)

from pages.views import (
	HomePageView,
	NotesPageView, 
	MainView,
	SearchView,
	GeolocationView,
	ProfileView,
	SettingsView,
	PaymentView,
	MessagingView,
	CreateSubjectView,
	ScheduleSubjectView,
	MentorProfileView,
	RequestSchedView,
	ChatBotView,
)

app_name = 'pages'
urlpatterns = [
	path('',HomePageView.as_view(),name='login'),
	path('index/',HomePageView.as_view(),name='index'),
	path('main/',MainView.as_view(),name='main'),
	path('RequestSched/',RequestSchedView.as_view(), name = 'RequestSched'),
	path('notes/',NotesPageView.as_view(),name='notes'),
	path('main/',SearchView.as_view(),name='main'),
	path('search/',SearchView.as_view(),name='search'),
	path('geolocation/',GeolocationView.as_view(),name='geo'),
	path('profile/',ProfileView.as_view(),name='profile'),
	path('settings/',SettingsView.as_view(),name='settings'),
	path('payment/',PaymentView.as_view(),name='payment'),
	path('messaging/',MessagingView.as_view(),name='message'),
	path('create-subject/',CreateSubjectView.as_view(),name='create-sub'),
	path('schedule/',ScheduleSubjectView.as_view(),name='subject-view'),
	path('mentor-profile/',MentorProfileView.as_view(),name='mentor-profile'),
	path('ChatBot/',ChatBotView.as_view(),name='chatbot'),

]