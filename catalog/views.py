from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    # template_name = 'catalog/product_form.html'
    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    # form_class = ProductForm
    # success_url = reverse_lazy('catalog:home')
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['object_list']

        active_versions = {}
        for product in products:
            current_versions = product.versions.filter(is_current=True)
            active_versions[product.id] = current_versions.first()

        context['active_versions'] = active_versions
        return context


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    # success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data.get('formset')
        if formset.is_valid():
            active_versions_count = sum(1 for form in formset if form.cleaned_data.get('is_current'))
            if active_versions_count > 1:
                formset.non_form_errors = ['Вы можете выбрать только одну активную версию для продукта.']
                return self.form_invalid(form)  # Возвращаем ошибку формы
            formset.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        context_data = self.get_context_data(form=form)
        # formset = context_data.get('formset')
        # if formset.errors:
        #     return self.render_to_response(self.get_context_data(form=form))
        # else:
        #     return super().form_invalid(form)
        return self.render_to_response(context_data)


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def contacts(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(name, phone, message)

        return render(request, 'catalog/contacts.html')


class ProductDeleteConfirm(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
