# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import datetime, timedelta


class asociacion(models.Model):
  _name = "coop2.asociacion"
  _description = "Asociacion"
  _rec_name = "nombre_asociacion"
  
  nombre_asociacion = fields.Char(string="Nombre", required=True)


