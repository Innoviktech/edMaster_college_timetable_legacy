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
import datetime
import pytz
import time

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging

class GenerateSessionLine(models.TransientModel):
    _inherit = 'gen.time.table.line'

    chapter_ids = fields.Many2many('op.chapter',string='Chapter',domain="[('subject_id','=',subject_id)]",required=False)
    lesson_ids = fields.Many2many('op.lesson',string='Lesson',required=False)
    activity_id = fields.Many2one('op.activity.type',string='Activity',required=False)


class GenerateSession(models.TransientModel):
    _inherit = 'generate.time.table'

    @api.multi
    def act_gen_time_table(self):
        for session in self:
            start_date = datetime.datetime.strptime(
                session.start_date, '%Y-%m-%d')
            end_date = datetime.datetime.strptime(session.end_date, '%Y-%m-%d')

            for n in range((end_date - start_date).days + 1):
                curr_date = start_date + datetime.timedelta(n)
                for line in session.time_table_lines:
                    if int(line.day) == curr_date.weekday():
                        hour = line.timing_id.hour
                        if line.timing_id.am_pm == 'pm' and int(hour) != 12:
                            hour = int(hour) + 12
                        per_time = '%s:%s:00' % (hour, line.timing_id.minute)
                        final_date = datetime.datetime.strptime(
                            curr_date.strftime('%Y-%m-%d ') +
                            per_time, '%Y-%m-%d %H:%M:%S')
                        local_tz = pytz.timezone(
                            self.env.user.partner_id.tz or 'GMT')
                        local_dt = local_tz.localize(final_date, is_dst=None)
                        utc_dt = local_dt.astimezone(pytz.utc)
                        utc_dt = utc_dt.strftime("%Y-%m-%d %H:%M:%S")
                        curr_start_date = datetime.datetime.strptime(
                            utc_dt, "%Y-%m-%d %H:%M:%S")
                        curr_end_date = curr_start_date + datetime.timedelta(
                            hours=line.timing_id.duration)
                        self.env['op.session'].create({
                            'faculty_id': line.faculty_id.id,
                            'subject_id': line.subject_id.id,
                            'chapter_ids': [(6, 0, line.chapter_ids.ids)],
                            'lesson_ids': [(6, 0, line.lesson_ids.ids)],
                            'activity_id': line.activity_id.id,
                            'year_id': session.year_id.id,
                            'course_id': session.course_id.id,
                            'batch_id': session.batch_id.id,
                            'timing_id': line.timing_id.id,
                            'classroom_id': line.classroom_id.id,
                            'start_datetime':
                            curr_start_date.strftime("%Y-%m-%d %H:%M:%S"),
                            'end_datetime':
                            curr_end_date.strftime("%Y-%m-%d %H:%M:%S"),
                            'type': calendar.day_name[int(line.day)],
                        })
            return {'type': 'ir.actions.act_window_close'}

