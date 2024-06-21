from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from . import models, forms
import random
import datetime

class SearchView(generic.ListView):
    template_name = 'Librarys/book_list.html'
    context_object_name = 'book_list'
    paginate_by = 5

    def get_queryset(self):
        return models.Book.objects.filter(name__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class BookListView(generic.ListView):
    template_name = 'Librarys/book_list.html'
    context_object_name = 'book_list'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

class BookDetailView(generic.DetailView):
    template_name = 'Librarys/book_detail.html'
    context_object_name = 'book_detail'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

class CreateBookView(generic.CreateView):
    template_name = 'Librarys/create_book.html'
    form_class = forms.BookForm
    success_url = '/Librarys/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)

class DeleteBookView(generic.DeleteView):
    template_name = 'Librarys/delete_book.html'
    success_url = '/Librarys/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

class EditBookView(generic.UpdateView):
    template_name = 'Librarys/edit_book.html'
    form_class = forms.BookForm
    success_url = '/Librarys/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditBookView, self).form_valid(form=form)

def manga_view(request):
    if request.method == 'GET':
        manga_tags = models.Library.objects.filter(tags__name='manga').order_by('-id')
        return render(
            request,
            template_name='products/manga_tag.html',
            context={'manga_tags': manga_tags},
        )

def comics_view(request):
    if request.method == 'GET':
        comics_tags = models.Library.objects.filter(tags__name='comic').order_by('-id')
        return render(
            request,
            template_name='products/comics_tags.html',
            context={'comics_tags': comics_tags},
        )

def another_things_view(request):
    if request.method == 'GET':
        another_things_tags = models.Library.objects.filter(tags__name='another thing').order_by('-id')
        return render(
            request,
            template_name='products/another_things_tag.html',
            context={'another_things_tags': another_things_tags},
        )
def all_products(request):
    if request.method == 'GET':
        products = models.Library.objects.filter().order_by('-id')
        return render(
            request,
            template_name='products/all_products.html',
            context={
                'products': products
            }
        )

# def book_detail_views(request, id):
#     if request.method == 'GET':
#         emp_id = get_object_or_404(models.Book, id=id)
#         return render(
#             request,
#             template_name='employees/book_detail.html',
#             context={
#                 'emp_id': emp_id,
#             }
#         )


# def create_book_view(request):
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Book added successfully</h3>'
#                                 '<a href=/employees/>список книг</a>')
#     else:
#         form = forms.BookForm()
#
#     return render(
#         request,
#         template_name='employees/create_book.html',
#         context={'form': form}
#        )

# def drop_book_view(request, id):
#     emp_id = get_object_or_404(models.Book, id=id)
#     emp_id.delete()
#     return HttpResponse('<h3>Book deleted successfully</h3>'
#                         '<a href=/employees/>список книг</a>')

# def edit_book_view(request, id):
#     emp_id = get_object_or_404(models.Book, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, instance=emp_id)
#         form.save()
#         return HttpResponse('<h3>Book edited successfully</h3>'
#                             '<a href=/employees/>список книг</a>')
#     else:
#         form = forms.BookForm(instance=emp_id)
#         return render(
#             request,
#             template_name='employees/edit_book.html',
#             context={
#                 'form': form,
#                 'emp_id': emp_id
#             }
#         )

# def book_list_views(request):
#     if request.method == 'GET':
#         queryset = models.Book.objects.filter().order_by('-id')
#         return render(
#             request,
#             template_name='employees/book_list.html',
#             context={
#                 'emp': queryset
#             }
#         )

def name_age(request):
    if request.method == 'GET':
        return HttpResponse("Привет меня зовут Бекболотов Марсель мне 17 лет")

def bio(request):
    if request.method == 'GET':
        return HttpResponse("кубик рубик, шахматы, теннис, программирование")

def random_number(request):
    if request.method == 'GET':
        number = random.randint(0, 100)
        return HttpResponse(number)

def current_time(request):
    if request.method == 'GET':
        time = datetime.datetime.now()
        return HttpResponse(time)
# Create your views here.
