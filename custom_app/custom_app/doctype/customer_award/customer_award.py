# -*- coding: utf-8 -*-
# Copyright (c) 2019, anas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import today

class CustomerAward(Document):
	def get_customers_info(self):
		conditions = self.prepare_conditions()
		a= """
			select c.name as customer,SUM(si.grand_total) as amount,c.customer_group as customer_group
			from `tabSales Invoice`
			as si join `tabCustomer` as c  
			on si.customer=c.name
			where
				c.disabled =0 and si.docstatus =1 {conditions}
			group by c.name
		""".format( conditions=conditions)
		customers = frappe.db.sql(a, as_dict=True)
		
		if customers:
			self.customer_award_detail=[]
			for c in customers:
				if c.amount and c.customer:
					c_child = self.append('customer_award_detail')
					c_child.customer = c.customer
					c_child.amount = c.amount
					c_child.discount_amount = self.get_range(c.amount,c.customer,c.customer_group)
				else:
					frappe.msgprint(_("No Sales Invoice Match your filtering"))
			self.calc_sales_invoice()
			
		
		return customers
	
	def get_range (self,amount,customer,customer_group):
		range_list = frappe.get_list("Customer Award Range Detail", fields=["*"])
		if range_list :
			percentage = 0 
			for data in range_list:
				if data["customer"]	:
					if data["customer"] == customer and  data["min"]<=amount  and data["max"]>=amount:
						return data["percentage"]
				elif data["customer_group"]	:
					if data["customer_group"] == customer_group and  data["min"]<=amount  and data["max"]>=amount:
						return data["percentage"]
				elif data["customer_group"] != customer_group and data["customer"] != customer:
					percentage = data["percentage"]
	
		return percentage		
	
	
	def calc_sales_invoice (self):
		total_amount =0.00
		total_discount=0.00
		for row in self.get('customer_award_detail'):
			if row.amount and row.customer:
				if row.discount_amount > 100:
						frappe.throw(_("Bad Value Discount should not be more than 100"))
				total_amount+= row.amount
				row.discount_value = row.amount*(row.discount_amount) /100.00
				total_discount+=row.discount_value
		self.total_amount= total_amount
		self.total_discount= total_discount
		return self.total_amount,self.total_discount
			
	def prepare_conditions(self):
		conditions = [""]
		if self.from_date and self.to_date:
			conditions.append(""" si.posting_date  BETWEEN '{from_date}' AND '{to_date}'"""
				.format(from_date=self.from_date, to_date=self.to_date)
				)		
		
		if self.customer :
			conditions.append("""c.name = '{customer}'""".format
			(customer=self.customer))

		if self.company :
			conditions.append("""si.company = '{company}'""".format
			(company=self.company))
		
		if self.customer_group :
			lft, rgt = frappe.db.get_value("Customer Group",
					self.customer_group, ["lft", "rgt"])
			conditions.append("""c.name in (select name from tabCustomer
				where exists(select name from `tabCustomer Group` where lft >= {0} and rgt <= {1}
				and name=tabCustomer.customer_group))""".format(lft, rgt))
		
		conditions.append("""si.name not in (select sales_invoice from `tabCustomer Award Log`)""")
		
		return " and ".join(conditions)
	
	def make_journal_entry(self):
		if not self.default_receivable_account or not self.expense_account :
			frappe.throw(_("Please correct accounts"))
		if not self.company:
			frappe.throw(_("Please select Company"))
		
		precision = frappe.get_precision("Journal Entry Account", "debit_in_account_currency")
		je = frappe.new_doc("Journal Entry")
		je.posting_date = today()
		je.company = self.company
		je.remark = "Rebate against {0} and {1}".format(self.from_date, self.to_date)
		for row in self.get('customer_award_detail'):
			je.append("accounts", {
				"account": self.default_receivable_account,
				"credit_in_account_currency": row.discount_value,
				"party":row.customer,
				"party_type":"Customer",

			})

			je.append("accounts", {
				"account": self.expense_account,
				"debit_in_account_currency": row.discount_value,
				"cost_center":self.cost_center
			})

		je.flags.ignore_permissions = True
		je.save()
		self.journal_entry = je.name
		
		invoices = self.get_sales_invoice_info()
		
		if invoices : 
			for row in invoices:
				log_doc = frappe.new_doc("Customer Award Log")
				log_doc.sales_invoice = row.name
				log_doc.journal_entry = je.name
				log_doc.flags.ignore_permissions = True
				log_doc.save()
		
		return self.journal_entry
	
	
	def get_sales_invoice_info(self):
		conditions = self.prepare_conditions()
		a= """
			select si.name
			from `tabSales Invoice`
			as si join `tabCustomer` as c  
			on si.customer=c.name
			where
				c.disabled =0 and si.docstatus =1 {conditions}
		""".format( conditions=conditions)
		invoices  = frappe.db.sql(a, as_dict=True)
		return invoices
			
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		


