from django.db import models


# 模型累要繼承models.Models類
# 類裡面的屬性可以對應表裡面的字段
# models.ForeignKey("要關聯的類")
#   CASCADE：此值設定，是級聯刪除；
#   PROTECT：此值設定，是會報完整性錯誤；
#   SET_NULL：此值設定，會把外來鍵設定為null，前提是允許為null；
#   SET_DEFAULT：此值設定，會把設定為外來鍵的預設值；
#   SET()：此值設定，會呼叫外面的值，可以是一個函式。
# 創建一個對象(模型)操作一個數據
###############################################################################
# Create your models here.
class Person(models.Model):
    P_name = models.CharField(max_length=50)
    lastTime = models.DateField(auto_now=True)
    createTime = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.P_name


class About(models.Model):
    P_about = models.CharField(max_length=200)
    P_Person = models.ForeignKey("Person", on_delete=models.CASCADE)

    def __str__(self):
        return self.P_about


class Education(models.Model):
    P_Person = models.ForeignKey("Person", on_delete=models.CASCADE)
    E_university = models.CharField(max_length=20)
    E_major = models.CharField(max_length=20)
    E_graduate = models.DateField()

    def __str__(self):
        return self.E_university


class Work(models.Model):
    P_Person = models.ForeignKey("Person", on_delete=models.CASCADE)
    W_posinion = models.CharField(max_length=20)
    W_company = models.CharField(max_length=20)
    W_content = models.CharField(max_length=200)
    W_start_date = models.DateField()
    W_end_date = models.DateField()

    def __str__(self):
        return self.W_posinion


class Recent(models.Model):
    P_Person = models.ForeignKey("Person", on_delete=models.CASCADE)
    R_recent = models.CharField(max_length=200)

    def __str__(self):
        return self.R_recent


class Skills(models.Model):
    P_Person = models.ForeignKey("Person", on_delete=models.CASCADE)
    S_skills = models.CharField(max_length=30)

    def __str__(self):
        return self.S_skills


class Portfolio(models.Model):
    P_Person = models.ForeignKey("Person", on_delete=models.CASCADE)
    Por_name = models.CharField(max_length=20)
    Por_content = models.CharField(max_length=200)
    Por_web = models.CharField(max_length=200)
    @classmethod
    def Portfolio(cls):
        return cls.Por_name,cls.Por_content,cls.Por_web
###############################################################################
# 結束後
# 1.生成遷移文件 python manage.py makemigrations 在migrations目錄下生成一個遷移文件，數據庫中無資料
# 2.執行遷移 python manage.py migrate

# 查所有數據 類別名稱.objects.all()
# 查詢一個 類別名稱.objects.get(pk=1)
# Person1 =Person()
# Person1.P_name = "Sam"
# Person1.save()
# Person1.P_name = "other" ＃修改
# Person1.save()   ＃儲存
# Person1.delete() #刪除
# Person1.About_set.all()
##Person1.Create_set(P_about='dasfasdfjaofd')
