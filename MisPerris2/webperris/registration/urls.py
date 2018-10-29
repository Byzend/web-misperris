from django.urls import path
from .views import SingnUpView

urlpatterns = [
    path('signup/', SingnUpView.as_view(), name="signup")

]