from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    product_id = fields.Many2one(
        'product.product',
        string="Product"
    )
