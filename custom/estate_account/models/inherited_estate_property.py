from typing import Iterable
from odoo import models, fields


class InheritedEstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold_estate(self):
        action = super().action_sold_estate()
        partner_id = None
        for record in self:
            partner_id = record.partner_id

        journal = self.env['account.journal'].create({
            'name': 'dfgsghghghsgh', 'code': '123235gfffffffhd', 'type': 'sale',
        })
        journal_id = journal.id

        #  get current company
        company = self.env.company

        self.env['account.move'].create({
            'partner_id': partner_id.id,
            'move_type': 'out_invoice',
            'journal_id': journal_id,
        })

        return action
