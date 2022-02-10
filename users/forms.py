from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column , Submit



class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'user_role', 'password1', 'password2' ,'Departament']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method='post'
        self.helper.add_input(Submit('Register User','Register User'))

        self.helper.layout = Layout(
            Row(
                Column('username'),
                Column('password1'),
                Column('password2')
            ),
            Row(
                Column('email'),
                Column('user_role')

            ),
            Row(
                Column('first_name'),
                Column('last_name')
            ),
            Row(
                Column('Departament'),
            ),

        )




        
class CustomerUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'user_role','Departament']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method='post'
        self.helper.add_input(Submit('Update User','Update User'))

        self.helper.layout = Layout(
            Row(
                Column('username'),
               
            ),
            Row(
                Column('email'),
                Column('user_role')

            ),
            Row(
                Column('first_name'),
                Column('last_name')
            ),
            Row(
                Column('Departament'),
            ),

        )







class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
