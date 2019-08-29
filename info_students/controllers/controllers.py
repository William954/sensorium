# -*- coding: utf-8 -*-
from odoo import http

# class InfoStudents(http.Controller):
#     @http.route('/info_students/info_students/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/info_students/info_students/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('info_students.listing', {
#             'root': '/info_students/info_students',
#             'objects': http.request.env['info_students.info_students'].search([]),
#         })

#     @http.route('/info_students/info_students/objects/<model("info_students.info_students"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('info_students.object', {
#             'object': obj
#         })