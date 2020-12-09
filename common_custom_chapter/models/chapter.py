import datetime
from odoo import models, fields, api, _
import logging


class Chapter(models.Model):
    _name = "op.chapter"
    _rec_name = 'chapter_name'

    chapter_name = fields.Char('Name', size=128, required=True)
    chapter_code = fields.Char('Code', size=256, required=True)
    subject_id = fields.Many2one('op.subject', 'Subject', required=True)
    lesson_ids = fields.One2many('op.lesson','chapter_id',string='Lesson(s)')
