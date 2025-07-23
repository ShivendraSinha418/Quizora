from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(quiz.urls)),
    path('quiz/' , include(quiz.urls)),
    path('quiz/play/' , include(quiz.urls)),
    path('quiz/play/showResult/' , include(quiz.urls))
]