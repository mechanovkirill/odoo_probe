{
    'name': "Telegram bot",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ir.bot_views.xml',
        'views/bot_menus.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}