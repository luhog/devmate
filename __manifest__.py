# -*- coding: utf-8 -*-
{
    'name': "betavision",

    'summary': """
       custom fields and reports""",

    'description': """
       custom fields and reports
    """,

    'author': "Betavision",
    'website': "http://www.betavision.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/sale_order.xml',
        'report/invoice.xml',
        'report/header.xml',
        'report/footer.xml',
        'report/paper_format.xml',
        'data/mail_template_data.xml',
        'data/invoice_action_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    }
