from django.contrib import admin

from products.models import About, AboutUsAdmin
from products.models import Product, Contact

admin.site.register([Product, Contact])


admin.site.register(About, AboutUsAdmin)
