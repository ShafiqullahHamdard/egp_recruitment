from odoo import api, fields, models

class EgpHrInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    reward_ids = fields.One2many('employee.reward', 'employee_id', string='Publication')

    rewards_type = fields.Char(string='Reward Type')
    reason_for_sentence = fields.Char(string='Reason of issuing sentence')
    date_of_sentence = fields.Char(string='Date of the Sentence')
    order_no = fields.Char(string='No of Sentence')


# Your Python code (e.g., in a controller or model)

class EmployeeReward(models.Model):
    _name = 'employee.reward'
    _description = 'publication'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    rewards_type = fields.Char(string='Reward Type')
    reason_for_sentence = fields.Char(string='Reason of issuing sentence')
    date_of_sentence = fields.Char(string='Date of the Sentence')
    order_no = fields.Char(string='No of Sentence')