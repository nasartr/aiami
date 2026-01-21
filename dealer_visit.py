
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models

class DealerVisit(models.Model):
    _name = 'dealer.visit'
    _description = 'Dealer Field Visit'
    _order = 'visit_date desc, id desc'

    name = fields.Char(default='New', copy=False)
    visit_date = fields.Date(required=True, default=fields.Date.context_today)
    branch_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    employee_id = fields.Many2one('hr.employee', string='Sales Executive', required=True)
    dealer_id = fields.Many2one('res.partner', string='Dealer', domain="[('is_dealer','=',True)]", required=True)

    q3_target = fields.Float(string='Q-3 Target')
    q3_till_date_achievement = fields.Float(string='Q-3 Till Date Achievement', compute='_compute_achievements', store=False)
    month_target_lifting = fields.Float(string='Month Target (LIFTING)')
    month_till_date_achievement_lifting = fields.Float(string='Till Date Achievement (LIFTING)', compute='_compute_achievements', store=False)
    today_lifting_plan = fields.Float(string="Today's Lifting Plan")
    today_achievement_lifting = fields.Float(string="Today's Achievement (Lifting)")

    branch_activity_details = fields.Text(string="Details in branch todays activity")
    visit_activity_details = fields.Text(string='Details of Visit Activities')

    order_collection = fields.Float(string='Order collection')
    todays_customer_inquiry = fields.Integer(string="Today's Customer Inquiry (Number)")
    dealer_today_physical_stock = fields.Float(string="Dealer Today's Physical Stock")
    dealer_today_retail = fields.Float(string="Dealer Today's Retail")
    dealer_till_date_retail = fields.Float(string='Dealer Till Date Retail')

    @api.onchange('dealer_id')
    def _onchange_dealer(self):
        for rec in self:
            if rec.dealer_id:
                if rec.dealer_id.branch_id:
                    rec.branch_id = rec.dealer_id.branch_id
                if rec.dealer_id.sales_executive_id:
                    rec.employee_id = rec.dealer_id.sales_executive_id

    @api.depends('dealer_id','visit_date')
    def _compute_achievements(self):
        MoveLine = self.env['stock.move.line']
        qty_field = None
        if 'qty_done' in MoveLine._fields:
            qty_field = 'qty_done'
        elif 'quantity_done' in MoveLine._fields:
            qty_field = 'quantity_done'
        elif 'product_uom_qty' in MoveLine._fields:
            qty_field = 'product_uom_qty'

        for rec in self:
            rec.q3_till_date_achievement = 0.0
            rec.month_till_date_achievement_lifting = 0.0
            if not rec.dealer_id or not rec.visit_date or not qty_field:
                continue

            dt = fields.Date.to_date(rec.visit_date)
            month_start = dt.replace(day=1)
            month_end = (month_start + relativedelta(months=1, days=-1))
            q3_start = date(dt.year, 7, 1)
            q3_end = date(dt.year, 9, 30)

            base = [
                ('picking_id.state', '=', 'done'),
                ('picking_id.picking_type_id.code', '=', 'outgoing'),
                ('picking_id.partner_id', '=', rec.dealer_id.id),
            ]
            dom_month = base + [
                ('picking_id.date_done', '>=', month_start),
                ('picking_id.date_done', '<=', month_end),
            ]
            dom_q3 = base + [
                ('picking_id.date_done', '>=', q3_start),
                ('picking_id.date_done', '<=', q3_end),
            ]

            lines_m = MoveLine.search(dom_month)
            lines_q3 = MoveLine.search(dom_q3)

            month_qty = sum(q for q in lines_m.mapped(qty_field) if q and q > 0)
            q3_qty = sum(q for q in lines_q3.mapped(qty_field) if q and q > 0)

            rec.month_till_date_achievement_lifting = month_qty
            rec.q3_till_date_achievement = q3_qty

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals.get('name') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('dealer.visit') or 'New'
        return super().create(vals_list)
