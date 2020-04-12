from django.db import models

# Create your models here.
class User(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=32,
                                verbose_name='사용자명') # 추훙 field에 대한 명령
    useremail = models.EmailField(max_length=128, verbose_name='이메일 주소')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간') # datetime의 약자
    
    def __str__(self):
        return self.username

    class Meta: # framework에게 내가 원하는 것을 전달할 수 있음
        db_table = 'community_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
