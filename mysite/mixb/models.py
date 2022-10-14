from django.db import models


class Customer(models.Model):
    abbreviation = models.CharField(max_length=10, verbose_name='缩写')
    name = models.CharField(max_length=255, verbose_name='公司名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '客户'


class Item(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='客户')
    name = models.CharField(max_length=255, verbose_name='品名')
    mv = models.CharField(max_length=255, verbose_name='门尼')
    mv_min = models.FloatField(verbose_name='最小值')
    mv_max = models.FloatField(verbose_name='最大值')
    temperature = models.IntegerField(default=100, blank=True, verbose_name='温度')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '品名清单'


class Schedule(models.Model):
    lot = models.IntegerField(verbose_name='批号')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='品名')
    batch = models.IntegerField(verbose_name='回数')
    packages = models.IntegerField(verbose_name='框数')
    mix_a_lot = models.CharField(max_length=6, blank=True, verbose_name='A炼批号')
    mix_b_lot = models.CharField(max_length=6, blank=True, verbose_name='B炼批号')
    notes = models.CharField(max_length=255, blank=True, verbose_name='备注')
    created_time = models.DateTimeField(auto_created=True, verbose_name='添加时间')
    etd = models.DateField(blank=True, verbose_name='发货日')

    def __str__(self):
        return str(self.lot) + " - " + self.item.name

    class Meta:
        verbose_name = verbose_name_plural = '计划'


class TestResult(models.Model):
    plan = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    batch = models.IntegerField(null=True, blank=True, verbose_name='回数')
    mv = models.FloatField(null=True, blank=True, verbose_name='门尼值')
    scorch = models.FloatField(null=True, blank=True, verbose_name='焦烧')
    fmin = models.FloatField(null=True, blank=True, verbose_name='Fmin')
    fmax = models.FloatField(null=True, blank=True, verbose_name='Fmax')
    t10 = models.FloatField(null=True, blank=True, verbose_name='T10')
    t90 = models.FloatField(null=True, blank=True, verbose_name='T90')
    sg = models.FloatField(null=True, blank=True, verbose_name='SG')
    hs = models.FloatField(null=True, blank=True, verbose_name='HS')
    m_percent = models.FloatField(null=True, blank=True, verbose_name='M %')
    tb = models.FloatField(null=True, blank=True, verbose_name='TB')
    eb = models.FloatField(null=True, blank=True, verbose_name='EB')
    shipment_status = models.BooleanField(default=False, verbose_name='出货状态')

    def __str__(self):
        return str(self.plan)

    class Meta:
        verbose_name = verbose_name_plural = '检查明细'
