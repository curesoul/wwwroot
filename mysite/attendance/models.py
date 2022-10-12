from django.db import models


class MonthList(models.Model):
    TYPES = [
        (0, '平日'),
        (1, '休日'),
        (2, '法定'),
    ]
    type_month = models.IntegerField(choices=TYPES, verbose_name='日期类型')
    day_month = models.DateField(blank=True, verbose_name='出表时间')

    class Meta:
        verbose_name = verbose_name_plural = '月日清单'


class PersonList(models.Model):
    code = models.CharField(max_length=20, verbose_name='人员编号')
    name = models.CharField(max_length=100, verbose_name='姓名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '人员清单'


class AttendanceLog(models.Model):
    TYPES = [
        (0, '白班'),
        (1, '夜班'),
    ]
    day = models.ForeignKey(MonthList, on_delete=models.CASCADE, verbose_name='日期')
    person = models.ForeignKey(PersonList, on_delete=models.CASCADE, verbose_name='姓名')
    type = models.IntegerField(choices=TYPES, verbose_name='白班夜班')
    worktime = models.IntegerField(default=8, verbose_name='出勤时间')
    overtime = models.IntegerField(verbose_name='加班时间')
    absencetime = models.IntegerField(verbose_name='缺勤时间')
    remark = models.CharField(max_length=255, verbose_name='备注')

    def __str__(self):
        return self.day + self.person

    class Meta:
        verbose_name = verbose_name_plural = '出勤记录'



