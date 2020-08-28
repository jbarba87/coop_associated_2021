# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import datetime, timedelta


class cabana(models.Model):
  _name = "coop2.cabana"
  _description = "Cabaña del socio"
  _rec_name = "nombre"


  # Funcion que cuenta la cantidad de parcelas de la cabaña
  @api.one
  @api.depends('parcelas')
  def count_parcelas(self):
    if self.parcelas is not False:
      self.num_parcelas = self.env["coop2.parcela"].search_count([('cabana_id', '=', self.id)])

  # Funcion que autocompleta el campo Socio, para saber el socio dueño de la cabana
  @api.one
  @api.depends('socio_id')
  def get_socio(self):
    if self.socio_id is not False:
      socio = self.socio_id
      print("nombre ", socio.name)
      self.nombre_socio = socio.name


  nombre = fields.Char(string = "Nombre", required = True)
  
  comunidad = fields.Char(string = "Comunidad/Asociacion")
  
  distrito_cab = fields.Char(string = "Distrito")
  provincia_cab = fields.Char(string = "Provincia")
  departamento_cab = fields.Char(string = "Departamento")
  
  via_acceso = fields.Char(string = "Via de acceso")
  distancia_capital = fields.Integer(string = "Dist. desde capital Distrital (Kms)")
  tipo_movilidad = fields.Char(string = "Tipo de movilidad")
  
  # Campos computados
  num_parcelas = fields.Integer(string="Cantidad parcelas", compute="count_parcelas", store=True)
  
  # Campos relacionales
  socio_id = fields.Many2one('res.partner', string="Socio Propietario", required = True)
  parcelas = fields.One2many('coop2.parcela', 'cabana_id', string="Parcela")
  
  # Datos del socio
  nombre_socio = fields.Char(string="Socio", compute="get_socio")

