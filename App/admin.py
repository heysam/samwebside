from django.contrib import admin
# 創建管理用戶 python manage.py createsuperuser
# 添加數據表
# Register your models here.
from django.contrib.admin import ModelAdmin

from .models import Person, About, Educattion, Work, Recent, Skills, Portfolio


# 註冊
class PersonAdmin(admin.ModelAdmin):  # 自定義管理介面
    # 列表頁屬性
    list_display = ['P_name', 'lastTime', 'createTime']  # 顯示字段
    list_filter = ['P_name']  # 過濾器功能
    search_fields = ['P_name']  # 尋找字段功能
    list_per_page = 5  # 顯示五個數據

    # 添加、修改夜屬性
    # fileds = []  # 可以規定屬性的先後順序
    # fieldsets = [] ＃給屬性分組，不能和fileds同時使用


admin.site.register(Person, PersonAdmin)

admin.site.register(About)
admin.site.register(Educattion)
admin.site.register(Work)
admin.site.register(Recent)
admin.site.register(Skills)
admin.site.register(Portfolio)
