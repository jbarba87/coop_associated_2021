from odoo import models, fields, api
from odoo.exceptions import ValidationError

class empleado(models.Model):

  _inherit = "hr.employee"

  asistencias = fields.One2many('coop2.asistencia', 'tecnico_id', string="Asistencias")
  capacitaciones = fields.One2many('coop2.capacitacion', 'tecnico_id', string="Capacitaciones")
