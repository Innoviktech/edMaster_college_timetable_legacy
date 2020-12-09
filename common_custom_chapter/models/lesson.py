import datetime
from odoo import models, fields, api, _
import logging


class Lesson(models.Model):
    _name = "op.lesson"
    _rec_name = 'lesson_name'

    lesson_name = fields.Char('Name', size=128, required=True)
    lesson_code = fields.Char('Code', size=256, required=True)
    chapter_id = fields.Many2one('op.chapter', 'Chapter', required=True)
