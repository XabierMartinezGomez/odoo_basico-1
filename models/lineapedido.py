# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lineapedido(models.Model):
     _name = 'odoo_basico.lineapedido' # Será o nome da táboa
     _description = ' modelo lineapedidos'

     descripcion_da_lineapedido = fields.Text(string="A descripción")
     # Os campos Many2one crean un campo na BD
     pedido_id = fields.Many2one('odoo_basico.pedido',ondelete="cascade", required=True)