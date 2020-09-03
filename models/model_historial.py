from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import datetime, timedelta

class historial(models.Model):
  _name = "coop2.historial"
  _description = "Historial del socio"
  
  fecha_muestreo = fields.Date()
  socio_id = fields.Many2one('coop2.potrero', string="Socio")
  num_camelidos = fields.Integer(string="Total camélidos")
  num_camelidos_macho = fields.Integer(string="Camélidos machos")
  num_camelidos_hembra = fields.Integer(string="Camélidos hembras")
