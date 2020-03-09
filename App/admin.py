from django.contrib import admin
# 創建管理用戶 python manage.py createsuperuser
# 添加數據表
# Register your models here.
from django.contrib.admin import ModelAdmin

from .models import Person, About, Education, Work, Recent, Skills, Portfolio


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


# AboutAdmin
class AboutAdmin(admin.ModelAdmin):  # 自定義管理介面
    # 列表頁屬性
    list_display = ['P_Person', 'P_about']  # 顯示字段
    list_filter = ['P_Person']  # 過濾器功能
    search_fields = ['P_Person']  # 尋找字段功能
    list_per_page = 5  # 顯示五個數據

    # 添加、修改夜屬性
    # fileds = []  # 可以規定屬性的先後順序
    # fieldsets = [] ＃給屬性分組，不能和fileds同時使用


admin.site.register(About, AboutAdmin)


# EducationAdmin
class EducationAdmin(admin.ModelAdmin):  # 自定義管理介面
    # 列表頁屬性
    list_display = ['P_Person', 'E_university', 'E_major', 'E_graduate']  # 顯示字段
    list_filter = ['P_Person']  # 過濾器功能
    search_fields = ['P_Person']  # 尋找字段功能
    list_per_page = 5  # 顯示五個數據

    # 添加、修改夜屬性
    # fileds = []  # 可以規定屬性的先後順序
    # fieldsets = [] ＃給屬性分組，不能和fileds同時使用


admin.site.register(Education, EducationAdmin)


# WorkAdmin
class WorkAdmin(admin.ModelAdmin):  # 自定義管理介面
    # 列表頁屬性
    list_display = ['P_Person', 'W_posinion', 'W_company', 'W_content', 'W_start_date', 'W_end_date']  # 顯示字段
    list_filter = ['P_Person']  # 過濾器功能
    search_fields = ['P_Person']  # 尋找字段功能
    list_per_page = 5  # 顯示五個數據

    # 添加、修改夜屬性
    # fileds = []  # 可以規定屬性的先後順序
    # fieldsets = [] ＃給屬性分組，不能和fileds同時使用


admin.site.register(Work, WorkAdmin)


# RecentAdmin
class RecentAdmin(admin.ModelAdmin):  # 自定義管理介面
    # 列表頁屬性
    list_display = ['P_Person', 'R_recent']  # 顯示字段
    list_filter = ['P_Person']  # 過濾器功能
    search_fields = ['P_Person']  # 尋找字段功能
    list_per_page = 5  # 顯示五個數據

    # 添加、修改夜屬性
    # fileds = []  # 可以規定屬性的先後順序
    # fieldsets = [] ＃給屬性分組，不能和fileds同時使用


admin.site.register(Recent, RecentAdmin)


# SkillsAdmin
class SkillsAdmin(admin.ModelAdmin):  # 自定義管理介面
    # 列表頁屬性
    list_display = ['P_Person', 'S_skills']  # 顯示字段
    list_filter = ['P_Person']  # 過濾器功能
    search_fields = ['P_Person']  # 尋找字段功能
    list_per_page = 5  # 顯示五個數據

    # 添加、修改夜屬性
    # fileds = []  # 可以規定屬性的先後順序
    # fieldsets = [] ＃給屬性分組，不能和fileds同時使用


admin.site.register(Skills, SkillsAdmin)


# PortfolioAdmin
class PortfolioAdmin(admin.ModelAdmin):  # 自定義管理介面
    # 列表頁屬性
    list_display = ['P_Person', 'Por_name', 'Por_content', 'Por_web']  # 顯示字段
    list_filter = ['P_Person']  # 過濾器功能
    search_fields = ['P_Person']  # 尋找字段功能
    list_per_page = 5  # 顯示五個數據

    # 添加、修改夜屬性
    # fileds = []  # 可以規定屬性的先後順序
    # fieldsets = [] ＃給屬性分組，不能和fileds同時使用


admin.site.register(Portfolio, PortfolioAdmin)
