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
    list_display = ('title', 'category_list', 'created_at', 'created_by')
    search_fields = ('title', 'mail_add', 'phone')
    search_help_text = '제목, 이메일, 전화번호로 검색 가능합니다.'
    list_filter = ('category_list',)
    inlines = [answerInline]

# 답변 = 인라인모델
#@admin.register(answer)
#class answerModelAdmin(admin.ModelAdmin):
# answer 보기위한 table 컬럼 구성
#    list_display = ('id', 'content', 'inquiry', 'writer', 'create_at')
