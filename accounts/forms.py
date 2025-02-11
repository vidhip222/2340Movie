from django import forms
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe


class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ""
        return mark_safe(
            "".join(
                [
                    f'<div class="alert alert-danger" role="alert">{e}</div>'
                    for e in self
                ]
            )
        )


class CustomUserCreationForm(UserCreationForm):
    # Add the email field.
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Update the default help texts and add a class to the widgets.
        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = ""
            self.fields[fieldname].widget.attrs.update({"class": "form-control"})


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help texts from both password fields.
        self.fields["new_password1"].help_text = ""
        self.fields["new_password2"].help_text = ""

