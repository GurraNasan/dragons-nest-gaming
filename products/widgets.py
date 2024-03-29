from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove this image')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_widget_templates/custom_clerable_file_input.html'
    )
