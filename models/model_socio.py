# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import datetime, timedelta

class socio(models.Model):

  _inherit = "res.partner"
    
  es_socio = fields.Boolean(default = False, string="Es socio?")
  #campo_prueba = fields.Char(string="Campo de prueba")
  cabanas = fields.One2many('coop2.cabana', 'socio_id', string="Cabañas")
