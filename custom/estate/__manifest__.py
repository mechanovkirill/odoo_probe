{
    'name': "Estate",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ir.inherited_users_views.xml',
        'views/ir.estate_types_views.xml',
        'views/ir.estate_tags_views.xml',
        'views/ir.estate_offers_views.xml',
        'views/ir.estate_property_views.xml',
        'views/estate_menus.xml',
        'data/estate.property.type.csv',
        'data/estate_property_data.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}