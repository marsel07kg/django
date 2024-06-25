from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class StatusClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            status_of_reader = (request.POST.get('status_of_reader'))
            if status_of_reader == 'not_readers':
                return HttpResponseBadRequest('Вы не читаете книгу ')

            elif status_of_reader == 'beginners':
                request.literary_club = 'beginners'
            elif status_of_reader =='amateur':
                request.literary_club = 'amateur'
            elif status_of_reader =='veteran':
                request.literary_club = 'veteran'
            else:
                return HttpResponseBadRequest('Вы не читаете книгу ')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'literary_club', 'Клуб не определен')

