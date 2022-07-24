from django.urls import path,include
from . import views

urlpatterns = [
    path('view-books',views.viewBooks),
    path('edit-book',views.editbook),
    path('delete-book',views.deleteBook),
    path('search-book',views.searchBook),
    path('new-book',views.NewBook),
    path('add',views.Add),
    path('edit',views.edit),
    path('search',views.search),
    # path('login',views.userLogin),
    # path('logout',views.userLogout),
]
