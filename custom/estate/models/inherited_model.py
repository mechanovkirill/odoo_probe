from odoo import models, fields


class InheritedResUsersModel(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='current_user_id')
