# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('case_number', models.CharField(max_length=200)),
                ('utid', models.CharField(max_length=200)),
                ('cse', models.CharField(max_length=200)),
                ('entry_date', models.DateField(default=django.utils.timezone.now)),
                ('target', models.CharField(max_length=200, blank=True, null=True)),
                ('system', models.CharField(max_length=200, blank=True, null=True)),
                ('subsystem', models.CharField(max_length=200, blank=True, null=True)),
                ('fault', models.CharField(max_length=200, blank=True, null=True)),
                ('symptoms', models.CharField(max_length=200, blank=True, null=True)),
                ('case_summary', models.TextField()),
                ('poa', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ltdrawdata',
            fields=[
                ('fiscal_year', models.IntegerField(primary_key=True, serialize=False, db_column='Fiscal year')),
                ('fiscal_quarter', models.IntegerField(db_column='Fiscal Quarter')),
                ('fiscal_month', models.IntegerField(db_column='Fiscal Month')),
                ('calendar_year_quarter', models.IntegerField(db_column='Calendar Year Quarter')),
                ('calendar_year_month', models.IntegerField(db_column='Calendar Year Month')),
                ('region', models.CharField(max_length=20, blank=True, null=True, db_column='Region')),
                ('case_number', models.IntegerField(db_column='Case Number')),
                ('case_title', models.CharField(max_length=200, db_column='Case Title')),
                ('customer_name', models.CharField(max_length=200, db_column='Customer Name')),
                ('business_unit', models.CharField(max_length=200, blank=True, null=True, db_column='Business Unit')),
                ('service_unit', models.CharField(max_length=200, blank=True, null=True, db_column='Service Unit')),
                ('customer_roll_up', models.CharField(max_length=200, blank=True, null=True, db_column='Customer Roll Up')),
                ('utid', models.CharField(max_length=200, db_column='UTID')),
                ('product_family', models.CharField(max_length=200, db_column='Product Family')),
                ('product_line', models.CharField(max_length=200, db_column='Product Line')),
                ('alias', models.CharField(max_length=200, blank=True, null=True, db_column='Alias')),
                ('model', models.CharField(max_length=200, db_column='Model')),
                ('case_owner', models.CharField(max_length=200, blank=True, null=True, db_column='Case Owner')),
                ('account_manager', models.CharField(max_length=200, blank=True, null=True, db_column='Account Manager')),
                ('life_stage', models.CharField(max_length=200, blank=True, null=True, db_column='Life Stage')),
                ('case_type', models.CharField(max_length=200, blank=True, null=True, db_column='Case Type')),
                ('down_hrs', models.CharField(max_length=200, blank=True, null=True, db_column='Down Hrs')),
                ('entitled_hours', models.CharField(max_length=200, blank=True, null=True, db_column='Entitled Hours')),
                ('ltd_reason', models.CharField(max_length=200, blank=True, null=True, db_column='LTD Reason')),
                ('override_reason', models.CharField(max_length=200, blank=True, null=True, db_column='Override Reason')),
                ('ltd_primary_reason_comments', models.CharField(max_length=200, blank=True, null=True, db_column='LTD Primary Reason Comments')),
                ('case_modified', models.CharField(max_length=200, blank=True, null=True, db_column='Case Modified')),
                ('cse_error_flag', models.CharField(max_length=200, blank=True, null=True, db_column='CSE Error Flag')),
                ('escalation_reason', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation Reason')),
                ('escalation_level_l1', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation Level L1')),
                ('escalation_l1_hrs', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation L1 Hrs')),
                ('escalation_level_l2', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation Level L2')),
                ('escalation_l2_hrs', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation L2 Hrs')),
                ('escalation_level_l3', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation Level L3')),
                ('escalation_l3_hrs', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation L3 Hrs')),
                ('escalation_level_l4', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation Level L4')),
                ('escalation_l4_hrs', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation L4 Hrs')),
            ],
            options={
                'db_table': 'LTDRawdata',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('post', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tblcasesummary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fab_code', models.IntegerField(db_column='Fab_Code')),
                ('case_id', models.IntegerField(db_column='Case ID')),
                ('case_description', models.CharField(max_length=200, db_column='Case Description')),
                ('case_type', models.CharField(max_length=200, blank=True, null=True, db_column='Case Type')),
                ('utid', models.IntegerField(db_column='UTID')),
                ('model_at_case_creation_time', models.CharField(max_length=200, db_column='Model at Case Creation Time')),
                ('case_creation_date', models.IntegerField(max_length=200, db_column='Case Creation Date')),
                ('case_classification_level_1', models.CharField(max_length=200, blank=True, null=True, db_column='Case Classification level 1')),
                ('case_classification_level_2', models.CharField(max_length=200, blank=True, null=True, db_column='Case Classification level 2')),
                ('tool_life_stg_per_case', models.CharField(max_length=200, blank=True, null=True, db_column='Tool Life Stg per Case')),
            ],
            options={
                'db_table': 'TBLCASESUMMARY',
            },
        ),
        migrations.CreateModel(
            name='Tblescalation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('entry_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=200, blank=True, db_column='Status')),
                ('plc_status', models.CharField(max_length=200, blank=True, null=True, db_column='PLC_Status')),
                ('poa_close', models.IntegerField(blank=True, null=True, db_column='POA-Close')),
                ('survey', models.IntegerField(blank=True, null=True, db_column='Survey')),
                ('esc_days', models.IntegerField(blank=True, null=True, db_column='ESC days')),
                ('case_id', models.IntegerField(db_column='Case ID')),
                ('product_family', models.CharField(max_length=200, db_column='Product_Family')),
                ('utid', models.IntegerField(db_column='UTID')),
                ('case_description', models.CharField(max_length=200, db_column='Case Description')),
                ('fab_code', models.IntegerField(db_column='Fab_Code')),
                ('max_escalation_level', models.CharField(max_length=200, blank=True, null=True, db_column='Max Escalation Level')),
                ('current_esc_level', models.CharField(max_length=200, blank=True, null=True, db_column='Current ESC Level')),
                ('l1', models.IntegerField(blank=True, null=True, db_column='L1')),
                ('l2', models.IntegerField(blank=True, null=True, db_column='L2')),
                ('l3', models.IntegerField(blank=True, null=True, db_column='L3')),
                ('l4', models.IntegerField(blank=True, null=True, db_column='L4')),
                ('escalation', models.IntegerField(blank=True, null=True, db_column='Escalation')),
                ('deescalation', models.IntegerField(blank=True, null=True, db_column='Deescalation')),
                ('tse_owner', models.CharField(max_length=200, db_column='TSE_Owner')),
                ('second_owner', models.CharField(max_length=200, blank=True, null=True, db_column='Second_Owner')),
                ('first_dispatch_tse', models.CharField(max_length=200, blank=True, null=True, db_column='First Dispatch_TSE')),
                ('first_dispatch_tse_date', models.IntegerField(blank=True, null=True, db_column='First Dispatch_TSE Date')),
                ('problem_statement', models.TextField(db_column='Problem statement')),
                ('symptoms', models.TextField(db_column='Symptoms')),
                ('fault_id', models.IntegerField(blank=True, null=True, db_column='Fault_ID')),
                ('system', models.CharField(max_length=200, db_column='System')),
                ('subsystem', models.CharField(max_length=200, db_column='SubSystem')),
                ('fault', models.CharField(max_length=200, db_column='Fault')),
                ('fix_rca', models.CharField(max_length=200, db_column='Fix_RCA')),
                ('poa', models.CharField(max_length=200, db_column='POA')),
                ('tse_analysis', models.TextField(db_column='TSE_Analysis')),
                ('plc_track', models.TextField(blank=True, null=True, db_column='PLC_Track')),
                ('passdown', models.TextField(db_column='Passdown')),
                ('rca_detail', models.TextField(db_column='RCA_Detail')),
                ('second_tse_dispatch_item', models.IntegerField(blank=True, null=True, db_column='Second TSE dispatch item')),
                ('second_tse', models.CharField(max_length=200, blank=True, null=True, db_column='Second_TSE')),
                ('second_escalation', models.IntegerField(blank=True, null=True, db_column='Second_Escalation')),
                ('second_deescalation', models.IntegerField(blank=True, null=True, db_column='Second_Deescalation')),
                ('third_tse_dispatch_item', models.IntegerField(blank=True, null=True, db_column='Third_TSE dispatch item')),
                ('third_tse', models.CharField(max_length=200, blank=True, null=True, db_column='Third_TSE')),
                ('image', models.IntegerField(blank=True, null=True, db_column='Image')),
                ('poa_1', models.TextField(db_column='POA-1')),
                ('poa_2', models.TextField(blank=True, null=True, db_column='POA-2')),
                ('poa_3', models.TextField(blank=True, null=True, db_column='POA-3')),
                ('poa_4', models.TextField(blank=True, null=True, db_column='POA-4')),
                ('poa_5', models.TextField(blank=True, null=True, db_column='POA-5')),
                ('seven_step', models.TextField(blank=True, null=True, db_column='Seven-step')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TBLEscalation',
            },
        ),
        migrations.CreateModel(
            name='Tblinstallbase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('prod_family', models.CharField(max_length=200, db_column='Prod Family')),
                ('prod_model', models.CharField(max_length=200, blank=True, null=True, db_column='Prod Model')),
                ('alias', models.CharField(max_length=200, blank=True, null=True, db_column='Alias')),
                ('install_start', models.IntegerField(blank=True, null=True, db_column='Install_Start')),
                ('warranty_end', models.IntegerField(blank=True, null=True, db_column='Warranty_End')),
                ('ship_date', models.IntegerField(blank=True, null=True, db_column='Ship_Date')),
                ('sales_order', models.CharField(max_length=200, blank=True, null=True, db_column='Sales Order')),
                ('tool_life_stage', models.CharField(max_length=200, db_column='Tool Life Stage')),
                ('utid', models.IntegerField(blank=True, null=True, db_column='UTID')),
                ('legacy_sn', models.CharField(max_length=200, blank=True, null=True, db_column='Legacy SN')),
                ('region_code', models.IntegerField(blank=True, null=True, db_column='Region_Code')),
                ('region', models.CharField(max_length=200, db_column='Region')),
                ('bu', models.CharField(max_length=200, blank=True, null=True, db_column='BU')),
                ('fab_code', models.IntegerField(db_column='FAB_Code')),
                ('fab', models.CharField(max_length=200, db_column='Fab')),
                ('svr_unit_code', models.IntegerField(db_column='SVR_Unit_Code')),
                ('svr_unit', models.CharField(max_length=200, db_column='SVR_Unit')),
            ],
            options={
                'db_table': 'TBLInstallBase',
            },
        ),
        migrations.CreateModel(
            name='Tblltdcategory',
            fields=[
                ('category', models.CharField(primary_key=True, max_length=200, blank=True, serialize=False, db_column='Category')),
            ],
            options={
                'db_table': 'TBLLTDCategory',
            },
        ),
        migrations.CreateModel(
            name='Tblltdreason',
            fields=[
                ('id', models.IntegerField(primary_key=True, blank=True, serialize=False, db_column='ID')),
                ('tier_1', models.CharField(max_length=200, blank=True, null=True, db_column='Tier 1')),
                ('tier_2', models.CharField(max_length=200, blank=True, null=True, db_column='Tier 2')),
                ('tier_3', models.CharField(max_length=200, blank=True, null=True, db_column='Tier 3')),
                ('definitions', models.TextField(blank=True, null=True, db_column='Definitions')),
            ],
            options={
                'db_table': 'TBLLTDReason',
            },
        ),
        migrations.CreateModel(
            name='Tblltdreport',
            fields=[
                ('fiscal_year', models.IntegerField(primary_key=True, serialize=False, db_column='Fiscal year')),
                ('fiscal_quarter', models.CharField(max_length=200, db_column='Fiscal Quarter')),
                ('fiscal_month', models.IntegerField(blank=True, null=True, db_column='Fiscal Month')),
                ('calendar_year_quarter', models.CharField(max_length=200, db_column='Calendar Year Quarter')),
                ('calendar_year_month', models.CharField(max_length=200, db_column='Calendar Year Month')),
                ('region', models.CharField(max_length=200, db_column='Region')),
                ('case_number', models.IntegerField(db_column='Case Number')),
                ('case_title', models.CharField(max_length=200, db_column='Case Title')),
                ('customer_name_fab_field', models.CharField(max_length=200, db_column='Customer Name (FAB)')),
                ('business_unit', models.CharField(max_length=200, blank=True, null=True, db_column='Business Unit')),
                ('service_unit', models.CharField(max_length=200, blank=True, null=True, db_column='Service Unit')),
                ('customer_roll_up', models.CharField(max_length=200, blank=True, null=True, db_column='Customer Roll Up')),
                ('utid', models.IntegerField(blank=True, null=True, db_column='UTID')),
                ('product_family', models.CharField(max_length=200, db_column='Product Family')),
                ('product_line', models.CharField(max_length=200, db_column='Product Line')),
                ('alias', models.CharField(max_length=200, blank=True, null=True, db_column='Alias')),
                ('model', models.CharField(max_length=200, blank=True, null=True, db_column='Model')),
                ('case_owner', models.CharField(max_length=200, db_column='Case Owner')),
                ('account_manager', models.CharField(max_length=200, blank=True, null=True, db_column='Account Manager')),
                ('life_stage', models.CharField(max_length=200, blank=True, null=True, db_column='Life Stage')),
                ('case_type', models.CharField(max_length=200, blank=True, null=True, db_column='Case Type')),
                ('down_hrs', models.CharField(max_length=200, db_column='Down Hrs')),
                ('entitled_hours', models.IntegerField(db_column='Entitled Hours')),
                ('ltd_reason', models.CharField(max_length=200, blank=True, null=True, db_column='LTD Reason')),
                ('override_reason', models.CharField(max_length=200, blank=True, null=True, db_column='Override Reason')),
                ('ltd_primary_reason_comments', models.TextField(db_column='LTD Primary Reason Comments')),
                ('case_modified', models.CharField(max_length=200, blank=True, null=True, db_column='Case Modified')),
                ('cse_error_flag', models.CharField(max_length=200, blank=True, null=True, db_column='CSE Error Flag')),
                ('escalation_reason', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation Reason')),
                ('escalation_level_l1', models.IntegerField(blank=True, null=True, db_column='Escalation Level L1')),
                ('escalation_l1_hrs', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation L1 Hrs')),
                ('escalation_level_l2', models.IntegerField(blank=True, null=True, db_column='Escalation Level L2')),
                ('escalation_l2_hrs', models.IntegerField(blank=True, null=True, db_column='Escalation L2 Hrs')),
                ('escalation_level_l3', models.IntegerField(blank=True, null=True, db_column='Escalation Level L3')),
                ('escalation_l3_hrs', models.CharField(max_length=200, blank=True, null=True, db_column='Escalation L3 Hrs')),
                ('escalation_level_l4', models.IntegerField(blank=True, null=True, db_column='Escalation Level L4')),
                ('escalation_l4_hrs', models.IntegerField(blank=True, null=True, db_column='Escalation L4 Hrs')),
                ('tier_1', models.CharField(max_length=200, blank=True, null=True, db_column='Tier 1')),
                ('tier_2', models.CharField(max_length=200, blank=True, null=True, db_column='Tier 2')),
                ('tier_3', models.CharField(max_length=200, blank=True, null=True, db_column='Tier 3')),
                ('category', models.CharField(max_length=200, blank=True, null=True, db_column='Category')),
                ('ar', models.IntegerField(blank=True, null=True, db_column='AR')),
                ('ltd_root_cause', models.TextField(blank=True, null=True, db_column='LTD Root cause')),
                ('action', models.TextField(blank=True, null=True, db_column='Action')),
                ('owner', models.TextField(blank=True, null=True, db_column='Owner')),
                ('due_date', models.CharField(max_length=200, blank=True, null=True, db_column='Due date')),
                ('complete_data', models.CharField(max_length=200, blank=True, null=True, db_column='Complete data')),
            ],
            options={
                'db_table': 'TBLLTDReport',
            },
        ),
        migrations.CreateModel(
            name='Tblpoa',
            fields=[
                ('poa_id', models.IntegerField(primary_key=True, serialize=False, db_column='POA_ID')),
                ('title', models.CharField(max_length=200, blank=True, null=True, db_column='Title')),
                ('document_link', models.TextField(blank=True, null=True, db_column='Document link')),
                ('fishbone', models.CharField(max_length=200, blank=True, null=True, db_column='Fishbone')),
                ('detail_poa', models.TextField(db_column='Detail_POA')),
                ('picture', models.CharField(max_length=200, blank=True, null=True, db_column='Picture')),
                ('bkm1', models.CharField(max_length=200, blank=True, null=True, db_column='BKM1')),
                ('bkm2', models.CharField(max_length=200, blank=True, null=True, db_column='BKM2')),
                ('bkm3', models.CharField(max_length=200, blank=True, null=True, db_column='BKM3')),
            ],
            options={
                'db_table': 'TBLPOA',
            },
        ),
        migrations.CreateModel(
            name='Tblsystem',
            fields=[
                ('id', models.IntegerField(primary_key=True, blank=True, serialize=False, db_column='ID')),
                ('system', models.CharField(max_length=200, blank=True, null=True, db_column='System')),
            ],
            options={
                'db_table': 'TBLSystem',
            },
        ),
        migrations.CreateModel(
            name='Tblsystemfaultfix',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, db_column='ID')),
                ('system', models.CharField(max_length=200, db_column='System')),
                ('subsystem', models.CharField(max_length=200, db_column='SubSystem')),
                ('fault', models.CharField(max_length=200, db_column='Fault')),
                ('poa', models.TextField(max_length=200, blank=True, null=True, db_column='POA')),
            ],
            options={
                'db_table': 'TBLSystemFaultFix',
            },
        ),
        migrations.CreateModel(
            name='Tblvrcafix',
            fields=[
                ('id', models.IntegerField(primary_key=True, blank=True, serialize=False, db_column='ID')),
                ('fix', models.CharField(max_length=200, blank=True, null=True, db_column='Fix')),
            ],
            options={
                'db_table': 'TBLVRCAFix',
            },
        ),
        migrations.CreateModel(
            name='Tblzinputesclevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, blank=True, serialize=False, db_column='ID')),
                ('esc_level', models.CharField(max_length=200, blank=True, null=True, db_column='ESC Level')),
            ],
            options={
                'db_table': 'TBLZinputESCLevel',
            },
        ),
        migrations.CreateModel(
            name='Tblzinputproductfamily',
            fields=[
                ('id', models.IntegerField(primary_key=True, blank=True, serialize=False, db_column='ID')),
                ('family', models.CharField(max_length=200, blank=True, null=True, db_column='Family')),
            ],
            options={
                'db_table': 'TBLZinputProductFamily',
            },
        ),
        migrations.CreateModel(
            name='Tblzinputstatus',
            fields=[
                ('status', models.CharField(primary_key=True, max_length=200, blank=True, serialize=False, db_column='Status')),
            ],
            options={
                'db_table': 'TBLZinputStatus',
            },
        ),
        migrations.CreateModel(
            name='Tblzinputtse',
            fields=[
                ('id', models.IntegerField(primary_key=True, blank=True, serialize=False, db_column='ID')),
                ('tse', models.CharField(max_length=200, blank=True, null=True, db_column='TSE')),
            ],
            options={
                'db_table': 'TBLZinputTSE',
            },
        ),
    ]
