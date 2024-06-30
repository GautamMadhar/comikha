from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    birth_date = fields.Date('Birth Date')
    nationality = fields.Char('Nationality')
    first_name = fields.Char('First Name')
    birth_place = fields.Char('Birth Place')
    occupation = fields.Char('Occupation')
    attachment_count = fields.Integer('Attachments')
    purpose_of_membership = fields.Selection([('full_member', 'Full Member'), ('trader', 'Trader'), ('mining_operator', 'Artisnal Mining Operator')], string="Purpose Of MemberShip")
    membership_info = fields.Selection([
        ("supporting_honorary_member","Membre d'honneur de soutien"),
        ("full_member", "Membre effectif"),
        ("trader","Négociant"),
        ("artisanal_mining_operator", "Exploitant minier artisanal"),
    ], string="Membership Information")
