
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    student_name = fields.Char(string='Student Name')

class student(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'student record'
    _rec_name = 'student_name'

    @api.constrains('student_age')
    def check_age(self):
        for rec in self:
            if rec.student_age <=5:
                raise ValidationError(_('The Age Must be Greater than 5.'))

    @api.depends('student_age')
    def set_age_group(self):
        for rec in self:
            if rec.student_age < 18:
                rec.age_group = 'minor'
            else:
                rec.age_group = 'major'


    name = fields.Char(string='Test')
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))


    gender= fields.Selection([
        ('male','Male'),
        ('fe_male','Female'),],default='male',string="Gender")
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'), ], string="Age Group",compute='set_age_group')
    student_name = fields.Char(string='Name', required='True', track_visibility='always')
    student_age = fields.Integer("Age", track_visibility='always')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')



    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('school.student.sequence') or _('New')
        result = super(student,self).create(vals)
        return result