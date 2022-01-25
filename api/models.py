from django.db import models


class Deviation(models.Model):
    region = models.CharField('Нефтебаза', max_length=200,)
    objectid = models.CharField('Резервуар', max_length=200,)
    productid = models.PositiveIntegerField('Продукт', unique=True,)
    shiftnumber = models.CharField('Номер смены', max_length=200,)
    shiftbegt = models.DateTimeField(
        'Дата и время начала рабочей смены',
        auto_now_add=True
        )
    shiftendt = models.DateTimeField(
        'Дата и время окончания рабочей смены',
        auto_now_add=True
        )
    attrval_start_weight = models.PositiveIntegerField(
        'Масса на начало смены',
        )
    attrval_end_weight = models.PositiveIntegerField(
        'Масса на конец смены',
        )
    acceptance_sum = models.PositiveIntegerField(
        'Суммарная масса принятого нефтепродукта',
        )
    shipment_sum = models.PositiveIntegerField(
        'Суммарная масса отгруженного нефтепродукта',
        )
    version = models.PositiveSmallIntegerField(
        'Версия пакета выгрузки по рабочей смене',
        )
    index = models.PositiveSmallIntegerField('Индекс',)

    class Meta:
        verbose_name = 'Отклонение'
        verbose_name_plural = 'Отклонения'
