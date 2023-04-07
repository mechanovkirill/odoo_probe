from odoo import models, fields


class EstateType(models.Model):
    _name = "estate.property.type"
    _description = "Type of estate"

    name = fields.Char(size=40, required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name of the estate type must be unique!')
    ]
