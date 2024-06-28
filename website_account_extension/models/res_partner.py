from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    birth_date = fields.Date('Birth Date')
    nationality = fields.Char('Nationality')
    first_name = fields.Char('First Name')
    birth_place = fields.Char('Birth Place')
    occupation = fields.Char('Occupation')
    attachment_count = fields.Integer('Attachments')
