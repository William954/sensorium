# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StudentsFields(models.Model):
    _inherit = 'op.student'

    oficial_identification = fields.Binary(string="Identificación oficila")
    address_proof = fields.Binary(string="Comprobante de domicilio")
    birth_certificate = fields.Binary(string="Acta de nacimiento")
    curp = fields.Binary(string="CURP")
    highschool_certificate = fields.Binary(string="Certificado de ecundaria")
