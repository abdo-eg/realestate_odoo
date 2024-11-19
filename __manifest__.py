# -*- coding: utf-8 -*-

{
    'name': 'Realestate',
    'version': '17.0.0.1.0',
    'category': 'learning_modules',
    'author': 'Abdullah Ahmed',
    'summary': 'simple realestate application',

    'depends': [
        'base',
    ],
    'data': [
        'views/base_menu.xml',
        'views/property_view.xml',
        'security/ir.model.access.csv',

    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
