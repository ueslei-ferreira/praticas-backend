from django.db import models

class Urls(models.Model):
    id = models.AutoField(primary_key=True)
    url_longo = models.CharField(unique=True, max_length=1000, blank=True, null=True)
    url_curto = models.CharField(unique=True, max_length=255, blank=True, null=True)

    def __str__(self):
        return self.url_curto or self.url_longo

    class Meta:
        managed = False
        db_table = 'urls'