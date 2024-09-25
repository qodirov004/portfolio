from django.contrib import admin
from .models import SkewStarP, SkewStarh1, AboutMe, PersonalInfo, Skill, Service, Work, Partfolio, PortfolioTitle, BlogTitle, Blog, Contact, BlogSingle


# admin.site.register(SkewStarh1)
admin.site.register(SkewStarP)
admin.site.register(PersonalInfo)
admin.site.register(Skill)
admin.site.register(AboutMe)
admin.site.register(Service)
admin.site.register(Work)
admin.site.register(Partfolio)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(BlogSingle)




@admin.register(SkewStarh1)
class H1(admin.ModelAdmin):
    list_display = ('h1',)

    def has_add_permission(self, request):
        if SkewStarh1.objects.count() >= 1:
            return False
        else:
            return True

@admin.register(PortfolioTitle)
class H1(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

    def has_add_permission(self, request):
        if PortfolioTitle.objects.count() >= 1:
            return False
        else:
            return True
        
@admin.register(BlogTitle)
class H1(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

    def has_add_permission(self, request):
        if BlogTitle.objects.count() >= 1:
            return False
        else:
            return True