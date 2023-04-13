from odoo import http
from werkzeug.wrappers import Response
import json
import logging
import traceback

logger = logging.getLogger(__name__)


class BotWebhook(http.Controller):
    @http.route('/telegram/webhook', type='http', auth='public', methods=['POST', 'GET'], csrf=False)
    def handler(self) -> Response:
        try:
            request_data = http.Request.get_json_data(http.request)
            chat_id = request_data['message']['chat']['id']
            text = request_data['message']['text']

            if text == '/get_all_products':
                products = http.request.env['product.product'].search([])
                product_lines = []
                for p in products:
                    product_lines.append(f'Name: {p.name}, Price: ${p.standard_price}')
                product_strings = '\n'.join(product_lines)
                data = {'method': 'sendMessage', 'chat_id': chat_id, 'text': product_strings}
                json_data = json.dumps(data)
                return Response(json_data, content_type='application/json')

            elif text == '/hello_world':
                data = {'method': 'sendMessage', 'chat_id': chat_id, 'text': 'Hello world!'}
                json_data = json.dumps(data)
                return Response(json_data, content_type='application/json')

            else:
                data = {'method': 'sendMessage', 'chat_id': chat_id, 'text': 'Incorrect response.'}
                json_data = json.dumps(data)
                return Response(json_data, content_type='application/json')
        except Exception:
            try:
                error_msg = traceback.format_exc()
                logger.warning(f"BotWebhook handler error: {error_msg}")
                request_data = http.Request.get_json_data(http.request)
                chat_id = request_data['message']['chat']['id']
                data = {'method': 'sendMessage', 'chat_id': chat_id, 'text': "Can't to handle your request"}
                json_data = json.dumps(data)
                return Response(json_data, content_type='application/json')
            except Exception:
                error_msg = traceback.format_exc()
                logger.warning(f"Can't send response to customer while BotWebhook handler error handling: {error_msg}")
