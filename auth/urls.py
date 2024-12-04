from django.contrib import admin
from django.urls import path, include
from . import views
from .views import (
    RouteListCreateView, RouteDetailView,
    ScheduleListCreateView, ScheduleDetailView,
    TrainListCreateView, TrainDetailView,
    StationListCreateView, StationDetailView,
    SeatListCreateView, SeatDetailView,
    TicketListCreateView, TicketDetailView,
    PaymentListCreateView, PaymentDetailView,
    HaltListCreateView, HaltDetailView
)
urlpatterns = [
    
    # Auth Views
    path("login/",views.login, name="login"),
    path("logout/",views.logout, name="logout"),
 
]