# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pathology_management"
app_title = "Pathology Management"
app_publisher = "Frappe"
app_description = "Pathology Management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "rohit@erpnext.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pathology_management/css/pathology_management.css"
# app_include_js = "/assets/pathology_management/js/pathology_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/pathology_management/css/pathology_management.css"
# web_include_js = "/assets/pathology_management/js/pathology_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pathology_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

fixtures = ["Role"]

# Installation
# ------------

# before_install = "pathology_management.install.before_install"
# after_install = "pathology_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pathology_management.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pathology_management.tasks.all"
# 	],
# 	"daily": [
# 		"pathology_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"pathology_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pathology_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pathology_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pathology_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pathology_management.event.get_events"
# }

