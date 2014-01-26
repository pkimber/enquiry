from django.core.exceptions import ValidationError
from django.db import models

import reversion

from base.model_utils import TimeStampedModel


class Enquiry(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email_sent = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __unicode__(self):
        return unicode('{}: {}, {}'.format(
            self.name,
            self.email,
            self.phone,
        ))

    def clean(self):
        if self.phone or self.email:
            pass
        else:
            raise ValidationError(
                'You must provide an email address or phone number.'
            )

reversion.register(Enquiry)
