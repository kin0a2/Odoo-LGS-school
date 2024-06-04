from odoo import models, fields, api, _

class SchoolAdmission(models.Model):
    _name = 'school.admission'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Admission'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('school.admission') or _('New')
        result = super(SchoolAdmission, self).create(vals)
        return result

    name_seq = fields.Char(string='Sequence', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: ('New'))

    name = fields.Char(string='name', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))

    student_id = fields.Many2one('school.student', string='Student ID', required=True)
    student_age = fields.Integer("Age")
    notes = fields.Text(string='Admission Notes')
    admission_date = fields.Date(string='Date', required=True)
