from odoo import models, fields, api


class icq24_departaments(models.Model):
    _name = 'icq24.departaments'
    _description = 'Modelo para crear los departamentos de nuestra compañía'
    _rec_name = 'd_name'

    d_name = fields.Char(string='Nombre', required=True)
    d_description = fields.Char(string='Descripción', required=True)
