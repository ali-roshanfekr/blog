import jdatetime
from django.db import models
from user_module.models import UserModel


class MessageModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
    text = models.CharField(max_length=2000, verbose_name='متن')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='فرستاده شده در')
    reply = models.BooleanField(default=True, verbose_name='پاسخ')

    def __str__(self):
        return self.user.username

    def get_date_fa(self):
        sent_at_fa = jdatetime.GregorianToJalali(self.sent_at.year, self.sent_at.month, self.sent_at.day)
        final_sent_at = sent_at_fa.getJalaliList()
        return f'{final_sent_at[0]}/{final_sent_at[1]}/{final_sent_at[2]}'

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
