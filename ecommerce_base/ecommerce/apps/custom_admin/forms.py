from django import forms
from ecommerce.apps.catalogue.models import Product,Brand,Category


class ProductUpdateForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Product
 
        # specify fields to be used
        fields = ["title","category",'brand','unit','unit_choices','description','slug',
                  'stock','regular_price','discount_price','is_active'] 

    def __init__(self, *args, **kwargs): 
            super(ProductUpdateForm, self).__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'class': 'form-control'})
            self.fields['category'].widget.attrs.update({'class': 'form-control'})
            self.fields['brand'].widget.attrs.update({'class': 'form-control'})
            self.fields['unit'].widget.attrs.update({'class': 'form-control'})
            self.fields['unit_choices'].widget.attrs.update({'class': 'form-control'})
            self.fields['description'].widget.attrs.update({'class': 'form-control'})
            self.fields['slug'].widget.attrs.update({'class': 'form-control'})
            self.fields['stock'].widget.attrs.update({'class': 'form-control'})
            self.fields['regular_price'].widget.attrs.update({'class': 'form-control'})
            self.fields['discount_price'].widget.attrs.update({'class': 'form-control'})
            self.fields['is_active'].widget.attrs.update({'class': 'form-control'})

class BrandUpdateForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Brand
 
        # specify fields to be used
        fields = ["name",'slug','is_active','image'] 

    def __init__(self, *args, **kwargs): 
            super(BrandUpdateForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({'class': 'form-control'})
            self.fields['slug'].widget.attrs.update({'class': 'form-control'})
            self.fields['is_active'].widget.attrs.update({'class': 'form-control'})
            self.fields['image'].widget.attrs.update({'class': 'form-control'})


class CategoryUpdateForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Category
 
        # specify fields to be used
        fields = ["name","image",'parent','slug','is_active'] 

    def __init__(self, *args, **kwargs): 
            super(CategoryUpdateForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({'class': 'form-control'})
            self.fields['parent'].widget.attrs.update({'class': 'form-control'})
            self.fields['image'].widget.attrs.update({'class': 'form-control'})
            self.fields['slug'].widget.attrs.update({'class': 'form-control'})
            self.fields['is_active'].widget.attrs.update({'class': 'form-control'})

    