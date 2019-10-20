from django.urls import path

from .views import BranchListView, BranchRetrieveView

urlpatterns = [
    path('<slug:ifsc>/', BranchRetrieveView.as_view()),
    path('', BranchListView.as_view()),
]