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

from datetime import datetime
from datetime import timedelta

from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

from odoo import models, fields, api, _


class SessionReport(models.TransientModel):
    _inherit = 'time.table.report'

    year_id = fields.Many2one(
        'op.college.year', 'Year', required=True)

    @api.multi
    def gen_time_table_report(self):
        time_table_report = super(SessionReport, self).gen_time_table_report()
        template = self.env.ref(
                'openeducat_timetable.report_teacher_timetable_generate')
        data = self.read(
            ['start_date', 'end_date', 'year_id', 'course_id', 'batch_id', 'state',
             'faculty_id'])[0]
        if data['state'] == 'student':
            time_table_ids = self.env['op.session'].search(
                [('year_id', '=', data['year_id'][0]),
                 ('course_id', '=', data['course_id'][0]),
                 ('batch_id', '=', data['batch_id'][0]),
                 ('start_datetime', '>=', data['start_date']),
                 ('end_datetime', '<=', data['end_date'])],
                order='start_datetime asc')
            data.update({'time_table_ids': time_table_ids.ids})
            template = self.env.ref(
                'openeducat_timetable.report_student_timetable_generate')
        else:
            teacher_time_table_ids = self.env['op.session'].search(
                [('start_datetime', '>=', data['start_date']),
                 ('end_datetime', '<=', data['end_date']),
                 ('faculty_id', '=', data['faculty_id'][0])],
                order='start_datetime asc')
            data.update({'teacher_time_table_ids': teacher_time_table_ids.ids})
        return template.report_action(self, data=data)
