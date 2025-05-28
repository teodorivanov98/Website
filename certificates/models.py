from django.db import models


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    issue_date = models.DateField()
    certificate_url = models.URLField(blank=True)
    file = models.FileField(upload_to='certificates/', blank=True)

    def __str__(self):
        return f"{self.title} - {self.issuer}"