from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from django.shortcuts import get_object_or_404
from .models import *
# Create your views here.

class MovieList(View):
    template_name="Home.html"
    def get(self, request, *args, **kwargs):
        movie_list=Movie.objects.all().order_by("-id")
        paginator = Paginator(movie_list, 8)  # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,self.template_name,locals())

def MovieView(request,pk):
    movie=get_object_or_404(Movie,id=pk)
    return render(request,"movieView.html",locals())