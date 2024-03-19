from django.urls import path
from .import views
urlpatterns = [
   path("",views.index, name ="index_page") ,
   path("squad",views.squad, name ="squad_page"),
   path("table", views.table, name ="table_page"),
   path("match",views.match, name ="match_page"),
   path("ticket",views.ticket, name ="ticket_page"),
   path("fanPage",views.fanPage, name ="fanPage"),
   path("fan",views.FansFormViews.as_view(), name ="fan_page"),
   path("profile",views.FanPictureView.as_view(), name ="fan_picture"),
   path("thankyou",views.ThankyouView.as_view(), name ="thankyou_page"),
   path("fan_list",views.FansListView.as_view(), name ="fan_list_page"),
   path("pictureView",views.PictureView.as_view(), name ="picture_page"),
   path("fan_list/favorite",views.FavoriteView.as_view()),
   path("fan_list/<int:pk>",views.SingleFanView.as_view(), name ="single_fan_page"),
   path ("squad/<str:player>", views.players_information, name= "players_information"),
   path("login",views.loginPage, name ="login_page"),
   path("signup",views.signup, name ="register_page"),
   path("logout",views.logoutPage, name ="logout_page"),
   path("forgot",views.forgot, name ="forget_page"),
]