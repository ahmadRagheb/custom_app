# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "custom_app"
app_title = "Custom App"
app_publisher = "anas"
app_description = "custom"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "anasanwar"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/custom_app/css/custom_app.css"
# app_include_js = "/assets/custom_app/js/custom_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/custom_app/css/custom_app.css"
# web_include_js = "/assets/custom_app/js/custom_app.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "custom_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "custom_app.install.before_install"
# after_install = "custom_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "custom_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
	"GL Entry": {
		"validate": ["custom_app.api_helper.add_sales_customer_info"]
	},
        "Item": {
                "before_insert": ["custom_app.api.naming_series_for_item"]
        }

}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"custom_app.tasks.all"
# 	],
# 	"daily": [
# 		"custom_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"custom_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"custom_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"custom_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "custom_app.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "custom_app.event.get_events"
# }

