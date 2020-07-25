from django.urls import path
from . import views
urlpatterns=[
				path("",views.home,name="home"),
				path("about",views.about,name="about"),
				path("packages",views.packages,name="packages"),
				path("services",views.services,name="services"),
				path("center",views.center,name="center"),
				path("review",views.review,name="review"),
				path("gallary",views.gallary,name="gallary"),
				path("book",views.book,name="book"),
				path("bookDetail",views.bookDetail,name="bookDetail"),
				path("superuser",views.superuser,name="superuser"),
				path("login",views.login,name="login"),
				path("register",views.register,name="register"),
]