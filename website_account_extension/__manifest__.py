# -*- coding: utf-8 -*-

{
    "name": "Website Invoice Extension",
    "category": "Accounting",
    "summary": "Generate custom report from Invoice",
    "version": "17.0.0.1.0",
    "license": "AGPL-3",
    'description': """
        Generate custom report from Invoice.
    """,
    "depends": ['web','account','website','contacts'],
    "data": [
        'data/report_paperformat_data.xml',
        'views/account_report.xml',
        'views/contact_form.xml',
        'views/res_partner.xml',
        'data/form_page.xml',   
    ],
    "application": True,
    "installable": True,
}
