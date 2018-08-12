
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .redis_for_view import run_task

from .models import PorterItem

# Create your views here.


from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = "main_page/index.html"


class ResListView(ListView):
    model = PorterItem
    context_object_name = 'scrap_items'
    template_name = 'main_page/item_list.html'
    paginate_by = 10


def start_scrap(request):
    if request.method == 'POST':
        obj = request.POST.get("code", "")
        if obj == "clothing":
            link = 'https://www.net-a-porter.com/us/en/d/Shop/Clothing/All'
            run_task(link)
            return render(request, 'main_page/work.html')
        elif obj == "shoes":
            link = 'https://www.net-a-porter.com/us/en/d/Shop/Shoes/All'
            run_task(link)
            return render(request, 'main_page/work.html')

    return redirect('index')
