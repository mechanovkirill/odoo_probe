from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "The probe model."

    name = fields.Char(required=True, size=50)
    description = fields.Text()
    postcode = fields.Char(size=20)
    date_availability = fields.Date(string='Availability Date', readonly=True)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer()
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Number of Facades')
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )

