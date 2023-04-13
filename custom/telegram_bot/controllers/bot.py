from odoo import http
from werkzeug.wrappers import Response
import json
import logging

logger = logging.getLogger(__name__)


class BotWebhook(http.Controller):
    @http.route('/telegram/webhook', type='http', auth='public', methods=['POST', 'GET'], csrf=False)
    def handler(self) -> Response:
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
