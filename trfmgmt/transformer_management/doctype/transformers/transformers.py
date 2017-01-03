# -*- coding: utf-8 -*-
# Copyright (c) 2015, DGSOL InfoTech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals, division
import frappe
from frappe import _
from frappe.model.document import Document
from datetime import datetime, date, time

class Transformers(Document):
	def autoname(self):
		self.validate_serial_no()
		self.validate_tr_location()
		self.name = self.mfg_code + "_" + self.tr_sl_no + "-" + self.tr_location 

	def validate(self):
		self.validate_serial_no()
		self.validate_model_no()

	def validate_serial_no(self):
		if (self.tr_sl_no):
			if (self.tr_sl_no == "Auto"):
				sl_no = datetime.now()
				self.tr_sl_no = sl_no.strftime('%Y%m%d%H%M%S')
		else:
			frappe.throw(_("Serial No is mandatory. Type 'Auto' to generate"), frappe.MandatoryError)

	def validate_tr_location(self):
		if (not self.tr_location):
			frappe.throw(_("Code Designation is mandatory. Select Valid Code Designation"), frappe.MandatoryError)
	
	def validate_model_no(self):
		model = ""
		# Transformer parameters required or not dtbr
		if (self.tr_type_code == 'DRUM'):
			dtbr = False
		else:
			dtbr = True

		# throw exception if mandatory details are required
		if (dtbr):
			v_msg = ""
			if (self.tr_rating):
				if (self.tr_rating // 1000 > 0):
					model = str(round((self.tr_rating / 1000), 3)) + " MVA"
				else:
					model = str(self.tr_rating) + " kVA"
			else:
				v_msg = "Rating"

			if (self.tr_hv):
				if (self.tr_lv):
					model += "_" + str(self.tr_hv) + "/" + str(self.tr_lv) + " Volts"
				else:
					model += "_" + str(self.tr_hv) + " Volts"
			else:
				v_msg += ", High Voltage"

			if (v_msg):
				v_msg += " are mandatory. Please provide valid values"
				frappe.throw(_(v_msg), frappe.MandatoryError)
			else:
				self.tr_model = (model + "_" + self.tr_no_of_phases)
		else:
			self.tr_model = "No Specific Model for DRUM"