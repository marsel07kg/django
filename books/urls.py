from books import views
from django.urls import path
from . import views
from .views import BookListView

urlpatterns = [
    path("all_products/", BookListView.as_view()),
    path("manga/", views.manga_view),
    path("comics/", views.comics_view),
    path("another thing/", views.another_things_view),
    path("", views.BookListView.as_view()),
    path("Librarys/<int:id>/", views.BookDetailView.as_view()),
    path("Librarys/<int:id>/delete/", views.DeleteBookView.as_view()),
    path("Librarys/<int:id>/update/", views.EditBookView.as_view()),
    path("create_book/", views.CreateBookView.as_view()),
    path("search/", views.SearchView.as_view(), name="search"),
    path("hello/", views.name_age),
    path("bio/", views.bio),
    path("number/", views.random_number),
    path("time/", views.current_time),
]
