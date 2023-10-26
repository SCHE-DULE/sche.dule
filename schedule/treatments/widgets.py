from django.forms import widgets

class CustomSelect2Widget(widgets.SelectMultiple):

    def render(self, name, value, attrs=None, choices=()):
        select_html = super().render(name, value, attrs, choices)
        label = attrs.get('label', '')
        label_html = f'<label for="{attrs["id"]}" class="form-label">{label}</label>'
        return f'<div class="col-md-6 mb-4" data-select2-id="45">{label_html}<div class="position-relative" data-select2-id="44">{select_html}</div></div>'
