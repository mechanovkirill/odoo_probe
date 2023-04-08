from odoo import models, fields


class EstateType(models.Model):
    _name = "estate.property.type"
    _description = "Type of estate"
    _order = 'sequence, name, id'

    name = fields.Char(size=40, required=True)

    properties_ids = fields.One2many(comodel_name='estate.property', inverse_name="property_type_id")

    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name of the estate type must be unique!')
    ]
