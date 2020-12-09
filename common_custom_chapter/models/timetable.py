# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import calendar
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OpSession(models.Model):
    _inherit = 'op.session'

    chapter_ids = fields.Many2many('op.chapter',string='Chapter',domain="[('subject_id','=',subject_id)]",required=False)
    lesson_ids = fields.Many2many('op.lesson',string='Lesson',required=False)
    activity_id = fields.Many2one('op.activity.type',string='Activity',required=False)

