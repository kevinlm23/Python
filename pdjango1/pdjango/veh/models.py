from django.db import models

# Create your models here.

class vhc_brand (models.Model):
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

class vhc_bodywork (models.Model):
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

class vhc_type (models.Model):
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

class vhc_model (models.Model):
    name = models.CharField(max_length=45)
    is_active = models.IntegerField(max_length=45)
    description = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)
    vhc_type = models.ForeignKey(vhc_type)
    vhc_brand = models.ForeignKey(vhc_brand)
    vhc_bodywork = models.ForeignKey(vhc_bodywork)

    def __unicode__(self):
        return self.name

class vhc_line (models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=60)
    state_code = models.CharField(max_length=6)
    is_active = models.IntegerField(max_length=45)
    description = models.CharField(max_length=255)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)
    vhc_model_id = models.ForeignKey(vhc_model)
    
    def __unicode__(self):
        return self.name
    
class vhc_service (models.Model):
    name = models.CharField(max_length=45)
    is_active = models.IntegerField(max_length=45)
    description = models.CharField(max_length=255)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class vhc_color (models.Model):
    name = models.CharField(max_length=90)
    is_active = models.IntegerField(max_length=20)
    description = models.CharField(max_length=255)
    hex_code = models.CharField(max_length=6)
    parent_id = models.IntegerField(max_length=20)
    manufacturer_code = models.CharField(max_length=45)
    vhc_model_id = models.ForeignKey(vhc_model)
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
    imp_mnf_date = models.DateTimeField(auto_now_add=True)
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45)
    create_by = models.CharField(max_length=45)
    update_by = models.CharField(max_length=45)
    vhc_service_id = models.ForeignKey(vhc_service)
    vhc_color_id = models.ForeignKey(vhc_color)
    vhc_line_id = models.ForeignKey(vhc_line)
    carplate_city = models.CharField(max_length=30)
    imp_mnt_city = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.motor_code
















    
