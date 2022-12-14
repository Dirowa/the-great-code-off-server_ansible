from django import forms

from . import models


class EntryForm(forms.ModelForm):
    """Define training request form."""

    error_css_class = "error"

    class Meta:
        """Define form metadata."""

        model = models.Entry
        fields = (
            "user",
            "name",
            "time",
            "complexity",
            "memory",
        )
