# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReportInvoiceWithPayment(models.AbstractModel):
    _name = 'report.website_account_extension.report_membership_form'
    _description = 'Comikha Membership form Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("called here")
        docs = self.env['account.move'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
        }