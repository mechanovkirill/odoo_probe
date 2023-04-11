from odoo import http


class MyController(http.Controller):
    @http.route('/telegram/webhook', type='http', auth='none', methods=['POST', 'GET'], csrf=False)
    def handler(self, **params):
        print('88'*100)
        print(params)

        # products = http.request.env['product.product'].search([])
        # product_names = [p.name for p in products]
        # response = http.Response(str(product_names), status=200)
        response = http.Response('hello world!', status=200)
        return response


