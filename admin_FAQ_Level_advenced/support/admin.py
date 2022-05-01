import email
from django.contrib import admin

from .models import Faq, inquiry, answer

class answerInline(admin.TabularInline):
    model = answer
    extra = 1
    min_num = 0
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

# 제목, 카테고리, 최종 수정 일시
@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
# Faq 보기위한 table 컬럼 구성
    list_display = ('title', 'category_list', 'updated_at')
    search_fields = ('title',)
    search_help_text = '제목으로 검색 가능합니다.'
    list_filter = ('category_list',)

# 질문 제목, 카테고리, 생성 일시, 생성자
@admin.register(inquiry)
class inquiryModelAdmin(admin.ModelAdmin):
# inquiry 보기위한 table 컬럼 구성
    list_display = ('title', 'category_list', 'created_at', 'created_by', 'status_list')
    search_fields = ('title', 'created_by', 'mail_add', 'phone')
    search_help_text = '제목, 작성자, 이메일, 전화번호로 검색 가능합니다.'
    list_filter = ('category_list','status_list',)
    inlines = [answerInline]

    actions = ['send_inquiry_massage',]

    def send_inquiry_massage(modeladmin, request, queryset):
        for item in queryset:
            check_send_mail = item.is_mail
            send_mail = item.mail_add

            check_send_phone = item.is_phone
            send_phone = item.phone

            if check_send_mail == True and send_phone !='' and check_send_phone == True and send_phone !='':
                print(send_mail)
                print(send_phone)
            elif check_send_mail == True and send_phone !='':
                print(send_mail)
            elif check_send_phone == True and send_phone !='':
                print(send_phone)
            else:
                print("데이터 이상 확인 바람")


# 답변 = 인라인모델
#@admin.register(answer)
#class answerModelAdmin(admin.ModelAdmin):
# answer 보기위한 table 컬럼 구성
#    list_display = ('id', 'content', 'inquiry', 'writer', 'create_at')

