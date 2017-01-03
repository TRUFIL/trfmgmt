# -*- coding: utf-8 -*-
# Copyright (c) 2015, DGSOL InfoTech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class TestResults(Document):
	def validate(self):
		self.validate_mandatory_fields()
		self.update_calculated_fields()

	def validate_mandatory_fields(self):
		if not (self.dga_tcg and self.dga_tcg != 0):
			frappe.throw(_("Total Gas Content is mandatory. Did not save"), frappe.MandatoryError)

	def update_calculated_fields(self):
		self.dga_tcgc = round(float(self.dga_h2 + self.dga_co + self.dga_ch4 + self.dga_c2h6 + self.dga_c2h4 + self.dga_c2h2 + self.dga_c3h8 + self.dga_c3h6), 2)
		if (self.dga_tcgc != 0.0):
			self.dga_tcgc_tcg = round((self.dga_tcgc / 100) / (self.dga_tcg), 2)
		else:
			self.dga_tcgc_tcg = 0.0

		if (self.dga_c2h2 != 0.0 or self.dga_c2h4 != 0.0 or self.dga_ch4 != 0.0):
			self.duvals_ratio_1 = get_duvals_ratio_1(self.dga_c2h2, self.dga_c2h4, self.dga_ch4)
		else:
			self.duvals_ratio_1 = ""

		if (self.duvals_ratio_1 != ""):
			self.duvals_region = get_duvals_region(self.dga_c2h2, self.dga_c2h4, self.dga_ch4)
		else:
			self.duvals_region = "NA"

		self.duvals_fault = get_duvals_fault(self.duvals_region)
		self.duvals_fault_example = get_duvals_fault_example(self.duvals_region)

# Supporting Functions
def get_duvals_ratio_1(c2h2, c2h4, ch4):
	# Calculate percentage of c2h2, c2h4, ch4 
	if (c2h2 != 0 or c2h4 != 0 or ch4 != 0):
		p = c2h2 + c2h4 + ch4
		p1 = 100 * ch4 / p
		p2 = 100 * c2h4 / p
		p3 = 100 * c2h2 / p
		return str(round(p1,2)) + " : " + str(round(p2,2)) + " : " + str(round(p3,2))
	else:
		return ""

def get_duvals_region(c2h2, c2h4, ch4):
	region = ""
	# check if Duval's analysis is applicable

	if (c2h2 > 1 or c2h4 > 50 or ch4 > 50):
		# Calculate percentage of c2h2, c2h4, ch4 
		p = c2h2 + c2h4 + ch4
		p1 = 100 * ch4 / p
		p2 = 100 * c2h4 / p
		p3 = 100 * c2h2 / p

		if (p1 >= 98):
			region = "PD"
		else:
			if ((p3 < 4) and (p2 < 20)):
				region = "T1"
			if ((p3 < 4) and (p2 >= 20 and p2 < 50)):
				region = "T2"
			if ((p3 < 15) and (p2 >= 50)):
				region = "T3"
			if ((p3 >= 4 and p3 < 13) and (p2 < 40)):
				region = "DT"
			if ((p3 >= 4 and p3 < 38) and (p2 >= 40 and p2 < 50)):
				region = "DT"
			if ((p3 >= 15 and p3 < 38) and (p2 >= 50)):
				region = "DT"
			if ((p3 >= 13) and (p2 < 23)):
				region = "D1"
			if ((p3 >= 23 and p3 < 40) and (p2 >= 13 and p2 < 38)):
				region = "D2"
			if ((p3 >= 23) and (p2 >= 38)):
				region = "D2"
	else:
		region = "NA"

	# Return the region details calculated above
	return region

def get_duvals_fault(region):
	fault = ""
	if (region):
		if (region == "PD"):
			fault = "<p>PARTIAL DISCHARGE - PD</p>"
		elif (region == "D1"):
			fault = "<p>DISCHARGE OF LOW ENERGY - D1</p>"
		elif (region == "D2"):
			fault = "<p>DISCHARGE OF HIGH ENERGY - D2</p>"
		elif (region == "DT"):
			fault = "<p>THERMAL AND ELECTRICAL FAULT - DT</p>"
		elif (region == "T1"):
			fault = "<p>THERMAL FAULT AT TEMPERATURE &lt; 300 <sup>O</sup>C - T1</p>"
		elif (region == "T2"):
			fault = "<p>THERMAL FAULT AT TEMPERATURE 300-700 <sup>O</sup>C - T2</p>"
		elif (region == "T3"):
			fault = "<p>THERMAL FAULT AT TEMPERATURE &gt; 700 <sup>O</sup>C - T3</p>"
		elif (region == "NA"):
			fault = "<p>DUVAL'S TRIANGLE ANALYSIS NOT APPLICABLE</p>"
		else:
			fault = ""
	return fault

def get_duvals_fault_example(region):
	fault_example = ""
	if (region):
		if (region == "PD"):
			fault_example = "<p>Discharge of the cold plasma(corona) type in gas bubbles or voids, with the possible formation of X-wax in paper</p>"
		elif (region == "D1"):
			fault_example = "<p>(1) Partial discharge of sparking type, include pinholes, carbonized puncture in paper</p> <p>(2) Low energy arcing including carbonized perforation or or surface tracking of paper or carbon particles in oil</p>"
		elif (region == "D2"):
			fault_example = "<p>(1) Discharges in paper or oil, with power flow through, resulting in extensive damage to paper.</p><p>(2) Large formation of carbon particle in oil, metal fusion, tripping of equipment and gas alarms</p>"
		elif (region == "DT"):
			fault_example = "<p>Mixture of thermal and electrical faults</p>"
		elif (region == "T1"):
			fault_example = "Evidenced by paper turning brownish (&gt; 200 <sup>O</sup>C) or carbonized (&lt; 300 <sup>O</sup>C)"
		elif (region == "T2"):
			fault_example = "<p>Carbonization of paper, formation of carbon particle in oil</p>"
		elif (region == "T3"):
			fault_example = "Extensive formation of carbon particle in oil, metal coloration (800 <sup>O</sup>C) or metal fusion (&gt; 1000 <sup>O</sup>C)"
		else:
			fault_example = ""
	return fault_example
