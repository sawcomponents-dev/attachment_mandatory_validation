import frappe
from frappe import _
    
@frappe.whitelist()
def validate_attachment(workflow_state, workflow_action, doctype, name):
    attachment_mandatory_state = frappe.db.get_value("Attachment Validation Settings", doctype, "state")
    attachment_mandatory_action = frappe.db.get_value("Attachment Validation Settings", doctype, "workflow_action")
    is_attachment_mandatory = frappe.db.get_value("Attachment Validation Settings", doctype, "attachment_mandatory")
    if workflow_state and workflow_state == attachment_mandatory_state and workflow_action == attachment_mandatory_action and is_attachment_mandatory:
        attachments = frappe.get_list("File", {"attached_to_doctype": doctype, "attached_to_name": name}, ["name"])
        if len(attachments) < 1:
            return False
        else:
            return True
    else:
        return True