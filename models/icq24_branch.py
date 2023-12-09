from odoo import models, fields, api


class icq24_branch(models.Model):
    _name = 'icq24.branch'
    _description = 'Modelo para crear las sedes de nuestra compañía'
    _rec_name = 'b_name'

    b_name = fields.Char(string='País', required=True)
    b_address = fields.Char(string='Dirección', required=True)