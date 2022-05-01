from django.db import models

# to=user 사용자와 연결하기 위한 import
from django.contrib.auth import get_user_model
User = get_user_model()

#자주묻는 질문
class Faq(models.Model):
    # Choices로 연결하기 위한 카테고리 목록
    category_Choices = [
        ('1', '일반'), #General
        ('2', '계정'), #admin
        ('3', '기타'), #etc
    ]  
    category_list = models.CharField(
        max_length=2,
        choices=category_Choices,
    )
    title = models.CharField(verbose_name='제목', max_length=30)     # 제목 글자수 제한
    content = models.TextField('질문')      # 질문 내용
    image = models.ImageField(verbose_name='이미지', null=True, blank = True)

    created_at = models.DateTimeField('생성일시', auto_now_add=True)      # 작성시(지금) 시간 
    updated_at = models.DateTimeField('최종 수정일시', auto_now=True)      # 수정(객체등록) 자동 업데이트
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='faq_created_by')    
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='faq_updated_by')

#1:1 문의
# 카테고리, 제목, 이메일, 문자메시지, 내용, 이미지
class inquiry(models.Model):
    # Choices로 연결하기 위한 카테고리 목록
    category_Choices = [
        ('1', '일반'), #General
        ('2', '계정'), #admin
        ('3', '기타'), #etc
    ]  
    category_list = models.CharField(
        max_length=2,
        choices=category_Choices,
    )
    title = models.CharField(verbose_name='제목', max_length=30)     # 제목 글자수 제한
    mail_add = models.EmailField('이메일')      # 이메일
    is_mail = models.BooleanField(verbose_name='이메일 수신 여부', default=False)

    phone = models.CharField(verbose_name='문자', max_length=11, blank=True)      # 문자메시지
    is_phone = models.BooleanField(verbose_name='문자 수신 여부', default=False)

    content = models.TextField('질문')      # 질문 내용
    image = models.ImageField(verbose_name='이미지', null=True, blank = True)

    created_at = models.DateTimeField('생성일시', auto_now_add=True)      # 작성시(지금) 시간 
    updated_at = models.DateTimeField('최종 수정일시', auto_now=True)      # 수정(객체등록) 자동 업데이트
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='inquiry_created_by')    
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='inquiry_updated_by')

# 답변
# 답변 내용, 참조 문의글, 생성자, 생성 일시, 최종 수정자, 최종 수정 일시
class answer(models.Model):
    content = models.TextField(verbose_name='답변')     # 답변 내용
    inquiry = models.ForeignKey(to='inquiry', on_delete=models.CASCADE)        #inquiry 삭제시 answer 전체 삭제 

    created_at = models.DateTimeField('생성일시', auto_now_add=True)      # 작성시(지금) 시간 
    updated_at = models.DateTimeField('최종 수정일시', auto_now=True)      # 수정(객체등록) 자동 업데이
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answer_created_by')    
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answer_updated_by')
