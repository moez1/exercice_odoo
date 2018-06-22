# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo import tools, _
from odoo import exceptions

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    #Surcharge la fonction create et redimensionner la taille de l'image 
    @api.model 
    def create(self, vals):
        tools.image_resize_images(vals) 
        return super(SaleOrder, self).create(vals)
    
    #Surcharge la fonction write et redimensionner la taille de l'image 
    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(SaleOrder, self).write(vals)
    
    #Verifier si le champ exercice est vide ou pas
    @api.constrains('exercice')   
    def _check_exercice(self):
        if not self.exercice:
            raise exceptions.ValidationError("le champ exercice est vide")
    
    exercice = fields.Text('Exercice',translate=True)
    image = fields.Binary('photo',attachment=True)
    image_medium = fields.Binary("Photo de taille moyenne", attachment=True,)
    image_small = fields.Binary("Photo de petite taille", attachment=True,)
    
  
