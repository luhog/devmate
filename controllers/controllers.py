# -*- coding: utf-8 -*-
from odoo import http

# class Betavision(http.Controller):
#     @http.route('/betavision/betavision/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/betavision/betavision/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('betavision.listing', {
#             'root': '/betavision/betavision',
#             'objects': http.request.env['betavision.betavision'].search([]),
#         })

#     @http.route('/betavision/betavision/objects/<model("betavision.betavision"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('betavision.object', {
#             'object': obj
#         })