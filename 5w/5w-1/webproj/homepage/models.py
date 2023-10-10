from django.db import models
# 모듈 내 데이터 베이스의 스키마 등을 class형태로 만듦.
# class <model name>(models.Model):

# Create your models here.

class COFFEE(models.Model):
    def __str__(self) -> str:
        return self.name #객체의 이름 출력
    # Feild 1
    name = models.CharField(default='', null=False, max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)

    
    '''
    문자열 : CharField
    숫자 : IntegerField, SmallIntegerField, ...
    논리형 : BooleanField
    시간 / 날짜 : DateTimeField
    ---
    CharField(default : 기본 default값 지정,
            null : null허용 여부 결정, 
            max_length : 최대 길이 지정
            )
    '''

    # Feild 2