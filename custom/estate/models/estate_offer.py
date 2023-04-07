from odoo import models, fields, api
from datetime import date, timedelta
from typing import Iterable


class EstateOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate offers'

    price = fields.Float()
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        string='Status',
        copy=False
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_validity')

    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self: Iterable) -> None:
        for record in self:
            record.date_deadline = record.create_date + timedelta(days=record.validity) if record.create_date \
                else date.today() + timedelta(days=record.validity)

    def _inverse_validity(self: Iterable) -> None:
        for record in self:
            time_delta = record.date_deadline - date.today()
            record.validity = time_delta.days

    def action_accept_property(self: Iterable) -> bool:
        for record in self:
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.partner_id = record.partner_id
        return True

    def action_refuse_property(self: Iterable) -> bool:
        for record in self:
            record.status = "refused"
        return True
