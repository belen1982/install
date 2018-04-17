# -*- coding: utf-8 -*-
{
    'name': "oca_install",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [

	#'account_export_csv',
	#'account_move_line_report_xls',
	'account_chart_update',
	'account_invoice_constraint_chronology',
	'account_invoice_currency',
	#'account_journal_always_check_date', 	
	'account_renumber',
	'account_due_list',
	'account_due_list_payment_mode',
	'account_banking_mandate',
	'account_banking_pain_base', 
	'account_banking_sepa_direct_debit', 
	'account_payment_partner',  
	#'attachment_preview', 
	#'attachments_to_filesystem', 
	'document_page', 
	#'document_url', 
	'account_balance_reporting_xlsx',  	
	'l10n_es_account_balance_report', 
	'l10n_es_account_bank_statement_import_n43', 
	'l10n_es_account_asset', 
	#'l10n_es_account_invoice_sequence', 
	#'l10n_es_aeat_mod111', 
	#'l10n_es_aeat_mod115', 
	#'l10n_es_aeat_mod130', 
	#'l10n_es_aeat_mod303', 
	#'l10n_es_aeat_mod349', 
	#'l10n_es_aeat_mod340_type0', 
	#'l10n_es_aeat_mod340', 
	#'l10n_es_aeat_mod347', 
	'l10n_es_aeat', 
	'l10n_es_partner_mercantil', 
	'l10n_es_partner', 
	#'l10n_es_pos',
	'l10n_es_toponyms', 
	'l10n_es', 
	#'l10n_es_account_fiscal_year_closing',
	'base_location', 
	'base_location_geonames_import', 
	'base_partner_sequence', 
	'report_xlsx', 	
	#'report_py3o', 
	'mass_editing', 
	'disable_odoo_online', 
	'web_export_view', 
	'account_invoice_refund_link', 

],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}