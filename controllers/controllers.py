# -*- coding: utf-8 -*-
from odoo import http

# class Coop1(http.Controller):
#     @http.route('/coop1/coop1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coop1/coop1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coop1.listing', {
#             'root': '/coop1/coop1',
#             'objects': http.request.env['coop1.coop1'].search([]),
#         })

#     @http.route('/coop1/coop1/objects/<model("coop1.coop1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coop1.object', {
#             'object': obj
#         })