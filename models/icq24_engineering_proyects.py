from odoo import models, fields, api
from odoo.exceptions import ValidationError

class icq24_engineering_proyects(models.Model):
    _name = 'icq24.engineering.proyects'
    _description = 'Modelo para crear los proyectos de ingeniería'
    _rec_name = 'e_name'

    b_branch_id = fields.Many2one('icq24.branch', string='Sede asignada')
    e_name = fields.Char(string='Nombre del proyecto', required=True)
    e_project_leader = fields.Many2one('icq24.prueba',string='Líder de proyecto',required=True,
        domain="[('b_branch_id', '=', b_branch_id), ('position', '=', 'SENIOR')]")
    e_basic_description = fields.Char(string='Descripción básica')
    e_description = fields.Text(string='Descripción', required=True)
    e_value = fields.Float(string='Valor del proyecto', required=True, default=False)
    e_engineering_details_ids = fields.One2many('icq24.engineering.details', 'e_engineering_id')
    e_status = fields.Selection([('PLANIFICACION', 'PLANIFICACION'), ('EJECUCION', 'EJECUCION'), ('ENTREGADO', 'ENTREGADO')],
                                string='Estado', default='PLANIFICACION', tracking=True)

    # Botón para terminar la etapa de planificación
    def run_planning(self):
        self.e_status = 'EJECUCION'
        if self.e_value < 1:
            raise ValidationError('Debe agregar un valor positivo al proyecto')

    # Botón para terminar la etapa de ejecución
    def run_execution(self):
        self.e_status = 'ENTREGADO'


class icq24_engineering_details(models.Model):
    _name = 'icq24.engineering.details'
    _description = 'Tabla que almacena los empleados por proyecto'

    e_engineering_id = fields.Many2one('icq24.engineering.proyects')
    e_employe_id = fields.Many2one('icq24.prueba', string='Nombre')

    #Se realiza una validación para garantizar que el empleado pueda estar en máximo 2 proyectos
    @api.constrains('e_employe_id')
    def _check_duplicate_employees(self):
        for record in self:
            employee_count = self.search_count([('e_employe_id', '=', record.e_employe_id.id)])
            if employee_count > 2:
                raise ValidationError(f"Sr usuario, el desarrollador {record.e_employe_id.name} ya tiene el máximo de proyectos asignados como desarrollador.")





















