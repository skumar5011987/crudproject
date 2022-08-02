# Generated by Django 4.0.6 on 2022-07-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_alter_employee_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('CEO', 'Chief Executive Officer'), ('CMO', 'Chief Marketing Officer'), ('CTO', 'Chief Marketing Officer'), ('OM', 'Operations Manager'), ('PM', 'Product Manager'), ('CSSM', 'Customer Service & Support Manager'), ('BDM', 'Business Development Manager'), ('BA', 'Business analyst'), ('NE', 'Network engineer'), ('SE', 'Software engineer'), ('SSE', 'Senior Software engineer')], default='SE', max_length=50),
        ),
    ]
