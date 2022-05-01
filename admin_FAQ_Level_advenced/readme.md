### Advanced Mission

---

<aside>
💡 고객센터 관리자 페이지 기능 및 사용성 개선

</aside>

### 미션 내용 : 기본 관리자 페이지의 사용성 개선 및 답변 상태 관리 기능 추가

### 목표

- 고객센터 담당자 업무 효율을 위한 사용성 개선
- 1:1문의 상태관리를 통한 고객응대 효율 향상

### 요구사항

- 1:1문의(`Inquiry`) 모델의 “상태” 필드 추가
    - 상태 : 문의 등록, 접수 완료, 답변 완료
- 1:1문의(`Inquiry`) 목록, 필터에 상태 추가
- 1:1문의 검색 필드 추가 : 사용자 모델의 `username`, `phone`, `email`
- 1:1문의 답변 완료 안내 발송 기능 추가
    - 관리자 페이지 체크된 문의 안내 발송
    - 1:1문의의 is_email, is_phone가 True인 경우 email, phone 데이터 `print()` 출력
        
        ※ action을 추가 학습을 위한 목적으로 실제 문자, 메일은 발송하지 않습니다.
        

### 힌트

- 참조 관계 모델 필드 검색 참고
    - [https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)
    - [https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups-1](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups-1)
- 기능 추가 참고
    - [https://docs.djangoproject.com/en/4.0/ref/contrib/admin/actions/#admin-actions](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/actions/#admin-actions)
    - [https://docs.djangoproject.com/en/4.0/ref/contrib/admin/actions/](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/actions/)


---
![그림4](https://user-images.githubusercontent.com/67627129/166158843-1008247b-7702-47b8-a530-03a2d378cb8b.png)


![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/67627129/166158971-f69a5f16-6832-456a-92f9-afb58af4f836.gif)
