from odoo import models, fields, api
from odoo.exceptions import ValidationError

class icq24_data_projects(models.Model):
    _name = 'icq24.data.projects'
    _description = 'Modelo para ver la suma de los valores de los proyectos dependiendo del estado.'
    _rec_name = 'd_status'

    d_status = fields.Selection(
        [('ELEJIR', 'Elija un estado'),('PLANIFICACION', 'PLANIFICACION'), ('EJECUCION', 'EJECUCION'), ('ENTREGADO', 'ENTREGADO')],
        string='Estado', default='ELEJIR', tracking=True)
    d_total_value = fields.Float(string='Valor total de los proyectos', compute='_calculate_total')

    #Validar que no hayan registros del mismo estado
    @api.constrains('d_status')
    def _check_unique_d_status(self):
        for record in self:
            if self.search_count([('d_status', '=', record.d_status)]) > 1:
                raise ValidationError(f"Sr Usuario, el estado '{record.d_status}' ya existe en otro registro.")


    #Se realiza el la suma con un api.depends de los registros del tipo seleccionado.
    #Se realiza una 'query' al modelo correspondiente y se le indican los parámetros de búsqueda.
    @api.depends('d_status','d_total_value')
    def _calculate_total(self):

        for record in self:

            if record.d_status == 'ELEJIR':
                self.d_total_value = 0

            if record.d_status == 'PLANIFICACION':
                query = self.env['icq24.engineering.proyects'].search([
                    ('e_status', '=', 'PLANIFICACION')
                ])
                value = 0
                if query:
                    for registro in query:
                        value = value + registro.e_value
                record.d_total_value = value


            if record.d_status == 'EJECUCION':
                query = self.env['icq24.engineering.proyects'].search([
                    ('e_status', '=', 'EJECUCION')
                ])
                value = 0
                if query:
                    for registro in query:
                        value = value + registro.e_value
                record.d_total_value = value


            if record.d_status == 'ENTREGADO':
                query = self.env['icq24.engineering.proyects'].search([
                    ('e_status', '=', 'ENTREGADO')
                ])
                value = 0
                if query:
                    for registro in query:
                        value = value + registro.e_value
                record.d_total_value = value


    # Función para imprimir el reporte de los proyectos
    def print_report(self):
        datas = {
            'id': self.id,
            'model': 'icq24.data.projects'
        }

        return {
            'type': 'ir.actions.report',
            'report_name': 'icq24_prueba.data_projects_template',
            'report_type': 'qweb-pdf',
            'datas': datas
        }
