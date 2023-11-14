from django.db import models

# Create your models here.

class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    email = models.EmailField(max_length=300, verbose_name="ایمیل")
    full_name = models.CharField(max_length=300, verbose_name="متن تماس با ما")
    message = models.TextField(verbose_name="متن پیام ارسالی")
    created_date = models.DateTimeField(verbose_name="تاریخ ایجاد" , auto_now_add=True)
    is_read_by_admin = models.BooleanField(verbose_name="خوانده شده توسط ادمین ")
    response = models.TextField(verbose_name="متن پیام ارسالی", null=True, blank=True)

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "لیست تماس با ما"

    def __str__(self):
        return self.title