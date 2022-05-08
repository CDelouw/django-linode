from django.urls import path
from .views import *

app_name = 'my_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
    path('success/', SuccessView.as_view(), name='success-page'),
    path('work/', WorkView.as_view(), name='work-page'),
    path('work/construction/', WorkConstructionView.as_view(), name='work-construction-page'),
    path('work/cleaning/', WorkCleaningView.as_view(), name='work-cleaning-page'),
    path('work/other/', WorkOtherView.as_view(), name='work-other-page'),
    path('work/construction/form/', WorkConstructionCreateView.as_view(), name='work-construction-form-page'),
    path('work/cleaning/form/', WorkCleaningCreateView.as_view(), name='work-cleaning-form-page'),
    path('work/other/form/', WorkOtherCreateView.as_view(), name='work-other-form-page'),
]
