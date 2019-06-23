# encoding=utf8
# -*- coding: utf-8 -*- u
import frappe


def add_sales_customer_info(doc, method):
	if doc.voucher_type == "Sales Invoice":
		main_doc = frappe.get_doc(doc.voucher_type,doc.voucher_no)
		doc.customer_grn_number = main_doc.customer_grn_number
		doc.po_no = main_doc.po_no

@frappe.whitelist()
def get_customer_income_account(customer):
	customer_group = frappe.db.get_value("Customer", customer, "customer_group")
	return frappe.db.get_value("Customer Group", customer_group, "default_income_account")
	 
	
