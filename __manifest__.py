
# -*- coding: utf-8 -*-
{
    'name': 'Dealer Management & Field Visits',
    'version': '19.0.1.0.0',
    'summary': 'Dealer master, Sales Executive visits, and Executive-wise Field Visit report',
    'category': 'Sales/CRM',
    'author': 'Nasar A Tawhid',
    'license': 'LGPL-3',
    'depends': ['base','contacts','hr','sale','stock','web'],
    'data': [
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/res_partner_dealer_view.xml',
        'views/res_partner_dealer_search.xml',
        'views/dealer_visit_views.xml',
        'wizard/exec_visit_report_wizard_views.xml',
        'report/exec_visit_report_actions.xml',
        'report/exec_visit_report_templates.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'application': True,
}
