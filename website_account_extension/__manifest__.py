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
    "depends": ['web','account'],
    "data": [
        'data/report_paperformat_data.xml',
        'views/account_report.xml',
        
    ],
    "application": True,
    "installable": True,
}
