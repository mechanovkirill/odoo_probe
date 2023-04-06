from datetime import timedelta, date
from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "The probe model."

    name = fields.Char(required=True, size=50)
    description = fields.Text()
    postcode = fields.Char(size=14)
    date_availability = fields.Date(
        string='Availability Date', copy=False,
        default=lambda self: date.today() + timedelta(days=90)
    )
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Number of Facades')
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'),
         ('canceled', 'Canceled')],
        string='Status',
        default='new',
        required=True,
        copy=False
    )
    marks = fields.Text(string="Marks")
    partner_id = fields.Many2one("res.partner", string="Buyer")
    property_type_id = fields.Many2one("estate.property.type", string='Type')
    current_user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)

