frappe.ui.form.on("Purchase Order", {
    before_workflow_action: async (frm) => {
        let promise = new Promise((resolve, reject) => {
            frappe.dom.unfreeze()
            frappe.call({
                method: "attachment_mandatory_validation.attachment_mandatory.validate_attachment",
                args: {
                    workflow_state: frm.doc.workflow_state,
                    workflow_action: frm.selected_workflow_action,
                    doctype: frm.doc.doctype,
                    name: frm.doc.name
                },
                callback: function(r) {
                    if (r.message == true) {
                        resolve();
                    } else {
                        reject();
                    }
                }
            });
    	});
    	await promise.catch(() => {frappe.throw(__("Attahment(s) is mandatory to proceed to next state"));});
    }
})