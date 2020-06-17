# forms.py ---
#
# Filename: forms.py
# Author: Louise <louise>
# Created: Mon Apr 27 20:55:38 2020 (+0200)
# Last-Updated: Wed Jun 17 18:39:20 2020 (+0200)
#           By: Louise <louise>
#
"""
Forms to check the data given to the signup page or the edit page..
"""
from django import forms

class UserForm(forms.Form):
    """
    Base form for the signup form and the edit profile form.
    """
    first_name = forms.CharField(label="Prénom",
                                 max_length=30)
    last_name = forms.CharField(label="Nom de famille",
                                max_length=30,
                                required=False)
    email = forms.EmailField(label="Adresse e-mail")

class SignupForm(UserForm):
    """
    Form for the signup page.
    """
    username = forms.CharField(label="Nom d'utilisateur",
                               max_length=255)
    password = forms.CharField(label="Mot de passe")

class EditProfileForm(UserForm):
    """
    Form to edit a profile.
    """
    password = forms.CharField(label="Mot de passe actuel")
