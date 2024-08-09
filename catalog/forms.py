import re

from django.forms import ModelForm, forms

from catalog.models import Product, Version

PROHIBITED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'category']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validate_prohibited_words(name, 'name')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validate_prohibited_words(description, 'description')
        return description

    def validate_prohibited_words(self, text, field_name):
        for word in PROHIBITED_WORDS:
            if re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE):
                raise forms.ValidationError(f"Поле содержит запрещенное слово: {word}")


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_current']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control", })
        self.fields["is_current"].widget.attrs["class"] = "form-check-input"