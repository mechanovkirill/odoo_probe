from odoo import fields, models, api
from odoo.exceptions import UserError
import requests



class Bot(models.Model):
    _name = 'telegram.bot'
    _description = 'Telegram bot model'

    webhook_url_domain = fields.Char(help='bla bla')
    bot_token = fields.Char(help='bla bla')

    # @api.model
    # def create(self, vals_list: dict) -> models.Model:
    #     offer = super().create(vals_list)
    #     property_state = offer.property_id.state
    #     if property_state == 'new':
    #         offer.property_id.state = 'offer_received'
    #     return offer
    # if self.env['account.journal'].search([], order='id desc', limit=1):
    #     print('**' * 100)
    #     print(True)

    #  GET https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}
    def action_set_webhook_domain(self: models.Model) -> requests.get:
        domain = None
        token = None
        for record in self:
            print(record)
            domain = record.webhook_url_domain
            token = record.bot_token

        base_url = f"https://api.telegram.org/bot{token}/setWebhook?url={domain}/telegram/webhook"

        if domain and token:
            return requests.get(url=base_url)
        else:
            raise UserError("Telegram bot domain and/or token missing.")


