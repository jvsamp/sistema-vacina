import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0003_alter_agendamento_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cartao_sus',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Cartão SUS'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='endereco',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='paciente',
            name='responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dependentes', to='vacinas.paciente', verbose_name='Responsável'),
        ),
    ]
