from odoo import models, fields


class EstateType(models.Model):
    _name = "estate.property.type"
    _description = "Type of estate"

    name = fields.Char(size=40, required=True)

    properties_ids = fields.One2many(comodel_name='estate.property', inverse_name="property_type_id")
    property_name = fields.Char()
    property_expected_price = fields.Float()


    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name of the estate type must be unique!')
    ]
