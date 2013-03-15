import settings
from django import forms
from django.forms import formsets
from django.forms import  util as form_util
from uw.models import Activity
from userprofile.models import UserProfile


class CreateActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ['author', 'date', 'visible']


class AddProgramForm(forms.ModelForm):
    program_name = forms.CharField(max_length=100)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.user = kwargs['instance']

#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(user=instance)

#class CreateUserProfileForm(forms.ModelForm):
#    class Meta:
#        model = models.UserProfile
#
#
#class UserProfileForm(forms.Form):
#  """Creates a form for user settings.
#
#  Attributes:
#  """
#
#  about_me = forms.CharField(widget=forms.TextInput(attrs={'size': 30}),
#                               label=('About Me'))
#
#  gender = forms.CharField(widget=forms.TextInput(attrs={'size': 6}),
#                               label=('Gender'))
#
#  date_of_birth = forms.DateTimeField(widget=forms.TextInput(attrs={'size': 30}),
#                               label=('Date of Birth'))
#
#  def __init__(self, *args, **kwargs):
#    super(UserProfileForm, self).__init__(*args, **kwargs)
#
#    about_me_display = []
#    self.fields['about_me'].attrs = about_me_display
#
#    gender_display = []
#    self.fields['gender'].attrs = gender_display
#
#    date_of_birth_display = []
#    self.fields['date_of_birth'].attrs = date_of_birth_display
#
#
#  def UpdateUserProfile(self, user):
#    """Updates User Profile.
#
#    Args:
#      user: The models.UserProfile who is using creating the program.
#    """
#    data = self.cleaned_data
#    user.about_me = data['about_me']
#    user.gender = data['gender']
#    user.date_of_birth = data['date_of_birth']
#  
#    if not user.about_me:
#      msg = [_('Invalid about me')]
#      self._errors['about_me'] = form_util.ValidationError(msg).messages
#
#    if not user.gender:
#      msg = [_('Invalid gender')]
#      self._errors['gender'] = form_util.ValidationError(msg).messages
#
#    if not user.date_of_birth:
#      msg = [_('Invalid date of birth')]
#      self._errors['date_of_birth'] = form_util.ValidationError(msg).messages
#
#    if self._errors:
#      return None
#
#    properties = {
#       'about_me': user.about_me,
#       'gender': user.gender,
#       'date_of_birth': user.date_of_birth,
#    }
#    user.save()
#      
#  @staticmethod
#  def BuildPostData(user):
#    """Create the post data to populate the form from an existing user."""
#    post_data = {}
#    post_data['about_me'] = user.about_me
#    post_data['gender'] = user.gender
#    post_data['date_of_birth'] = user.date_of_birth
#    return post_data
