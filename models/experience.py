# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    experience_ids = fields.One2many('employee.experience', 'employee_id', string='experience')

    organization = fields.Char(string='Organization')
    job_position = fields.Char(string='Job Position')
    grade = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'),
                              ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], string="Grade")
    step = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'),
                             ('5th', '5th')], string="Step")

    job_location = fields.Char(string='Job Location')
    department = fields.Char(string='Department')
    status = fields.Char(string='Status')
    job_start_date = fields.Date(string='Start Date')
    job_end_date = fields.Date(string='End Date')
    # service_duration = fields.Char(string='Service Duration')

    duration_days = fields.Integer('Duration Days (Days)', compute='_compute_duration_days', store=True)

    @api.depends('job_start_date', 'job_end_date')
    def _compute_duration_days(self):
        for record in self:
            if record.job_start_date and record.job_end_date:
                delta = record.job_end_date - record.job_start_date
                record.duration_days = delta.days
                # record.duration_years = delta.days
                # record.duration_months = delta.months
            else:
                record.duration_days = 0
                # record.duration_months = 0


# Your Python code (e.g., in a controller or model)

class EmployeeExperience(models.Model):
    _name = 'employee.experience'
    _description = 'Employee Experience'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    organization = fields.Char(string='Organization')
    job_position = fields.Char(string='Job Position')
    grade = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'),
                              ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], string="Grade")
    step = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'),
                             ('5th', '5th')], string="Step")

    job_location = fields.Char(string='Job Location')
    department = fields.Char(string='Department')
    status = fields.Char(string='Status')
    job_start_date = fields.Date(string='Start Date')
    job_end_date = fields.Date(string='End Date')
    # service_duration = fields.Char(string='Service Duration')

    duration_days = fields.Integer('Duration Days (Days)', compute='_compute_duration_days', store=True)













