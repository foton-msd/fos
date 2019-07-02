# -*- coding: utf-8 -*-
{
  'name': "ONe System",
  'summary': "FOTON's ONe Dealers System",
  'description': """This application is customized to fit FOTON's (Automotive) Trading Business.
     """,
  'author': "Marlon Quidasol and Jun Salinga",
  'website': "https://one.fotonphils.net/",
  'category': 'Uncategorized',
  'version': '0.1',
  'depends': ['base', 'stock', 'purchase', 'mail', 'sale_management', 'account_invoicing', 'report_xlsx',
     'web_sheet_full_width', 'base_vat', 'backend_theme','web_tree_dynamic_colored_field','account_financial_report'],
  'data': [
    # Jun Salinga
    # odoo native (inherited) views
    'views/res_company_view.xml',
    'views/res_partner_view.xml',
    'views/product_template_view.xml',
    'views/product_attribute_value_view.xml',
    'views/purchase_order_view.xml',
    'views/sale_order_view.xml', 
    'views/service_order_lines_view.xml',
    'views/account_invoice_view.xml',
    'views/stock_picking_view.xml',
    'views/stock_move_line_view.xml',
    'views/fos_account_journal_view.xml',
    #'views/fos_account_account.xml',
    #'views/fos_inet_reports.xml',
    # FOS' groups, menus, wizards and views
    'views/fos_groups_view.xml',
    'views/fos_menu_view.xml', 
    'views/fos_purchase_order_line_import_view.xml',
    'views/fos_sales_parts_view.xml',
    'views/fos_sales_service_view.xml',
    'wizards/fos_cancel_ro_view.xml',  
    'views/fos_repair_order_view.xml',   
    'views/fos_sales_units_view.xml',
    'views/fos_fu_view.xml',        
    'wizards/fmpi_vqir_ack.xml',
    'wizards/fmpi_vqir_app.xml',
    'wizards/fmpi_vqir_dis.xml',
    'wizards/fmpi_vqir_pre.xml',
    'wizards/fmpi_vqir_dec.xml',
    'wizards/fmpi_vqir_pd.xml',
    'views/fmpi_fu_view.xml',   
    'views/fos_vqir_view.xml',
    'views/fmpi_vqir_view.xml',
    'views/one_local_names_view.xml',
    'views/one_dealers_view.xml',  
    'views/fos_payment_terms_view.xml',
    'views/fos_banks_view.xml',
    'views/fos_payment_modes_view.xml',
    'views/fos_account_payment_view.xml',
    'views/fos_serial_view.xml',
    'views/fos_acctg_reports.xml',
    'views/fos_account_internal_xfer_view.xml',
    'views/stock_backorder_confirmation_view.xml',
    'views/fos_service_technician_view.xml',
    #'views/fos_labor_codes_view.xml',
    # non-FOTON Servicing
    'views/nonf_menus_view.xml',
    'views/nonf_units_view.xml',
    'views/nonf_makers_view.xml',
    'views/nonf_ro_view.xml',
    'views/nonf_sales_service_view.xml',
    'views/fos_calc_view.xml',
    'views/fos_productivity_losses_view.xml',
    #'wizards/nonf_cancel_ro_view.xml',
    # Parts Online Order
    'views/fos_parts_po_view.xml',
    'views/fmpi_parts_so_view.xml',
    # reports
    'report/bir_report_sale_order_layout.xml',
    'report/fas_sales_parts_report.xml',
    'report/fas_sales_service_report.xml',
    'report/fos_report_invoice_document.xml',
    'report/fos_so_parts_report.xml',
    'report/fos_so_parts_quote_report.xml',
    'report/fos_so_units_report.xml',
    'report/fos_so_service_report.xml',
    'report/fos_so_service_report_quote.xml',
    'report/fos_repair_order_report.xml',
    'report/fos_nonf_repair_order_report.xml',
    'report/one_vqir_print_report.xml',
    'report/fmpi_vqir_print_report.xml',
    'report/fas_report_payment_voucher.xml',
    'report/fos_report_invoice_payment.xml',
    'report/fas_report_picking_operation_view.xml',
    'report/fas_report_delivery_document.xml',
    'report/fos_picking_list.xml',
    #'report/fas_report_payment_receipt_document.xml',
    'report/fas_report_purchase_order.xml',
    'report/parts_sales_report_1_view.xml',
    'report/fos_sale_report.xml',    
    'report/fos_vqir_report_1.xml',
    'report/fos_so_nonf_service_report.xml',
    'report/fos_sale_calculator_report.xml',
    'report/fos_nf_sales_parts_report.xml',
    'report/fos_nf_sales_service_report.xml',
    'security/ir.model.access.csv',
    ],
  'application': 'True',
}
