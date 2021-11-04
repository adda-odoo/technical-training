# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Manage training""",
    
    'description': 'Testing Module Creation',
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}