from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("oldhome", views.home_old, name="home_old"),
    path("home1", views.home1, name="home1"),
    path("home2", views.home2, name="home2"),
    path("home3", views.home3, name="home3"),
    path("signup/", views.signup, name="signup"),
    path("stubbitlogout/", views.stubbitlogout, name="stubbitlogout"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.login, name="login"),
    path("organization/", views.AddOrganization, name="organization"),
    path("createstub/", views.createstub, name="createstub"),
    path("refresh/", views.refresh, name="refresh"),
    path("login_message_homeredirect/", views.loginwelcome, name="loginwelcome"),
    path("addOrganization_message_homeredirect/", views.addOrganizationSuccess, name="addOrganizationSuccess"),
    path("createStub_message_homeredirect/", views.addStubSuccess, name="addStubSuccess"),
    path("signupsuccess/", views.signupsuccess, name="signupsuccess"),
    path("edit/", views.edit, name="edit"),
    path("view/", views.view, name="view"),
    path("updatesuccess/", views.updatesuccess, name="updatesuccess"),
    path("deletesuccess/", views.deletesuccess, name="deletesuccess"),
    path("deleteconfirmation/", views.deleteconfirmation, name="deleteconfirmation"),
    path("about/", views.about, name="about")
]
