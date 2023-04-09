from typing import Any
from odoo import models, Command
from odoo.exceptions import UserError


class InheritedEstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold_estate(self: models.Model) -> Any:
        action = super().action_sold_estate()
        partner_id = None
        price_unit = None
        estate_name = None
        for record in self:
            partner_id = record.partner_id
            price_unit = record.selling_price * 0.06 + 100.0
            estate_name = record.name

        if not price_unit:
            raise UserError("Selling price can't be zero.")

        code = self.env['account.journal'].search([], order='id desc', limit=1).code
        code = int(code) + 1

        journal = self.env['account.journal'].create({
            'name': 'dfdsgdfsgh', 'code': str(code), 'type': 'sale',
        })
        journal_id = journal.id

        #  get current company
        company = self.env.company

        self.env['account.move'].create({
            'partner_id': partner_id.id,
            'move_type': 'out_invoice',
            'journal_id': journal_id,
            "invoice_line_ids": [
                Command.create({
                    "name": estate_name,
                    "quantity": 1,
                    "price_unit": price_unit,
                })
            ],
        })

        return action
