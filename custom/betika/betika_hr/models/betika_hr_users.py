from odoo import api, fields, models


class Betika_leave(models.Model):
    _name = "betika.paladin"
    _description = "company name"
    name = fields.Char(string='Name', required=True)
    spouse = fields.Char(string='Spouse', required=True)
    age = fields.Integer(string='Age')
    image = fields.Binary(string=" Staff image")
    gender = fields.Selection([
       ('male', 'Male'), ('female', 'Female'), ('other', 'other')], required=True, default='male')
    note = fields.Text(string='Description')
