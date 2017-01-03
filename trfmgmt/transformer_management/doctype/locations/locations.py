# -*- coding: utf-8 -*-
# Copyright (c) 2015, DGSOL InfoTech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Locations(Document):
	# Generate a unique ID for the location
	def autoname(self):
		if (self.loc_code):
			if (self.loc_code == "Auto"):
				# Generate a new location code using plant, substation and cd
				self.name = generate_location_code(self.loc_plant, self.loc_substation, self.loc_cd)
			else:
				# use loc_code as ID
				self.name = self.loc_code

	def validate(self):
		self.check_and_validate_loc_code()


	def check_and_validate_loc_code(self):
		if (self.loc_code):
			if (self.loc_code == "Auto"):
				# Generate a new location code using plant, substation and cd
				self.loc_code = generate_location_code(self.loc_plant, self.loc_substation, self.loc_cd)
		else:	
			# Throw exception
			frappe.throw(_("Location Code is Mandatory... Type 'Auto' to generate by system"), frappe.MandatoryError)




# Other Functions
# Function to generate location code
def generate_location_code(plant, substation, cd):
	if (plant):
		loc_code = plant.strip().upper() + "_" + substation.strip().upper() + "_" + cd.strip().upper()
	else:
		loc_code = substation.strip().upper() + "_" + cd.strip().upper()
	return loc_code

