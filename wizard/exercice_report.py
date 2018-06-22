# -*- coding: utf-8 -*-

from odoo import fields, models, _, api
from odoo.exceptions import UserError


class Exercicereport(models.TransientModel):
    _name = "exercice.report"
    _description = "Time Sheet Report"

    #Fonction compute pour chercher les ids de  sale.order.line
    @api.one
    @api.depends('sale_ids')
    def get_sale_line_ids(self):
        domain = []
        work_ids = []
        sale_ids = self.sale_ids
        
        if sale_ids:   
            for sale in sale_ids:
                domain += [('order_id','=',sale.id)]
                work_ids += [a.id for a in self.env['sale.order.line'].search(domain)]
                domain.pop()
        self.sale_line_ids = work_ids
    
    
    sale_ids = fields.Many2many('sale.order', string='Vente')
    sale_line_ids = fields.Many2many('sale.order.line', string='Resultat',compute=get_sale_line_ids,store=True)

    
    #Fonction pour imprimer le rapport 
    @api.multi
    def check_report(self):
        return self.env.ref('exercice_odoo.action_exercice_rep').report_action(self, data=None)

    