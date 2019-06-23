// Copyright (c) 2019, anas and contributors
// For license information, please see license.txt
cur_frm.add_fetch('customer','company','company');
cur_frm.add_fetch('company','default_receivable_account','default_receivable_account');
cur_frm.add_fetch('company','cost_center','cost_center');

frappe.ui.form.on('Customer Award', {
	onload: function(frm) {
		frm.set_value('company', '');
		frm.set_value('total_amount', '');
		frm.set_value('total_discount', '');
		frm.set_value('default_receivable_account', '');
		frm.set_value('journal_entry', '');
		frm.set_value('cost_center', '');
		frm.set_value('customer', '');
		frm.clear_table("customer_award_detail");
		frm.set_value('expense_account', '');
		
		frm.set_query("default_receivable_account", function () {
			return {
				"filters": {
					"company": frm.doc.company,
					"account_type": "Receivable",
					"is_group":0
				}
			};
		});
		frm.set_query("expense_account", function () {
			return {
				"filters": {
					"company": frm.doc.company,
					"root_type": "Expense",
					"is_group":0
				}
			};
		});
		frm.set_query("cost_center", function () {
			return {
				"filters": {
					"company": frm.doc.company,
					"is_group":0
				}
			};
		});
	},
	refresh: function(frm) {
		frm.disable_save();
	},
	get_sales_invoices: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "get_customers_info",
			freeze: true,
			freeze_message: 'Get Info...',
			callback: function(r) {
				if(!r.exc){
					setTimeout(frappe.dom.unfreeze(),3000);
					frm.events.refresh(frm);
					cur_frm.refresh();
					frm.set_value('journal_entry', '');

				}
			}
		});
	},
	create_journal_entry: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "make_journal_entry",
			freeze: true,
			freeze_message: 'Make Journal Entry...',
			callback: function(r) {
				if(!r.exc){
					setTimeout(frappe.dom.unfreeze(),3000);
					frm.events.refresh(frm);
					cur_frm.refresh();
				}
			}
		});
				
	},
	
});
frappe.ui.form.on('Customer Award Detail', {
	refresh: function(frm) {
	},
	discount_amount: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "calc_sales_invoice",
			freeze: true,
			freeze_message: 'Calculate...',
			callback: function(r) {
				if(!r.exc){
					frm.events.refresh(frm);
					cur_frm.refresh();								
				}
			}
		});
	},
	
});
