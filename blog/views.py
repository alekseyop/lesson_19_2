from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogListViewAll(ListView):
    model = Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview_image', 'is_published']
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_slug = form.save()
            new_slug.slug = slugify(new_slug.title)
            new_slug.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview_image', 'is_published']

    # success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_slug = form.save()
            new_slug.slug = slugify(new_slug.title)
            new_slug.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
