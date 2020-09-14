# -*- coding: utf-8 -*-
{
    'name': "coop2",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/view_socio.xml',
        'views/view_cabana.xml',
        'views/view_asociacion.xml',
        'views/view_parcela.xml',
        'views/view_potrero.xml',
        'views/view_camelido_andino.xml',
        'views/view_historial.xml',
        'views/view_tablero.xml',
#        'data/data.xml',
#        'data/data_esquila.xml',
        'data/asoc.xml',
        'data/user_1.xml',
        'data/user_2.xml',
        'data/user_3.xml',
        'data/user_4.xml',
        'data/user_5.xml',
        'data/user_6.xml',
        'data/user_7.xml',
        'data/user_8.xml',
####        'data/user_9.xml',
        'data/user_10.xml',
        'data/user_11.xml',
        'data/user_12.xml',
        'data/user_13.xml',
        'data/user_14.xml',
        'data/user_15.xml',
        'data/user_16.xml',
        'data/user_17.xml',
        'data/user_18.xml',
        'data/user_19.xml',
        'data/user_20.xml',
####      'data/user_21.xml',
####       'data/user_22.xml',
        'data/user_23.xml',
        'data/user_24.xml',
        'data/user_25.xml',
        'data/user_26.xml',
        'data/user_27.xml',
        'data/user_28.xml',
        'data/user_29.xml',
        'data/user_30.xml',
####        'data/user_31.xml',
        'data/user_32.xml',
        'data/user_33.xml',
        'data/user_34.xml',
        'data/user_35.xml',
        'data/user_36.xml',
        'data/user_37.xml',
        'data/user_38.xml',
        'data/user_39.xml',
        'data/user_40.xml',
        'data/user_41.xml',
        'data/user_42.xml',
        'data/user_43.xml',
        'data/user_44.xml',
        'data/user_45.xml',
        'data/user_46.xml',
        'data/user_47.xml',
        'data/user_48.xml',
        'data/user_49.xml',
        'data/user_50.xml',
        'views/templates_prueba.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
 #       'demo/demo.xml',
    ],
    'application': True,
}
