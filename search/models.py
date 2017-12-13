# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove 'managed = False' lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import TblinstallbaseIndex, BlogPostIndex

class Case(models.Model):
    # null=True means you can save to DB with this field being blank
    # blank=True means the Django form will not require this field
    user = models.ForeignKey(User)
    case_number = models.CharField(max_length=200)
    utid = models.CharField(max_length=200)
    cse = models.CharField(max_length=200)
    entry_date = models.DateField(default=timezone.now)
    target = models.CharField(max_length=200, blank=True, null=True)
    system = models.CharField(max_length=200, blank=True, null=True)
    subsystem = models.CharField(max_length=200, blank=True, null=True)
    fault = models.CharField(max_length=200, blank=True, null=True)
    symptoms = models.CharField(max_length=200, blank=True, null=True)
    case_summary = models.TextField()
    poa = models.TextField()

class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)


class Ltdrawdata(models.Model):
    fiscal_year = models.IntegerField(db_column='Fiscal year', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fiscal_quarter = models.IntegerField(db_column='Fiscal Quarter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fiscal_month = models.IntegerField(db_column='Fiscal Month')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    calendar_year_quarter = models.IntegerField(db_column='Calendar Year Quarter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    calendar_year_month = models.IntegerField(db_column='Calendar Year Month')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    region = models.CharField(db_column='Region', max_length=20, blank=True, null=True)  # Field name made lowercase.
    case_number = models.IntegerField(db_column='Case Number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_title = models.CharField(db_column='Case Title', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_name = models.CharField(db_column='Customer Name', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    business_unit = models.CharField(db_column='Business Unit', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_unit = models.CharField(db_column='Service Unit', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_roll_up = models.CharField(db_column='Customer Roll Up', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utid = models.CharField(db_column='UTID', max_length=200)  # Field name made lowercase.
    product_family = models.CharField(db_column='Product Family', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    product_line = models.CharField(db_column='Product Line', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alias = models.CharField(db_column='Alias', max_length=200, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=200)  # Field name made lowercase.
    case_owner = models.CharField(db_column='Case Owner', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    account_manager = models.CharField(db_column='Account Manager', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    life_stage = models.CharField(db_column='Life Stage', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_type = models.CharField(db_column='Case Type', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    down_hrs = models.CharField(db_column='Down Hrs', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    entitled_hours = models.CharField(db_column='Entitled Hours', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ltd_reason = models.CharField(db_column='LTD Reason', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    override_reason = models.CharField(db_column='Override Reason', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ltd_primary_reason_comments = models.CharField(db_column='LTD Primary Reason Comments', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_modified = models.CharField(db_column='Case Modified', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cse_error_flag = models.CharField(db_column='CSE Error Flag', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_reason = models.CharField(db_column='Escalation Reason', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_level_l1 = models.CharField(db_column='Escalation Level L1', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_l1_hrs = models.CharField(db_column='Escalation L1 Hrs', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_level_l2 = models.CharField(db_column='Escalation Level L2', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_l2_hrs = models.CharField(db_column='Escalation L2 Hrs', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_level_l3 = models.CharField(db_column='Escalation Level L3', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_l3_hrs = models.CharField(db_column='Escalation L3 Hrs', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_level_l4 = models.CharField(db_column='Escalation Level L4', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_l4_hrs = models.CharField(db_column='Escalation L4 Hrs', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:

        db_table = 'LTDRawdata'


class Tblcasesummary(models.Model):
    fab_code = models.IntegerField(db_column='Fab_Code')  # Field name made lowercase.
    case_id = models.IntegerField(db_column='Case ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_description = models.CharField(db_column='Case Description', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_type = models.CharField(db_column='Case Type', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utid = models.IntegerField(db_column='UTID')  # Field name made lowercase.
    model_at_case_creation_time = models.CharField(db_column='Model at Case Creation Time', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_creation_date = models.IntegerField(db_column='Case Creation Date', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_classification_level_1 = models.CharField(db_column='Case Classification level 1', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_classification_level_2 = models.CharField(db_column='Case Classification level 2', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tool_life_stg_per_case = models.CharField(db_column='Tool Life Stg per Case', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:

        db_table = 'TBLCASESUMMARY'


class Tblescalation(models.Model):
    user = models.ForeignKey(User)
    entry_date = models.DateField(default=timezone.now)
    status = models.CharField(db_column='Status', max_length=200, blank=True)  # Field name made lowercase.
    plc_status = models.CharField(db_column='PLC_Status', max_length=200, blank=True, null=True)  # Field name made lowercase.
    poa_close = models.IntegerField(db_column='POA-Close', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    survey = models.IntegerField(db_column='Survey', blank=True, null=True)  # Field name made lowercase.
    esc_days = models.IntegerField(db_column='ESC days', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_id = models.IntegerField(db_column='Case ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    product_family = models.CharField(db_column='Product_Family', max_length=200)  # Field name made lowercase.
    utid = models.IntegerField(db_column='UTID')  # Field name made lowercase.
    case_description = models.CharField(db_column='Case Description', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fab_code = models.IntegerField(db_column='Fab_Code')  # Field name made lowercase.
    max_escalation_level = models.CharField(db_column='Max Escalation Level', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_esc_level = models.CharField(db_column='Current ESC Level', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l1 = models.IntegerField(db_column='L1', blank=True, null=True)  # Field name made lowercase.
    l2 = models.IntegerField(db_column='L2', blank=True, null=True)  # Field name made lowercase.
    l3 = models.IntegerField(db_column='L3', blank=True, null=True)  # Field name made lowercase.
    l4 = models.IntegerField(db_column='L4', blank=True, null=True)  # Field name made lowercase.
    escalation = models.IntegerField(db_column='Escalation', blank=True, null=True)  # Field name made lowercase.
    deescalation = models.IntegerField(db_column='Deescalation', blank=True, null=True)  # Field name made lowercase.
    tse_owner = models.CharField(db_column='TSE_Owner', max_length=200)  # Field name made lowercase.
    second_owner = models.CharField(db_column='Second_Owner', max_length=200, blank=True, null=True)  # Field name made lowercase.
    first_dispatch_tse = models.CharField(db_column='First Dispatch_TSE', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_dispatch_tse_date = models.IntegerField(db_column='First Dispatch_TSE Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    problem_statement = models.TextField(db_column='Problem statement')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    symptoms = models.TextField(db_column='Symptoms')  # Field name made lowercase.
    fault_id = models.IntegerField(db_column='Fault_ID', blank=True, null=True)  # Field name made lowercase.
    system = models.CharField(db_column='System', max_length=200)  # Field name made lowercase.
    subsystem = models.CharField(db_column='SubSystem', max_length=200)  # Field name made lowercase.
    fault = models.CharField(db_column='Fault', max_length=200)  # Field name made lowercase.
    fix_rca = models.CharField(db_column='Fix_RCA', max_length=200)  # Field name made lowercase.
    poa = models.CharField(db_column='POA', max_length=200)  # Field name made lowercase.
    tse_analysis = models.TextField(db_column='TSE_Analysis')  # Field name made lowercase.
    plc_track = models.TextField(db_column='PLC_Track', blank=True, null=True)  # Field name made lowercase.
    passdown = models.TextField(db_column='Passdown')  # Field name made lowercase.
    rca_detail = models.TextField(db_column='RCA_Detail')  # Field name made lowercase.
    second_tse_dispatch_item = models.IntegerField(db_column='Second TSE dispatch item', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    second_tse = models.CharField(db_column='Second_TSE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    second_escalation = models.IntegerField(db_column='Second_Escalation', blank=True, null=True)  # Field name made lowercase.
    second_deescalation = models.IntegerField(db_column='Second_Deescalation', blank=True, null=True)  # Field name made lowercase.
    third_tse_dispatch_item = models.IntegerField(db_column='Third_TSE dispatch item', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    third_tse = models.CharField(db_column='Third_TSE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    image = models.IntegerField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    poa_1 = models.TextField(db_column='POA-1')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    poa_2 = models.TextField(db_column='POA-2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    poa_3 = models.TextField(db_column='POA-3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    poa_4 = models.TextField(db_column='POA-4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    poa_5 = models.TextField(db_column='POA-5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seven_step = models.TextField(db_column='Seven-step', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:

        db_table = 'TBLEscalation'


class Tblinstallbase(models.Model):
    prod_family = models.CharField(db_column='Prod Family', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prod_model = models.CharField(db_column='Prod Model', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alias = models.CharField(db_column='Alias', max_length=200, blank=True, null=True)  # Field name made lowercase.
    install_start = models.IntegerField(db_column='Install_Start', blank=True, null=True)  # Field name made lowercase.
    warranty_end = models.IntegerField(db_column='Warranty_End', blank=True, null=True)  # Field name made lowercase.
    ship_date = models.IntegerField(db_column='Ship_Date', blank=True, null=True)  # Field name made lowercase.
    sales_order = models.CharField(db_column='Sales Order', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tool_life_stage = models.CharField(db_column='Tool Life Stage', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utid = models.IntegerField(db_column='UTID', blank=True, null=True)  # Field name made lowercase.
    legacy_sn = models.CharField(db_column='Legacy SN', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    region_code = models.IntegerField(db_column='Region_Code', blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=200)  # Field name made lowercase.
    bu = models.CharField(db_column='BU', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fab_code = models.IntegerField(db_column='FAB_Code')  # Field name made lowercase.
    fab = models.CharField(db_column='Fab', max_length=200)  # Field name made lowercase.
    svr_unit_code = models.IntegerField(db_column='SVR_Unit_Code')  # Field name made lowercase.
    svr_unit = models.CharField(db_column='SVR_Unit', max_length=200)  # Field name made lowercase.

    class Meta:

        db_table = 'TBLInstallBase'

    def indexing(self):
        obj = TblinstallbaseIndex(
            meta={'id': self.id},
            prod_family = self.prod_family,
            prod_model = self.prod_model,
            alias = self.alias,
            install_start = self.install_start,
            warranty_end = self.warranty_end,
            ship_date = self.ship_date,
            sales_order = self.sales_order,
            tool_life_stage = self.tool_life_stage,
            utid = self.utid,
            legacy_sn = self.legacy_sn,
            region_code = self.region_code,
            region = self.region,
            bu = self.bu,
            fab_code = self.fab_code,
            fab = self.fab,
            svr_unit_code = self.svr_unit_code,
            svr_unit = self.svr_unit
        )
        obj.save()
        return obj.to_dict(include_meta=True)

class Tblltdcategory(models.Model):
    category = models.CharField(db_column='Category', max_length=200, blank=True, primary_key=True)  # Field name made lowercase.

    class Meta:

        db_table = 'TBLLTDCategory'


class Tblltdreason(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    tier_1 = models.CharField(db_column='Tier 1', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tier_2 = models.CharField(db_column='Tier 2', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tier_3 = models.CharField(db_column='Tier 3', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    definitions = models.TextField(db_column='Definitions', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'TBLLTDReason'


class Tblltdreport(models.Model):
    fiscal_year = models.IntegerField(db_column='Fiscal year', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fiscal_quarter = models.CharField(db_column='Fiscal Quarter', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fiscal_month = models.IntegerField(db_column='Fiscal Month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    calendar_year_quarter = models.CharField(db_column='Calendar Year Quarter', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    calendar_year_month = models.CharField(db_column='Calendar Year Month', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    region = models.CharField(db_column='Region', max_length=200)  # Field name made lowercase.
    case_number = models.IntegerField(db_column='Case Number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_title = models.CharField(db_column='Case Title', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_name_fab_field = models.CharField(db_column='Customer Name (FAB)', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    business_unit = models.CharField(db_column='Business Unit', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_unit = models.CharField(db_column='Service Unit', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_roll_up = models.CharField(db_column='Customer Roll Up', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utid = models.IntegerField(db_column='UTID', blank=True, null=True)  # Field name made lowercase.
    product_family = models.CharField(db_column='Product Family', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    product_line = models.CharField(db_column='Product Line', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alias = models.CharField(db_column='Alias', max_length=200, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=200, blank=True, null=True)  # Field name made lowercase.
    case_owner = models.CharField(db_column='Case Owner', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    account_manager = models.CharField(db_column='Account Manager', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    life_stage = models.CharField(db_column='Life Stage', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_type = models.CharField(db_column='Case Type', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    down_hrs = models.CharField(db_column='Down Hrs', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    entitled_hours = models.IntegerField(db_column='Entitled Hours')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ltd_reason = models.CharField(db_column='LTD Reason', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    override_reason = models.CharField(db_column='Override Reason', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ltd_primary_reason_comments = models.TextField(db_column='LTD Primary Reason Comments')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    case_modified = models.CharField(db_column='Case Modified', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cse_error_flag = models.CharField(db_column='CSE Error Flag', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_reason = models.CharField(db_column='Escalation Reason', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_level_l1 = models.IntegerField(db_column='Escalation Level L1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_l1_hrs = models.CharField(db_column='Escalation L1 Hrs', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_level_l2 = models.IntegerField(db_column='Escalation Level L2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_l2_hrs = models.IntegerField(db_column='Escalation L2 Hrs', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_level_l3 = models.IntegerField(db_column='Escalation Level L3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_l3_hrs = models.CharField(db_column='Escalation L3 Hrs', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_level_l4 = models.IntegerField(db_column='Escalation Level L4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalation_l4_hrs = models.IntegerField(db_column='Escalation L4 Hrs', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tier_1 = models.CharField(db_column='Tier 1', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tier_2 = models.CharField(db_column='Tier 2', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tier_3 = models.CharField(db_column='Tier 3', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    category = models.CharField(db_column='Category', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ar = models.IntegerField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    ltd_root_cause = models.TextField(db_column='LTD Root cause', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action = models.TextField(db_column='Action', blank=True, null=True)  # Field name made lowercase.
    owner = models.TextField(db_column='Owner', blank=True, null=True)  # Field name made lowercase.
    due_date = models.CharField(db_column='Due date', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    complete_data = models.CharField(db_column='Complete data', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:

        db_table = 'TBLLTDReport'


class Tblpoa(models.Model):
    poa_id = models.IntegerField(db_column='POA_ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)  # Field name made lowercase.
    document_link = models.TextField(db_column='Document link', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fishbone = models.CharField(db_column='Fishbone', max_length=200, blank=True, null=True)  # Field name made lowercase.
    detail_poa = models.TextField(db_column='Detail_POA')  # Field name made lowercase.
    picture = models.CharField(db_column='Picture', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bkm1 = models.CharField(db_column='BKM1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bkm2 = models.CharField(db_column='BKM2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bkm3 = models.CharField(db_column='BKM3', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'TBLPOA'


class Tblsystem(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    system = models.CharField(db_column='System', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'TBLSystem'


class Tblsystemfaultfix(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    system = models.CharField(db_column='System', max_length=200)  # Field name made lowercase.
    subsystem = models.CharField(db_column='SubSystem', max_length=200)  # Field name made lowercase.
    fault = models.CharField(db_column='Fault', max_length=200)  # Field name made lowercase.
    poa = models.TextField(db_column='POA', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'TBLSystemFaultFix'


class Tblvrcafix(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    fix = models.CharField(db_column='Fix', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'TBLVRCAFix'


class Tblzinputesclevel(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    esc_level = models.CharField(db_column='ESC Level', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:

        db_table = 'TBLZinputESCLevel'


class Tblzinputproductfamily(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'TBLZinputProductFamily'


class Tblzinputstatus(models.Model):
    status = models.CharField(db_column='Status', max_length=200, blank=True, primary_key=True)  # Field name made lowercase.

    class Meta:

        db_table = 'TBLZinputStatus'


class Tblzinputtse(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    tse = models.CharField(db_column='TSE', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'TBLZinputTSE'

class BlogPost(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField(max_length = 100)

    class Meta:
        db_table = 'BlogPost'

    def indexing(self):
        obj = BlogPostIndex(
            meta = {'id':self.id},
            title = self.title,
            text = self.text
        )
        obj.save()
        return obj.to_dict(include_meta=True)
