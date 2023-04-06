from odoo import models, fields


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
