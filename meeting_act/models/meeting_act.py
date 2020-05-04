# -*- coding: utf-8 -*-
from odoo import api, models, fields

class MeetingAct(models.Model):
    _name = 'meeting.act'
    _inherit = ['mail.thread']

    name = fields.Char(
        string="Nombre"
    )
    date = fields.Date(
        string="Fecha"
    )
    meeting_act_category_id = fields.Many2one(
        comodel_name='meeting.act.category', 
        string='Categoría acta reunion',
    )
    description = fields.Text(
        string="Descripcion"
    )