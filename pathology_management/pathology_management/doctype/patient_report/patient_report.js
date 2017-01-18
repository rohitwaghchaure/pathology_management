// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Patient Report', {
	setup: function(frm) {
		frm.add_fetch("patient", "mobile", "mobile");
		frm.add_fetch("patient", "email_id", "email_id");

		frappe.meta.get_docfield("Test","sample_name", frm.doc.name).in_list_view = 1;
	}
});
