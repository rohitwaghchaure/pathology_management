# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PatientReport(Document):
	def get_sample_test_details(self):
		self.set('tests', [])

		for data in frappe.db.sql(""" Select 
				`tabPatient Sample`.name,  `tabPatient Sample`.sample_name, `tabTest`.test
			from 
				`tabPatient Sample`, `tabTest` 
			where 
				`tabPatient Sample`.name = `tabTest`.parent and `tabPatient Sample`.patient=%s 
				and `tabPatient Sample`.docstatus = 1 and `tabPatient Sample`.status = 'Pending'
			order by 
				`tabPatient Sample`.name""", self.patient, as_dict=1):
			child = self.append('tests', {})
			child.test = data.test
			child.sample_id = data.name
			child.sample_name = data.sample_name

	def on_submit(self):
		self.update_status()

	def update_status(self):
		for data in self.tests:
			name = frappe.db.get_value('Test', {'parent': data.sample_id, 'test': data.test}, 'name')
			frappe.set_value("Test", name, "result", data.result)