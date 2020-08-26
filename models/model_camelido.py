from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import datetime, timedelta

class camelido_andino(models.Model):
  _name = "coop2.camelido"
  _description = "Camelido Andino"
  _rec_name = "nombre_camelido"
  
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
      

  nombre_camelido = fields.Char(string="Nombre", required=True)
  fecha_empadre = fields.Date(string="Fecha de empadre")
  fecha_nac = fields.Date(string="Fecha de naciomiento")
  edad = fields.Integer(string="Edad", compute="calcula_edad", store=True)
  
  # Tipo de identificacion
  tipo_identificacion = fields.Selection([
    ('tatuaje', 'Tatuaje'),
    ('arete', 'Arete'),
    ('senal', 'Señal'),
    ('otro', 'Otro'),
  ], default="tatuaje", string="Tipo de identificación")

  identificacion = fields.Char(string="Número")
  
  # Antepasados
  #cod_padre = fields.Char(string="Código del padre")
  #cod_madre = fields.Char(string="Código de la madre")
  #cod_abuelo = fields.Char(string="Código del abuelo")
  #cod_abuela = fields.Char(string="Código de la abuela")
  #cod_bisabuelo = fields.Char(string="Código del bisabuelo")
  #cod_bisabuela = fields.Char(string="Código de la bisabuela")
  
  # Campos relacionales
  cod_padre = fields.Many2one('coop2.camelido', string="Código del padre")
  cod_madre = fields.Many2one('coop2.camelido', string="Código de la madre")
  cod_abuelo = fields.Many2one('coop2.camelido', string="Código del abuelo")
  cod_abuela = fields.Many2one('coop2.camelido', string="Código de la abuela")
  cod_bisabuelo = fields.Many2one('coop2.camelido', string="Código del bisabuelo")
  cod_bisabuela = fields.Many2one('coop2.camelido', string="Código de la bisabuela")
#  socio_id = fields.Many2one('coop2.socio', string="Socio Propietario", required = True)
  
  sexo = fields.Selection([
    ('masculino', 'Masculino'),
    ('femenino', 'Femenino'),
  ], default="masculino", string="Sexo")
  
  raza = fields.Char(string="Raza")
  color = fields.Char(string="Color")
  categoria = fields.Char(string="Categoria")

  esquila = fields.Selection([
    ('si', 'Sí'),
    ('no', 'No'),
  ], default="no", string="Esquila")
  num_esquila = fields.Integer(string="Número de esquila")

# Caracteristicas del Vellon
  # Propiedades fisicas
  diametro = fields.Float(string="Diámetro")
  longitud_mecha = fields.Float(string="Longitud de mecha")
  rizo_ondulacion = fields.Float(string="Rizo o ondulación")
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
  potrero_id = fields.Many2one('coop2.potrero', string="Potrero")
  
  
  # obtencion del socio
  nombre_socio = fields.Char(string="Socio", compute="get_socio")
