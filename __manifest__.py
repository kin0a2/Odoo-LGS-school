# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'LGS School System',
    'version' : '16.0',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting/Accounting',
    'website': '',
    'depends' : ['mail','sale'],
    'data': ['views/account_account_views.xml','views/fees.xml','views/Admission.xml','views/student.xml','security/ir.model.access.csv','data/sequence.xml'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install':False,
    'license': 'LGPL-3',
}
