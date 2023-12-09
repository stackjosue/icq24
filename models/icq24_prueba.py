# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class icq24_prueba(models.Model):
    _name = 'icq24.prueba'
    _description = 'Modelo para crear Y editar usuarios para nuestra compañía'
    _rec_name = 'name'

    b_branch_id = fields.Many2one('icq24.branch',string='Sede', required=True)
    name = fields.Char(string='Nombre', required=True)
    b_departaments_id = fields.Many2one('icq24.departaments', string='Departamento')
    age = fields.Integer(string='Edad', required=True)
    identification = fields.Integer(string='Identificación', required=True)
    position = fields.Selection([('NEW','NUEVO'),('JUNIOR','JUNIOR'),('MID','MID'),('SENIOR','SENIOR'),('GERENCIA','GERENCIA')], string='Posición', required=True)
    job_modality = fields.Boolean(string='¿Trabaja remoto?')








