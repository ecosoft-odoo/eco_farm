# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Groups
    group_eco_farm_manager = fields.Boolean(
        string='Manage Ecosoft FARM',
        implied_group='eco_farm.group_eco_farm_manager',
    )
    # OCA/l10n-thailand
    module_account_create_tax_cash_basis_entry_hook = fields.Boolean(
        string='TH - Cash Basis Hook',
        readonly=True,
    )
    module_l10n_th_partner = fields.Boolean(
        string='TH - Partner Fields',
        readonly=True,
    )
    module_l10n_th_account_report = fields.Boolean(
        string='TH - Accounting Reports',
    )
    module_l10n_th_vendor_tax_invoice = fields.Boolean(
        string='TH - Vendor Tax Invoice',
    )
    module_l10n_th_withholding_tax_cert = fields.Boolean(
        string='TH - Withholding Tax Certificate',
    )
    module_l10n_th_withholding_tax_cert_form = fields.Boolean(
        string='TH - Print Standard Withholding Tax Certificate ',
    )
    # OCA/account-financial-reporting
    module_account_financial_report = fields.Boolean(
        string='OCA Financial Reports',
    )
    # OCA/account-invoicing
    module_account_billing = fields.Boolean(
        string='Account Billing',
    )
    module_account_invoice_reimbursable = fields.Boolean(
        string='Invoice Remibursable',
    )
    module_account_menu_invoice_refund = fields.Boolean(
        string='Netting Invoice/Refund',
    )
    # OCA/acount-financial-tools
    module_account_type_menu = fields.Boolean(
        string='Account Menus',
        readonly=True,
    )
    module_account_asset_management = fields.Boolean(
        string='Asset Management',
    )
    module_account_document_reversal = fields.Boolean(
        string='Account Document Reversal',
    )
    module_account_fiscal_year = fields.Boolean(
        string='Fiscal Year',
        readonly=True,
    )
    module_account_invoice_refund_link = fields.Boolean(
        string='Invoice/Refund Linkage',
    )
    module_account_payment_intransit = fields.Boolean(
        string='Payment Intransit',
    )
    module_account_payment_intransit_deduction = fields.Boolean(
        string='Payment Intransit Multi Deduction',
    )
    module_account_payment_intransit_reversal = fields.Boolean(
        string='Payment Intransit Document Reversal',
    )
    # OCA/credit-control
    module_account_financial_risk = fields.Boolean(
        string='Account Financial Risk',
    )
    module_sale_financial_risk = fields.Boolean(
        string='Sales Financial Risk',
    )
    module_stock_financial_risk = fields.Boolean(
        string='Stock Financial Risk',
    )
    # OCA/hr
    module_hr_expense_advance_clearing = fields.Boolean(
        string='HR Expense Advance/Clearing',
    )
    module_hr_expense_invoice = fields.Boolean(
        string='HR Expense Invoicing',
    )
    module_hr_expense_payment_difference = fields.Boolean(
        string='HR Expense Payment Diff',
    )
    # OCA/manufacture
    module_stock_picking_product_kit_helper = fields.Boolean(
        string='Stock Product Kit Helper',
    )
    # OCA/partner-contact
    module_partner_fax = fields.Boolean(
        string='Add Partner Fax Number',
        readonly=True,
    )
    # OCA/product-attribute
    module_product_brand = fields.Boolean(
        string='Product Brands',
    )
    module_product_secondary_unit = fields.Boolean(
        string='Product Secondary Unit',
    )
    module_product_sequence = fields.Boolean(
        string='Product Sequence',
    )
    # OCA/purchase-workflow
    module_purchase_deposit = fields.Boolean(
        string='Purchase Deposit',
    )
    module_purchase_discount = fields.Boolean(
        string='Purchase Discount',
    )
    module_purchase_order_secondary_unit = fields.Boolean(
        string='Purchase Order Secondary Unit',
    )
    # OCA/reporting-engine
    module_report_xlsx = fields.Boolean(
        string='Report XLSX',
        readonly=True,
    )
    module_report_qweb_element_page_visibility = fields.Boolean(
        string='QWeb Element Page Visibility',
        readonly=True,
    )
    # OCA/sale-workflow
    module_sale_order_line_sequence = fields.Boolean(
        string='Sales Order Line Sequence',
    )
    module_sale_invoice_plan = fields.Boolean(
        string='Sales Invoice Plan',
    )
    # OCA/server-tools
    module_auto_backup = fields.Boolean(
        string='Auto Backup Database',
    )
    module_excel_import_export = fields.Boolean(
        string='Excel Import Export',
    )
    module_dbfilter_from_header = fields.Boolean(
        string='Filter DB From URL',
    )
    module_module_analysis = fields.Boolean(
        string='Module Analysis',
    )
    # OCA/server-ux
    module_date_range = fields.Boolean(
        string='Date Range',
        readonly=True,
    )
    module_mass_editing = fields.Boolean(
        string='Mass Editing',
    )
    # OCA/stock-logistics-warehouse
    module_stock_secondary_unit = fields.Boolean(
        string='Stock Secondary Unit',
    )
    # OCA/web
    module_web_m2x_options = fields.Boolean(
        string='M2X Options',
    )
