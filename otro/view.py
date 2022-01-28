from django.views import View
from django.shortcuts import render


class FotosView(View):
    def get(self, request):
        
        return render(request, 'fotos.html')