
from odoo import fields, models

class ExecVisitReportWizard(models.TransientModel):
    _name = 'exec.visit.report.wizard'
    _description = 'Executive-wise Field Visit Report Wizard'

    date_from = fields.Date(required=True, default=lambda self: fields.Date.context_today(self).replace(day=1))
    date_to = fields.Date(required=True, default=fields.Date.context_today)
    branch_id = fields.Many2one('res.company', string='Branch/Company')
    employee_ids = fields.Many2many('hr.employee', string='Sales Executives')

    def _get_lines(self):
        domain=[('visit_date','>=',self.date_from),('visit_date','<=',self.date_to)]
        if self.branch_id:
            domain.append(('branch_id','=',self.branch_id.id))
        if self.employee_ids:
            domain.append(('employee_id','in',self.employee_ids.ids))
        visits=self.env['dealer.visit'].search(domain, order='branch_id, employee_id, dealer_id, visit_date')
        res=[]
        for v in visits:
            res.append({
                'branch': v.branch_id.name,
                'employee': v.employee_id.name,
                'dealer': v.dealer_id.name,
                'visit_date': v.visit_date,
                'q3_target': v.q3_target,
                'q3_ach': v.q3_till_date_achievement,
                'month_target': v.month_target_lifting,
                'month_ach': v.month_till_date_achievement_lifting,
                'today_plan': v.today_lifting_plan,
                'today_ach': v.today_achievement_lifting,
                'branch_det': v.branch_activity_details,
                'visit_det': v.visit_activity_details,
                'order_collection': v.order_collection,
                'inquiries': v.todays_customer_inquiry,
                'stock_today': v.dealer_today_physical_stock,
                'retail_today': v.dealer_today_retail,
                'retail_ttd': v.dealer_till_date_retail,
            })
        return res

    def action_print(self):
        return self.env.ref('fd_dealer_mgmt_fixed10.action_exec_visit_report').report_action(self)
