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
  
  # Funcion que cuenta el numero de camelidos del socio
  @api.one
  @api.depends('cabanas.parcelas.potreros.camelidos.socio_id')
  def contar_camelidos(self):
    self.num_camelidos = self.env["coop2.camelido"].search_count([('socio_id', '=', self.id)])

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
  departamento_nac = fields.Char(string = "Departamento")
  
  #archive = os.getcwd() + '/addons/coop2/models/dep.txt'
  
  # Importar departamentos
  #with open(archive, 'r') as dptos:
  #  data = json.load(dptos)
    
  #departamentos = [ (d['departamento'], d['departamento']) for d in data ]
  #departamento_nac = fields.Selection(departamentos, string = "Departamento")

  # Otros datos
  sexo = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino')], default="masculino", string="Sexo")
  
  estado_civil = fields.Selection([
  ('soltero', 'Soltero'),
  ('casado', 'Casado'),
  ('viudo', 'Viudo'),
  ('divorciado', 'Divorciado'),
  ], default="soltero", string="Estado Civil")
  
  # Campo relacional al historial del socio
  historial = fields.One2many('coop2.historial', 'socio_id', string="Historial")
  
  # Domicilio
  dom_permanente = fields.Char(size=30)
  dom_transitorio = fields.Char(size=30)
  
  num = [(x, str(x)) for x in range(1, 20)]
  personas_nucleo = fields.Selection(num, string="Personas nucleo familiar")
  

	## CAMPOS AGREGADOS DEBIDO AL DOCUMENTO #### 

  @api.one
  @api.depends('num_hijos_1', 'num_hijos_2', 'num_hijos_3', 'num_hijos_4', 'num_hijos_5')
  def calc_hijos(self):
    self.num_hijos_total = self.num_hijos_1 + self.num_hijos_2 + self.num_hijos_3 + self.num_hijos_4 + self.num_hijos_5


  num = [(x, str(x)) for x in range(1, 10)]
  num_hijos_1 = fields.Selection(num, string="Hijos de 0 a 5 años")
  num_hijos_2 = fields.Selection(num, string="Hijos de 6 a 10 años")
  num_hijos_3 = fields.Selection(num, string="Hijos de 11 a 15 años")
  num_hijos_4 = fields.Selection(num, string="Hijos de 16 a 20 años")
  num_hijos_5 = fields.Selection(num, string="Hijos de 21 años a más")
  
  num_hijos_total = fields.Integer(string="Total hijos", compute="calc_hijos")
  
  
  ###################################################
  ##### CAMPOS PARA LAS ESTADISTICAS
  ###################################################  
  
  # Obtencion de la data por cada potrero

  @api.one
  @api.depends('cabanas.parcelas.potreros.suri')
  def cont_suri(self):
    ptrs = self.env["coop2.potrero"].search([('socio_id', '=', self.id)])
    acc = 0
    for rec in ptrs:
      acc = acc + rec.suri
    self.suri_total = acc

  @api.one
  @api.depends('cabanas.parcelas.potreros.huacaya')
  def cont_huacaya(self):
    ptrs = self.env["coop2.potrero"].search([('socio_id', '=', self.id)])
    acc = 0
    for rec in ptrs:
      acc = acc + rec.huacaya
    self.huacaya_total = acc

  @api.one
  @api.depends('cabanas.parcelas.potreros.alp_macho_adulto')
  def cont_macho_adulto(self):
    ptrs = self.env["coop2.potrero"].search([('socio_id', '=', self.id)])
    acc = 0
    for rec in ptrs:
      acc = acc + rec.alp_macho_adulto
    self.macho_adulto_total = acc


  @api.one
  @api.depends('cabanas.parcelas.potreros.alp_hembra_adulto')
  def cont_hembra_adulto(self):
    ptrs = self.env["coop2.potrero"].search([('socio_id', '=', self.id)])
    acc = 0
    for rec in ptrs:
      acc = acc + rec.alp_hembra_adulto
    self.hembra_adulto_total = acc


  @api.one
  @api.depends('cabanas.parcelas.potreros.tui_macho')
  def cont_tui_macho(self):
    ptrs = self.env["coop2.potrero"].search([('socio_id', '=', self.id)])
    acc = 0
    for rec in ptrs:
      acc = acc + rec.tui_macho
    self.tui_macho_total = acc

  @api.one
  @api.depends('cabanas.parcelas.potreros.tui_hembra')
  def cont_tui_hembra(self):
    ptrs = self.env["coop2.potrero"].search([('socio_id', '=', self.id)])
    acc = 0
    for rec in ptrs:
      acc = acc + rec.tui_hembra
    self.tui_hembra_total = acc


  @api.one
  @api.depends('cabanas.parcelas.potreros.alp_hembra')
  def cont_hembra(self):
    ptrs = self.env["coop2.potrero"].search([('socio_id', '=', self.id)])
    acc = 0
    for rec in ptrs:
      acc = acc + rec.alp_hembra
    self.alp_hembra_total = acc


  @api.one
  @api.depends('cabanas.parcelas.potreros.menores')
  def cont_menores(self):
    ptrs = self.env["coop2.potrero"].search([('socio_id', '=', self.id)])
    acc = 0
    for rec in ptrs:
      acc = acc + rec.menores
    self.menores_total = acc


  @api.one
  @api.depends('cabanas.parcelas.potreros.total_alpacas_raza')
  def cont_alpacas(self):
    ptrs = self.env["coop2.potrero"].search([('socio_id', '=', self.id)])
    acc = 0
    for rec in ptrs:
      acc = acc + rec.total_alpacas_raza
    self.alpacas_total = acc

  suri_total = fields.Integer(string="Alpacas Suri", compute="cont_suri")
  huacaya_total = fields.Integer(string="Alpacas Huacaya", compute="cont_huacaya")

  macho_adulto_total = fields.Integer(string="Alpacas Macho adulto", compute="cont_macho_adulto")
  hembra_adulto_total = fields.Integer(string="Alpacas Hembra adulto", compute="cont_hembra_adulto")
  tui_macho_total = fields.Integer(string="Tui macho", compute="cont_tui_macho")
  tui_hembra_total = fields.Integer(string="Tui hembra", compute="cont_tui_hembra")

  alp_hembra_total = fields.Integer(string="Alpacas Hembra", compute="cont_hembra")
  
  menores_total = fields.Integer(string="Menores", compute="cont_menores")
  
  alpacas_total = fields.Integer(string="Total alpacas", compute="cont_alpacas")
  

