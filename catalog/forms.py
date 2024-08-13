from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version

valid_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'picture', 'owner')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in valid_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Запрещенный продукт')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in valid_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Запрещенный продукт')
        return cleaned_data


class VersionForm(StyleMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
