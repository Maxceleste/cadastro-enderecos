# Generated by Django 4.0.3 on 2022-03-31 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_alter_endereco_bairro_alter_endereco_complemento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(error_messages={'max_lenght': 'O bairro é muito grande.', 'required': 'Por favor, insira o bairro'}, help_text='Ex: Funcionários', max_length=300, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(error_messages={'max_lenght': 'O CEP deve conter 8 números.', 'required': 'Por favor, insira o CEP'}, help_text='Ex: 36202072', max_length=8, validators=[django.core.validators.RegexValidator('^\\d\\d\\d\\d\\d\\d\\d\\d$', message='Insira um CEP válido')], verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(error_messages={'max_lenght': 'A cidade é muito grande.', 'required': 'Por favor, insira a cidade'}, help_text='Ex: Barbacena', max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(blank=True, error_messages={'max_lenght': 'O complemento é muito grande.'}, help_text='Ex: Casa 2', max_length=300, verbose_name='Complemento (Não obrigatório)'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='descricao',
            field=models.CharField(blank=True, error_messages={'max_lenght': 'O complemento é muito grande.'}, help_text='Ex: Casa amarela localizada no fundo', max_length=300, verbose_name='Descrição (Não obrigatório)'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='endereco',
            field=models.CharField(error_messages={'max_lenght': 'O endereço é muito grande.', 'required': 'Por favor, insira o endereço'}, help_text='Ex: José Josino de Oliveira', max_length=300, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.CharField(error_messages={'max_lenght': 'O número é muito grande.', 'required': 'Por favor, insira o número'}, help_text='Ex: 45', max_length=15, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='uf',
            field=models.CharField(error_messages={'max_lenght': 'Uma UF tem apenas 2 caracteres.', 'required': 'Por favor, insira o UF'}, help_text='Ex: MG', max_length=2, validators=[django.core.validators.RegexValidator('^[A-Z][A-Z]$', message='Insira uma UF válida')], verbose_name='UF'),
        ),
    ]