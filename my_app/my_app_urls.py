from django.urls import path, include
from .views import *
# from django.views.generic import RedirectView

app_name = 'my_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
    path('success/', SuccessView.as_view(), name='success-page'),
    path('login/', LoginView.as_view(), name='login-page'),
    path('success-account/', SuccessAccountView.as_view(), name='success-account-page'),
    path('signup/', SignUpView.as_view(), name='signup-page'),
    path('house/', HouseView.as_view(), name='house-page'),
    path('work/', include([
        path('', WorkView.as_view(), name='work-page'),
        path('construction/', include([
            path('', WorkConstructionView.as_view(), name='work-construction-page'),
            path('form/', WorkConstructionCreateView.as_view(), name='work-construction-form-page')
        ])),
        path('cleaning/', include([
            path('', WorkCleaningView.as_view(), name='work-cleaning-page'),
            path('form/', WorkCleaningCreateView.as_view(), name='work-cleaning-form-page')
        ])),
        path('other/', include([
            path('', WorkOtherView.as_view(), name='work-other-page'),
            path('form/', WorkOtherCreateView.as_view(), name='work-other-form-page')
        ])),
    ])),
    path('service/', include([
        path('', ServiceView.as_view(), name='service-page'),
        path('form/', ServiceFormView.as_view(), name='service-form-page'),
        path('domestic/', ServiceDomesticView.as_view(), name='service-domestic-page'),
        path('healthy_beauty/', ServiceHealthyBeautyView.as_view(), name='service-healthy-beauty-page'),
        path('transport/', ServiceTransportView.as_view(), name='service-transport-page'),
        path('food/', ServiceFoodView.as_view(), name='service-food-page'),
        path('technic/', ServiceTechnicView.as_view(), name='service-technic-page'),
        path('other/', ServiceView.as_view(), name='service-other-page'),
        path('class/', ServiceClassView.as_view(), name='service-class-page'),
        path('travel/', ServiceTravelView.as_view(), name='service-travel-page'),
    ]))
]
