# -*- coding: utf-8 -*-
{
    'author': "Moldeo Interactive,ADHOC SA,Odoo Community Association (OCA)",
    'category': 'Localization/Argentina',
    'depends': [
        'partner_identification',
        # this is for demo data, for fiscal position data on account
        # and also beacuse it is essential for argentinian use
        # for the sales config
        'base_setup',
    ],
    'installable': True,
    'license': 'AGPL-3',
    'name': 'Títulos de Personería y Tipos de documentos Arentinos',
    'data': [
        'data/res_partner_title_data.xml',
        'data/res_partner_id_category_data.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/res_partner_id_category_view.xml',
        'views/res_partner_id_number_view.xml',
        'views/sale_config_view.xml',
        'security/security.xml',
    ],
    'demo': [
        'demo/partner_demo.xml',
    ],
    'version': '10.0.1.0.0',
}
