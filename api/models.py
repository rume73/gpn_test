from django.db import models

from .validators import validate_positive


class Deviation(models.Model):
    region = models.CharField('Нефтебаза', max_length=200,)
    objectid = models.CharField('Резервуар', max_length=200,)
    productid = models.PositiveIntegerField(
        'Продукт',
        validators=[validate_positive],
        )
    shiftnumber = models.CharField('Номер смены', max_length=200,)
    shiftbegt = models.DateTimeField('Дата и время начала рабочей смены',)
    shiftendt = models.DateTimeField('Дата и время окончания рабочей смены',)
    attrval_start_weight = models.PositiveIntegerField(
        'Масса на начало смены',
        validators=[validate_positive],
        )
    attrval_end_weight = models.PositiveIntegerField(
        'Масса на конец смены',
        validators=[validate_positive],
        )
    acceptance_sum = models.PositiveIntegerField(
        'Суммарная масса принятого нефтепродукта',
        validators=[validate_positive],
        )
    shipment_sum = models.PositiveIntegerField(
        'Суммарная масса отгруженного нефтепродукта',
        validators=[validate_positive],
        )
    version = models.PositiveSmallIntegerField(
        'Версия пакета выгрузки по рабочей смене',
        validators=[validate_positive],
        )
    index = models.PositiveSmallIntegerField(
        'Индекс',
        validators=[validate_positive],
        unique=True
        )

    class Meta:
        verbose_name = 'Отклонение'
        verbose_name_plural = 'Отклонения'
