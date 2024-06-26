# Generated by Django 4.2.8 on 2024-05-17 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.CharField(max_length=100)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('fin_prdt_cd', models.CharField(max_length=100)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('etc_note', models.TextField(blank=True, null=True)),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('join_way', models.CharField(max_length=100)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('contract_user', models.ManyToManyField(blank=True, related_name='saving_contract', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.CharField(max_length=100)),
                ('intr_rate_type_nm', models.CharField(max_length=2)),
                ('rsrv_type_nm', models.CharField(max_length=10)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('save_trm', models.CharField(max_length=3)),
                ('saving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_prdts.savingproducts')),
            ],
        ),
        migrations.CreateModel(
            name='LoanProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.CharField(max_length=100)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('fin_prdt_cd', models.CharField(max_length=100)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('crdt_prdt_type_nm', models.CharField(max_length=100)),
                ('join_way', models.CharField(max_length=100)),
                ('cd_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contract_user', models.ManyToManyField(blank=True, related_name='loan_contract', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoanOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.CharField(max_length=100)),
                ('crdt_lend_rate_type', models.CharField(max_length=10)),
                ('crdt_lend_rate_type_nm', models.CharField(max_length=20)),
                ('crdt_grad_1', models.FloatField(null=True)),
                ('crdt_grad_4', models.FloatField(null=True)),
                ('crdt_grad_5', models.FloatField(null=True)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_prdts.loanproducts')),
            ],
        ),
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.CharField(max_length=100)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('fin_prdt_cd', models.CharField(max_length=100)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('join_way', models.CharField(max_length=100)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('contract_user', models.ManyToManyField(blank=True, related_name='deposit_contract', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.CharField(max_length=100)),
                ('intr_rate_type_nm', models.CharField(max_length=2)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('save_trm', models.CharField(max_length=3)),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_prdts.depositproducts')),
            ],
        ),
    ]
