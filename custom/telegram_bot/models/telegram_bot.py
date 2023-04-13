from odoo import fields, models, api, _
from odoo.exceptions import UserError
import requests

import logging

logger = logging.getLogger(__name__)


class Bot(models.Model):
    _name = 'telegram.bot'
    _description = 'Telegram bot model'

    webhook_url_domain = fields.Char(help='Your domain to create a telegram webhook without https:// i.e. "example.com"'
                                          'Must be encrypted.')
    bot_token = fields.Char(help='Your telegram bot token')

    #  GET https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}
    def action_set_webhook_domain(self: api.model) -> dict:
        domain = self.webhook_url_domain
        token = self.bot_token

        if domain and token:
            base_url = f"https://api.telegram.org/bot{token}/setWebhook?url={domain}/telegram/webhook"
            response = requests.get(url=base_url)
            if response.status_code == 200:
                logger.info(f'Webhook creating status code 200: {response.text}')
                return {
                    'warning': {
                        'title': _('Info'),
                        'message': f'Telegram response: {response.text}'
                    }
                }
            else:
                logger.warning(f'Webhook creating error: {response.status_code} {response.text}')
                return {'warning': {
                    'title': _("Warning"),
                    'message': f"Can't create webhook: {response.status_code} {response.text}"}}

        else:
            if not domain:
                logger.warning("Telegram bot domain missing while trying to install telegram webhook.")
                raise UserError("Telegram bot domain missing while trying to install telegram webhook.")
            if not token:
                logger.warning("Telegram bot token missing while trying to install telegram webhook.")
                raise UserError("Telegram bot token missing while trying to install telegram webhook.")
