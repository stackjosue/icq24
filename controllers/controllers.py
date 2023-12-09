# -*- coding: utf-8 -*-
# from odoo import http


# class Icq24Prueba(http.Controller):
#     @http.route('/icq24_prueba/icq24_prueba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/icq24_prueba/icq24_prueba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('icq24_prueba.listing', {
#             'root': '/icq24_prueba/icq24_prueba',
#             'objects': http.request.env['icq24_prueba.icq24_prueba'].search([]),
#         })

#     @http.route('/icq24_prueba/icq24_prueba/objects/<model("icq24_prueba.icq24_prueba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('icq24_prueba.object', {
#             'object': obj
#         })
