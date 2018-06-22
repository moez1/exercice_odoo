# -*- coding: utf-8 -*-
{
    'name' : 'Exercice odoo',
    'version' : '1.1',
    'author': "Moez labidi",
    'summary': ' ',
    'sequence': 30,
    'description': """
     Customize odoo 

    """,
    'category': 'Sale',
    'images' : [],
    'depends' : ['sale','portal','base'],
    'data': [
        'views/sale_views.xml',
        'report/sale_report.xml',
        'views/portal_template.xml',
        'wizard/exercice_report_view.xml',
        'report/exercice_report.xml',
    ],
    'demo': [
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
