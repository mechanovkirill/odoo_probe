from odoo import http


class MyController(http.Controller):
    @http.route('/telegram/webhook', type='http', auth='none', methods=['POST', 'GET'], csrf=False)
    def handler(self):
        print('88'*100)
        token = http.request.env['telegram.bot'].search([], order='id desc', limit=1).bot_token
        print(token)
        request_data = http.Request.get_json_data(http.request)
        print(request_data)
        user_id = request_data['message']['from']['id']
        print(user_id)
        text = request_data['message']['text']
        print(text)

        # products = http.request.env['product.product'].search([])
        # product_names = [p.name for p in products]
        # response = http.Response(str(product_names), status=200)
        response = http.Response('hello world!', status=200)
        return response


