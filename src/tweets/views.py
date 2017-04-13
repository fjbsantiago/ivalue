from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin

class TweetCreateView(FormUserNeededMixin, FormView):

    template_name = 'tweets/tweet_create.html'
    form_class = TweetModelForm
    success_url = '/tweet'

    login_url = '/admin/login'
    redirect_field_name = 'redirect_to'

    """
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(TweetCreateView, self).form_valid(form)
    """

def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    
    print("tweet_create_view start")    
    if form.is_valid():
        print("form is valid")
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()

    print("tweet_create_view end")

    context = {
        'form': form
    }

    return render(request, 'tweets/tweet_create.html', context)


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        #obj = get_object_or_404(Tweet, pk=pk)
        return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        """
        If you don't use this method, you will simply get queryset
        as object_list in Jinja2 templates.
        If you use it, you can extend this context
        """
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context

"""
class TweetUpdateView(ListView):
    queryset = Tweet.objects.all()

    def get_object(self):
        return Tweet.objects.get(id=1)
"""


"""
def tweet_detail_view(request, tweet_id=1):
    obj = Tweet.objects.get(id=tweet_id)

    context = {
        'object': obj
    }
    return render(request, "detail_view.html", context)

def tweet_list_view(request, id=1):
    queryset = Tweet.objects.all()

    context = {
        'object_list': queryset
    }
    return render(request, "list_view.html", context)
"""