from odoo import models


class InheritedProducts(models.Model):
    _inherit = 'product.product'

