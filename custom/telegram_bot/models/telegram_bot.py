from odoo import fields, models, api, http


class Bot(models.Model):
    _name = 'telegram.bot'
    _description = 'Telegram bot model'

    webhook_url_domain = fields.Char(required=True)
    bot_token = fields.Char(required=True)

    # @api.model
    # def create(self, vals_list: dict) -> models.Model:
    #     offer = super().create(vals_list)
    #     property_state = offer.property_id.state
    #     if property_state == 'new':
    #         offer.property_id.state = 'offer_received'
    #     return offer

    #  GET https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}
    def action_set_webhook_domain(self: models.Model) -> bool:

        return True

    # code = self.env['account.journal'].search([], order='id desc', limit=1).code
    # https://api.telegram.org/bot5849516026:AAHFhxviC8_juSNqkTwvLwjMmZlCqGelRFY/setWebhook?url=057b-91-151-136-186.ngrok-free.app/telegram/webhook


