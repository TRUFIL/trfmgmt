# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "trfmgmt"
app_title = "Transformer Management"
app_publisher = "DGSOL Infotech"
app_description = "Manages transformer for an organisation"
app_icon = "octicon octicon-file-directory"
app_color = "yellow"
app_email = "sales@dgsol-in.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/trfmgmt/css/trfmgmt.css"
# app_include_js = "/assets/trfmgmt/js/trfmgmt.js"

# include js, css files in header of web template
# web_include_css = "/assets/trfmgmt/css/trfmgmt.css"
# web_include_js = "/assets/trfmgmt/js/trfmgmt.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "trfmgmt.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "trfmgmt.install.before_install"
# after_install = "trfmgmt.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "trfmgmt.notifications.get_notification_config"

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
# 		"trfmgmt.tasks.all"
# 	],
# 	"daily": [
# 		"trfmgmt.tasks.daily"
# 	],
# 	"hourly": [
# 		"trfmgmt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"trfmgmt.tasks.weekly"
# 	]
# 	"monthly": [
# 		"trfmgmt.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "trfmgmt.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "trfmgmt.event.get_events"
# }

