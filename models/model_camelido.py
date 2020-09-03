from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import datetime, timedelta

class camelido_andino(models.Model):
  _name = "coop2.camelido"
  _description = "Camelido Andino"
  _inherit = ['mail.thread', 'mail.activity.mixin'] # for Chatter
  _rec_name = "identificacion"
  
  @api.one
  @api.depends('fecha_nac')
  def calcula_edad(self):
    if self.fecha_nac is not False:
      today = datetime.today()
      nac = fields.Date.from_string(self.fecha_nac)
      self.edad = today.year - nac.year - ( (today.month, today.day) < (nac.month, nac.day) )

  # Funcion que autocompleta el campo Socio, para saber el socio dueño de la parcela
  @api.one
  @api.depends('potrero_id')
  def get_socio(self):
    if self.potrero_id is not False:
      socio = self.potrero_id.parcela_id.cabana_id.socio_id
      self.nombre_socio = socio.name
      self.socio_id = socio.id
  @api.one
  @api.depends('potrero_id')
  def get_socio_id(self):
    if self.potrero_id is not False:
      socio = self.potrero_id.parcela_id.cabana_id.socio_id
      self.socio_id = socio.id
  identificacion = fields.Char(string="Número", required=True, track_visibility="always")

  fecha_empadre = fields.Date(string="Fecha de empadre")
  fecha_nac = fields.Date(string="Fecha de naciomiento")
  edad = fields.Integer(string="Edad", compute="calcula_edad", store=True)
  
  # Tipo de identificacion
  tipo_identificacion = fields.Selection([
    ('tatuaje', 'Tatuaje'),
    ('arete', 'Arete'),
    ('senal', 'Señal'),
    ('otro', 'Otro'),
  ], default="tatuaje", string="Tipo de identificación", track_visibility="always")



  # Campos relacionales
  cod_padre = fields.Many2one('coop2.camelido', string="Código del padre", domain="[('sexo', '=', 'macho'), ('identificacion', '!=', identificacion)]" )
  cod_madre = fields.Many2one('coop2.camelido', string="Código de la madre", domain="[('sexo', '=', 'hembra'), ('identificacion', '!=', identificacion )]")
  cod_abuelo = fields.Many2one('coop2.camelido', string="Código del abuelo", domain="[('sexo', '=', 'macho'), ('identificacion', '!=', identificacion)]" )
  cod_abuela = fields.Many2one('coop2.camelido', string="Código de la abuela", domain="[('sexo', '=', 'hembra'), ('identificacion', '!=', identificacion )]")
  cod_bisabuelo = fields.Many2one('coop2.camelido', string="Código del bisabuelo", domain="[('sexo', '=', 'macho'), ('identificacion', '!=', identificacion)]")
  cod_bisabuela = fields.Many2one('coop2.camelido', string="Código de la bisabuela", domain="[('sexo', '=', 'hembra'), ('identificacion', '!=', identificacion )]")
  
  sexo = fields.Selection([
    ('macho', 'Macho'),
    ('hembra', 'Hembra'),
  ], default="macho", string="Género")
  
  raza = fields.Selection([
    ('huacayo', 'Huacayo'),
    ('suri', 'Suri'),
    ('raza 3', 'Raza 3'),
    ('raza 4', 'Raza 4'),
  ], string="Raza")
  
  color = fields.Selection([
    ('blanco', 'blanco'),
    ('color 2', 'Color 2'),
    ('color 3', 'Color 3'),
    ('color 4', 'Color 4'),
  ], string="Color")

  categoria = fields.Selection([
    ('categoria 1', 'Categoria 1'),
    ('categoria 2', 'Categoria 2'),
    ('categoria 3', 'Categoria 3'),
    ('categoria 4', 'Categoria 4'),
  ], string="Categoria")

  cond_adquisicion = fields.Selection([
    ('alquilado', 'Alquilado'),
    ('comprado', 'Comprado'),
    ('trueque', 'Trueque'),
    ('prestado', 'Prestado'),
  ], string="Condición de adquisición")

  esquila = fields.Selection([('si', 'Sí'), ('no', 'No')], default="no", string="Esquila")

  num_esquila = fields.Selection([(x, str(x)) for x in range(0, 6)], default='0', string="Número de esquila")

# Caracteristicas del Vellon
  # Propiedades fisicas
  diametro = fields.Float(string="Diámetro")
  longitud_mecha = fields.Float(string="Longitud de mecha")
  rizo_ondulacion = fields.Float(string="Rizo u ondulación")
  resistencia_tenacidad = fields.Float(string="Resistencia o tenacidad")
  lustre_brillo = fields.Float(string="Lustre o brillo")
  grasa = fields.Float(string="Grasa")
  
  categoria_vellon = fields.Selection([
    ('extrafina', 'Extrafina'),
    ('fina', 'Fina'),
    ('semifina', 'Semifina'),
    ('gruesa', 'Gruesa'),
  ], default="extrafina", string="Categoria")
  
  clasificacion_vellon = fields.Selection([
    ('baby', 'Alpaca Baby (<23um)'),
    ('fleece', 'Alpaca Fleece (23.1 a 26.5um)'),
    ('medium_fleece', 'Alpaca Medium Fleece (26.6 a 29.0um)'),
    ('huarizo', 'Alpaca Huarizo (29.1 a 31.6um)'),
    ('gruesa', 'Alpaca Gruesa (>31um)'),
    ('corta', 'Alpaca Corta'),
  ], default="baby", string="Clasificación del Vellón")
  
  # Conformacion
  cabeza = fields.Char(string="Cabeza")
  talla = fields.Char(string="Talla")
  calze = fields.Char(string="Calce")
  ap_general = fields.Char(string="Apariencia General")
  defectos = fields.Char(string="Defectos")
  
  #observaciones
  observaciones = fields.Text(string="Observaciones")
  
  
  # Campo potrero
  potrero_id = fields.Many2one('coop2.potrero', string="Potrero", track_visibility="always")
  
  
  # obtencion del socio
  nombre_socio = fields.Char(string="Socio", compute="get_socio")
  socio_id = fields.Integer(string="id", compute="get_socio_id", store=True)
