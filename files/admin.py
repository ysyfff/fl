from django.contrib import admin
from files.models import Car, BackCar
from datetime import datetime


# class MyModelAdmin(admin.ModelAdmin):
#     def get_urls(self):
#         urls = super(MyModelAdmin, self).get_urls()
#         my_urls = patterns('',
#             (r'^my_view/$', self.admin_site.admin_view(self.my_view))
#             )
#         print urls, '9999999999999'
#         print my_urls+urls, '88888888888888888888'
#         return my_urls + urls

#     def my_view(self, request):
#         file_name = datetime.now().strftime('%Y%m%d%H%M%S')
#         if request.method=="POST":
#             picture = request.FILES['file']
#             p_name, format = picture.name.split('.')
#             picture.name=file_name+'.'+format
#             bcar = BackCar(picture=picture)
#             bcar.save()
#         else:
#             form = UploadFileForm()

#         return render_to_response(get_urls(),
#             locals(),
#             context_instance=RequestContext(request)
#             )


class MyModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.picture = request.FILES['picture']
        p_name, format = obj.picture.name.split('.')
        file_name = datetime.now().strftime('%Y%m%d%H%M%S')
        obj.picture.name=file_name+'.'+format
        obj.save()

admin.site.register(Car)
admin.site.register(BackCar, MyModelAdmin)