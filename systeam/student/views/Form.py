from django import forms
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

TOPIC_CHOICES = (
  ('leve1', '唱歌'),
  ('leve2', '跳舞'),
  ('leve3', '运动'),
)

class likeForm(forms.Form):
    like = forms.ChoiceField(label='爱好',choices=TOPIC_CHOICES)
    food = forms.CharField(label="爱吃的",max_length=100)

class uploadfileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()




