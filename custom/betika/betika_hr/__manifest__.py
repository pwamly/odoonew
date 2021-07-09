# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'betika leave',
    'version' : '1.1',
    'summary': 'leave portal',
    'sequence': -100, 
    'description': """Leave portal""",
    'category': 'Human Resources/Employees',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : [],
    'data': [
        'security/ir.model.access.csv',
        'views/users.xml'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
