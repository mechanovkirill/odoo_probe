from datetime import timedelta, date
from odoo import models, fields, api


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
    partner_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    property_type_id = fields.Many2one("estate.property.type", string='Type')
    current_user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many(comodel_name="estate.property.offer", inverse_name="property_id")

    total_area = fields.Float(compute='_compute_total_area')
    best_price = fields.Float(compute='_compute_best_offers_price', string='Best Offer')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_offers_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0

    # @api.depends('offer_ids.price')
    # def _compute_best_offers_price(self):
    #     for record in self:
    #         max_ = 0
    #         if len(record.offer_ids) > 0:
    #             for i in range(len(record.offer_ids)):
    #                 if i == 0:
    #                     max_ = record.offer_ids[i].price
    #                     continue
    #                 if record.offer_ids[i].price > max_:
    #                     max_ = record.offer_ids[i].price
    #         record.best_price = max_
