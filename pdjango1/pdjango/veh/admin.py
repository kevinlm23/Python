from django.contrib import admin

from veh.models import Vehicle
from veh.models import Vhc_color
from veh.models import Vhc_service
from veh.models import Vhc_model
from veh.models import Vhc_bodywork
from veh.models import Vhc_type
from veh.models import Vhc_brand
from veh.models import Vhc_line

admin.site.register(Vehicle)
admin.site.register(Vhc_color)
admin.site.register(Vhc_service)
admin.site.register(Vhc_model)
admin.site.register(Vhc_bodywork)
admin.site.register(Vhc_type)
admin.site.register(Vhc_brand)
admin.site.register(Vhc_line)
