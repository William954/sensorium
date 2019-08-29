# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StudentsFields(models.Model):
    _inherit = 'op.student'

    oficial_identification = fields.Binary(string="Identificación oficial")
    address_proof = fields.Binary(string="Comprobante de domicilio")
    birth_certificate = fields.Binary(string="Acta de nacimiento")
    curp = fields.Binary(string="CURP")
    highschool_certificate = fields.Binary(string="Certificado de secundaria")

    check_identification_oficial = fields.Boolean( string = "Identificación oficial", default = False )
    check_adress_proof = fields.Boolean( string = "Comprobante de domicilio", default = False )
    check_birth_certificate = fields.Boolean( string ="Acta de nacimiento", default = False )
    check_curp = fields.Boolean( string = "CURP", default = False )
    check_highschool_certificate = fields.Boolean( string = "Certificado de secundaria", default = False )
