
from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    is_dealer = fields.Boolean('Is a Dealer')
    dealer_code = fields.Char('Dealer Code')
    branch_id = fields.Many2one('res.company', 'Branch/Company')
    sales_executive_id = fields.Many2one('hr.employee', 'Assigned Sales Executive')
