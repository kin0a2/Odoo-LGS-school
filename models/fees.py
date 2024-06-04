from odoo import models, fields, api, _

class SchoolFees(models.Model):
    _name = 'school.fees'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Fees'
    _rec_name = 'name'

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('school.fees') or _('New')
        return super(SchoolFees, self).create(vals)

    name_seq = fields.Char(string='Sequence', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: ('New'))

    name = fields.Char(string='name', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))

    student_id = fields.Many2one('school.student', string='Student ID', required=True)
    student_age = fields.Integer("Age")
    notes = fields.Text(string='Admission Notes')
    admission_date = fields.Date(string='Date', required=True)

