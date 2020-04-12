from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label='사용자 이름',
                               error_messages={'required': '아이디를 입력하세요'})
    password = forms.CharField(widget=forms.PasswordInput, label='비밀번호')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                my_user = User.objects.get(username=username)
            except User.DoesNotExist:
                self.add_error('username','아이디가 없습니다')
                return
            if not check_password(password, my_user.password):
                self.add_error('password', '비밀번호가 틀렸습니다')  # 특정 필드에다가 error를 넣음
            else:
                self.user_id = my_user.id
