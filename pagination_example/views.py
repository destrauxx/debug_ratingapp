from django.shortcuts import render
from rating.models import Rating

# Create your views here.
def pagination_view(request, *args, **kwargs):
    qs = Rating.objects.all()
    page = int(request.GET.get('page', 1))
    paginate_by = 5
    start_index = (page * paginate_by) - paginate_by
    # print(start_index)
    end_index = page * paginate_by
    next_page = page + 1
    # print(end_index)
    # print(list(qs))
    return render(request, 'pagination_example/pagination_example.html', {'page': page, 'data_list': qs[start_index:end_index], 'next': next_page, 'prev': page-1 or 1})