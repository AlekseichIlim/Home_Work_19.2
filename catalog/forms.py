from django.forms import ModelForm, forms

from catalog.models import Product

valid_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'picture',)

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
