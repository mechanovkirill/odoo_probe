from odoo import models, fields


class EstateType(models.Model):
    _name = "estate.property.type"
    _description = "Type of estate"

    name = fields.Char(size=40, required=True)
