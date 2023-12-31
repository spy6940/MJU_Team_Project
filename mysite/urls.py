"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),       #url을 parsing 해서 polls/ 에서 polls.url 파일로 감
    path('gpt/', include('GPT.urls')),          # 개발서버/GPT를 입력받으면 GPT/urls.py로 넘어감
    path('food/', include('q_food.urls')),      # 개발서버/food를 입력받으면 q_food/urls.py로 넘어감
    path('question/', include('Question.urls')),
    path('admin/', admin.site.urls),
]
