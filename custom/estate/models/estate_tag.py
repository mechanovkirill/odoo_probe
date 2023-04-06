from odoo import models, fields


class EstateTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate property tags model'

    name = fields.Char(required=True, size=50)
