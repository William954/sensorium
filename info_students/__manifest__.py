# -*- coding: utf-8 -*-
{
    'name': "Complemento Educat",
    'summary': """
        Modulo complementario para el registro de nuevos estudiantes""",

    'description': """
        Se agergaron campos donde podran adjuntar los papeles oficiales del estudiante y tutor
    """,
    'author': "Xmarts",
    'website': "www.Xmarts.com",
    'category': 'Adecuacion',
    'version': '0.1',
    'depends': ['base', 'openeducat_core'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}