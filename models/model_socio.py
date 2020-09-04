# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import json
from datetime import datetime, timedelta
import os
class socio(models.Model):

  _inherit = "res.partner"


  _sql_constraints = [
    ('DNI_unico', 'unique (dni)', 'Ya existe un socio con ese número de DNI.')
  ]
  
  # Funcion que cuenta el nuemro de camelidos del socio
  @api.one
  @api.depends('cabanas.parcelas.potreros.camelidos.socio_id')
  def contar_camelidos(self):
    self.num_camelidos = self.env["coop2.camelido"].search_count([('socio_id', '=', self.id)])
    print("          Cantidad camelidos", self.num_camelidos)

  @api.one
  @api.depends('cabanas.socio_id')
  def contar_cabanas(self):
    if self.cabanas is not False:
      self.num_cabanas = self.env["coop2.cabana"].search_count([('socio_id', '=', self.id)])

  @api.one
  @api.depends('cabanas.parcelas.socio_id')
  def contar_parcelas(self):
    self.num_parcelas = self.env["coop2.parcela"].search_count([('socio_id', '=', self.id)])


  @api.one
  @api.depends('cabanas.parcelas.potreros.socio_id')
  def contar_potreros(self):
    self.num_potreros = self.env["coop2.potrero"].search_count([('socio_id', '=', self.id)])


  es_socio = fields.Boolean(default = False, string="Es socio?")
  cabanas = fields.One2many('coop2.cabana', 'socio_id', string="Cabañas")
  
  
  # Campos computados para estadistica
  # Si se coloca store=True aoarece 0 en el formulario (averiguar porquee)
  num_camelidos = fields.Integer(string="Numero de camelidos", compute="contar_camelidos", store=True)
  num_cabanas = fields.Integer(string="Numero de cabañas", compute="contar_cabanas", store=True)
  num_parcelas = fields.Integer(string="Numero de parcelas", compute="contar_parcelas", store=True)
  num_potreros = fields.Integer(string="Numero de potreros", compute="contar_potreros", store=True)
  
  @api.one
  @api.depends('cabanas.parcelas.potreros.camelidos.socio_id')
  def contar_huacayos(self):
    self.num_alpacas_huacayo = self.env["coop2.camelido"].search_count([('socio_id', '=', self.id), ('raza', '=', 'huacayo')])

  @api.one
  @api.depends('cabanas.parcelas.potreros.camelidos.socio_id')
  def contar_suris(self):
    self.num_alpacas_suri = self.env["coop2.camelido"].search_count([('socio_id', '=', self.id), ('raza', '=', 'suri')])

  @api.one
  @api.depends('cabanas.parcelas.potreros.camelidos.socio_id')
  def contar_machos(self):
    self.num_alpacas_macho = self.env["coop2.camelido"].search_count([('socio_id', '=', self.id), ('sexo', '=', 'macho')])

  @api.one
  @api.depends('cabanas.parcelas.potreros.camelidos.socio_id')
  def contar_hembras(self):
    self.num_alpacas_hembra = self.env["coop2.camelido"].search_count([('socio_id', '=', self.id), ('sexo', '=', 'hembra')])

  num_alpacas_huacayo = fields.Integer(string="Alpacas Huacayo", compute="contar_huacayos", store=True)
  num_alpacas_suri = fields.Integer(string="Alpacas Suri", compute="contar_suris", store=True)
  num_alpacas_macho = fields.Integer(string="Alpacas Macho", compute="contar_machos", store=True)
  num_alpacas_hembra = fields.Integer(string="Alpacas Hembra", compute="contar_hembras", store=True)
 
 
  # Campos personales y sus funciones
  @api.constrains('dni')
  def check_dni(self):
    for rec in self:
      if len(rec.dni) < 8:
        raise ValidationError('El campo DNI debe tener 8 digitos.')
      if not rec.dni.isnumeric():
        raise ValidationError('El campo DNI solo debe contener números.')
 
 
 
 
  # Campos personales
  dni = fields.Char(string="DNI", size=8, required=True)
  fecha_nac = fields.Date(string="Fecha de nacimiento")
  direccion = fields.Char(string="Dirección", size=30)
  
  # Lugar de nacimiento
  distrito_nac = fields.Char(string = "Distrito")
  provincia_nac = fields.Char(string = "Provincia")
  
  archive = os.getcwd() + '/addons/coop2/models/dep.txt'
  
  # Importar departamentos
  with open(archive, 'r') as dptos:
    data = json.load(dptos)
    
  departamentos = [ (d['departamento'], d['departamento']) for d in data ]
  departamento_nac = fields.Selection(departamentos, string = "Departamento")

  # Otros datos
  sexo = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino')], default="masculino", string="Sexo")
  
  estado_civil = fields.Selection([
  ('soltero', 'Soltero'),
  ('casado', 'Casado'),
  ('viudo', 'Viudo'),
  ('divorciado', 'Divorciado'),
  ], default="soltero", string="Estado Civil")
  
  # Domicilio
  dom_permanente = fields.Char(size=30)
  dom_transitorio = fields.Char(size=30)
  
  num = [(x, str(x)) for x in range(1, 20)]
  personas_nucleo = fields.Selection(num, string="Personas nucleo familiar")
  
  
  num = [(x, str(x)) for x in range(1, 10)]
  num_hijos = fields.Selection(num, string="Número de hijos")
  num_hijas = fields.Selection(num, string="Número de hijas")
  
  # Campo relacional al historial del socio
  historial = fields.One2many('coop2.historial', 'socio_id', string="Historial")

