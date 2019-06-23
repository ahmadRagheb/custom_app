from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	config = [
		{
			"label": _("Company and Accounts"),
			"items": [

                {
                        "type": "report",
                        "name": "General Ledger Enhanced",
                        "doctype": "GL Entry",
                        "is_query_report": True,
                }
			]
		},
	]
	gst = {
		"label": _("Goods and Services Tax (GST India)"),
		"items": [
			{
				"type": "doctype",
				"name": "GST Settings",
			},
			{
				"type": "doctype",
				"name": "GST HSN Code",
			},
			{
				"type": "report",
				"name": "GSTR-1",
				"is_query_report": True
			},
			{
				"type": "report",
				"name": "GSTR-2",
				"is_query_report": True
			},
			{
				"type": "report",
				"name": "GST Sales Register",
				"is_query_report": True
			},
			{
				"type": "report",
				"name": "GST Purchase Register",
				"is_query_report": True
			},
			{
				"type": "report",
				"name": "GST Itemised Sales Register",
				"is_query_report": True
			},
			{
				"type": "report",
				"name": "GST Itemised Purchase Register",
				"is_query_report": True
			},
		]
	}
	retail = {
		"label": _("Retail Operations"),
		"items": [
			{
				"type": "page",
				"name": "pos",
				"label": _("POS"),
				"description": _("Point of Sale")
			},
			{
				"type": "doctype",
				"name": "Cashier Closing",
				"description": _("Cashier Closing")
			},
			{
				"type": "doctype",
				"name": "POS Settings",
				"description": _("Setup mode of POS (Online / Offline)")
			},
			{
				"type": "doctype",
				"name": "POS Profile",
				"label": _("Point-of-Sale Profile"),
				"description": _("Setup default values for POS Invoices")
			},
			{
				"type": "doctype",
				"name": "Loyalty Program",
				"label": _("Loyalty Program"),
				"description": _("To make Customer based incentive schemes.")
			},
			{
				"type": "doctype",
				"name": "Loyalty Point Entry",
				"label": _("Loyalty Point Entry"),
				"description": _("To view logs of Loyalty Points assigned to a Customer.")
			}
		]
	}
	subscriptions = {
		"label": _("Subscription Management"),
		"icon": "fa fa-microchip ",
		"items": [
			{
				"type": "doctype",
				"name": "Subscription Plan",
			},
			{
				"type": "doctype",
				"name": "Subscription"
			},
			{
				"type": "doctype",
				"name": "Subscription Settings"
			}
		]
	}
	countries = frappe.get_all("Company", fields="country")
	countries = [country["country"] for country in countries]
	if "India" in countries:
		config.insert(7, gst)
	domains = frappe.get_active_domains()
	if "Retail" in domains:
		config.insert(2, retail)
	else:
		config.insert(7, retail)
	if "Services" in domains:
		config.insert(2, subscriptions)
	else:
		config.insert(7, subscriptions)
	return config
