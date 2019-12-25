from django.db import models
from django.utils.translation import gettext_lazy as _


class App(models.Model):
    name = models.CharField(_('name'), max_length=200)
    slug = models.SlugField()
    icon = models.ImageField(_('icon'), upload_to='uploads/distribution/app',
            blank=True, null=True)
    background = models.ImageField(_('background image'),
            upload_to='uploads/distribution/app', blank=True, null=True)
    description = models.TextField(_('description'), blank=True, null=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/distribution/{}/'.format(self.slug)

    def get_android(self):
        return self.version_set.filter(platform='android').first()

    def get_android_url(self):
        v = self.get_android()

        if not v:
            return None
        elif v.url:
            return v.url
        elif v.package:
            return v.package.url
        else:
            return None

    def get_android_version_name(self):
        v = self.get_android()

        if not v:
            return 0

        return v.name
    get_android_version_name.short_description = _('android version name')


    def get_android_version_number(self):
        v = self.get_android()

        if not v:
            return 0

        return v.number

    def get_android_version_content(self):
        v = self.get_android()

        if not v:
            return None

        return v.content


    def get_ios(self):
        return self.version_set.filter(platform='ios').first()

    def get_ios_url(self):
        v = self.get_ios()

        if not v:
            return None

        return v.url

    def get_ios_version_name(self):
        v = self.get_ios()

        if not v:
            return 0

        return v.name

    get_ios_version_name.short_description = _('ios version name')


    def get_ios_version_number(self):
        v = self.get_ios()

        if not v:
            return 0

        return v.number

    def get_ios_version_content(self):
        v = self.get_ios()

        if not v:
            return None

        return v.content


class Version(models.Model):
    PLATFORM_CHOICES = (
            ('android', _('android')),
            ('ios', _('ios'))
            )
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    platform = models.CharField(_('platform'), max_length=20,
            default='android', choices=PLATFORM_CHOICES)
    name = models.CharField(_('version name'), max_length=50)
    number = models.SmallIntegerField(_('version number'), default=1)
    content = models.TextField(_('content'), blank=True, null=True)
    package = models.FileField(_('package'),
            upload_to='uploads/distribution/packages', blank=True, null=True)
    url = models.URLField(_('download url'), blank=True, null=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-number']
        verbose_name = _('app version')
        verbose_name_plural = _('app version')
