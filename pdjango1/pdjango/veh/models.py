from django.db import models
from django.utils import timezone
# Create your models here.

class Vhc_brand (models.Model):
    name = models.CharField(max_length=45)
    is_active = models.IntegerField(max_length=45)
    description = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class Vhc_bodywork (models.Model):
    name = models.CharField(max_length=60)
    is_active = models.IntegerField(max_length=45)
    description = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class Vhc_type (models.Model):
    name = models.CharField(max_length=45)
    is_active = models.IntegerField(max_length=45)
    description = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class Vhc_model (models.Model):
    name = models.CharField(max_length=45)
    is_active = models.IntegerField(max_length=45)
    description = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)
    vhc_type = models.ForeignKey(Vhc_type)
    vhc_brand = models.ForeignKey(Vhc_brand)
    vhc_bodywork = models.ForeignKey(Vhc_bodywork)

    def __unicode__(self):
        return self.name

class Vhc_line (models.Model):
    name = models.CharField(max_length=60)
    state_code = models.CharField(max_length=6)
    is_active = models.IntegerField(max_length=45)
    description = models.CharField(max_length=255)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)
    vhc_model = models.ForeignKey(Vhc_model)
    
    def __unicode__(self):
        return self.name
    
class Vhc_service (models.Model):
    name = models.CharField(max_length=45)
    is_active = models.IntegerField(max_length=45)
    description = models.CharField(max_length=255)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class Vhc_color (models.Model):
    name = models.CharField(max_length=90)
    is_active = models.IntegerField(max_length=20)
    description = models.CharField(max_length=255)
    hex_code = models.CharField(max_length=6)
    parent_id = models.IntegerField(max_length=20)
    manufacturer_code = models.CharField(max_length=45)
    vhc_model = models.ForeignKey(Vhc_model)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

   
class Vehicle (models.Model):
    model_year = models.IntegerField(max_length=5)
    motor_code = models.CharField(max_length=30)
    serial_code = models.CharField(max_length=30)
    carplate_code = models.CharField(max_length=10)
    imp_mnf_num = models.CharField(max_length=45)
    imp_mnf_date = models.DateTimeField('Fecha')
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)
    carplate_city = models.CharField(max_length=30)
    imp_mnt_city = models.CharField(max_length=30)
    vhc_service = models.ForeignKey(Vhc_service)
    vhc_color = models.ForeignKey(Vhc_color)
    vhc_line = models.ForeignKey(Vhc_line)
        
    def __unicode__(self):
        return self.motor_code
















    
