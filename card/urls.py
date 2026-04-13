from django.urls import path
from .views import card_view, download_vcf, admin_login, admin_edit, admin_logout

urlpatterns = [
    path('', card_view, name='home'),
    path('download/', download_vcf, name='download_vcf'),

    # ✅ ADD THESE
    path('admin/', admin_login, name='admin_login'),
    path('admin/edit/', admin_edit, name='admin_edit'),
    path('admin/logout/', admin_logout, name='admin_logout'),
]