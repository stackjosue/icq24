# -*- coding: utf-8 -*-
{
    'name': "icq24_prueba",

    'summary': """
        Esta es una prueba para demostrar conocimientos a la empresa icq24""",

    'description': """
        Es una aplicación sencilla que muestra la creación de:
        Modelos, Vistas, y pequeñas funcionalidades.
        En principio busca crear módulos desde cero, pero tambien adaptar módulos existentes.
    """,

    'author': "Josué Vital Acosta",
    'website': "josuedva@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menus.xml',
        'views/actions_departaments.xml',
        'views/actions_branch.xml',
        'views/actions_engineering_proyects.xml',
        'views/actions_data_projects.xml',
        'report/report_data_projects.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
