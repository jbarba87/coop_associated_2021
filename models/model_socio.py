# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import datetime, timedelta

class socio(models.Model):

  _inherit = "res.partner"
  
  # Funcion que cuenta el nuemro de camelidos del socio
  @api.one
  @api.depends('num_camelidos')
  def contar_camelidos(self):
    self.num_camelidos = self.env["coop2.camelido"].search_count([('socio_id', '=', self.id)])
#self.num_parcelas = self.env["coop2.parcela"].search_count([('cabana_id', '=', self.id)])
    print("          Cantidad camelidos", self.num_camelidos)

  @api.one
  @api.depends('num_cabanas')
  def contar_cabanas(self):
    self.num_cabanas = self.env["coop2.cabana"].search_count([('socio_id', '=', self.id)])

  @api.one
  @api.depends('num_parcelas')
  def contar_parcelas(self):
    self.num_parcelas = self.env["coop2.parcela"].search_count([('socio_id', '=', self.id)])


  @api.one
  @api.depends('num_potreros')
  def contar_potreros(self):
    self.num_potreros = self.env["coop2.potrero"].search_count([('socio_id', '=', self.id)])


  es_socio = fields.Boolean(default = False, string="Es socio?")
  cabanas = fields.One2many('coop2.cabana', 'socio_id', string="Cabañas")
  
  
  # Campos computados para estadistica
  # Si se coloca store=True aoarece 0 en el formulario (averiguar porquee)
  num_camelidos = fields.Integer(string="Numero de camelidos", compute="contar_camelidos")
  num_cabanas = fields.Integer(string="Numero de cabañas", compute="contar_cabanas")
  num_parcelas = fields.Integer(string="Numero de parcelas", compute="contar_parcelas")
  num_potreros = fields.Integer(string="Numero de potreros", compute="contar_potreros")
