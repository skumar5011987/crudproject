from django.db import models

ROLE=(
    ('CEO','Chief Executive Officer'),
    ('CMO','Chief Marketing Officer'),
    ('CTO','Chief Marketing Officer'),
    ('OM','Operations Manager'),
    ('PM','Product Manager'),
    ('CSSM','Customer Service & Support Manager'),
    ('BDM','Business Development Manager'),
    ('BA','Business analyst'),
    ('NE','Network engineer'),
    ('SE','Software engineer'),
    ('SSE','Senior Software engineer')
)



# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100)

    