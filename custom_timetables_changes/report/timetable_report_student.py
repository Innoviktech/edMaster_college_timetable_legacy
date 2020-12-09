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
import time
from datetime import datetime

import pytz

from odoo import models, api, _


class ReportTimetableStudentGenerate(models.AbstractModel):
    _inherit = 'report.openeducat_timetable.report_timetable_student_generate'

    @api.multi
    def _convert_to_local_timezone(self, time):
        '''
            Converts time as per local timezone.
        '''
        if time:
            tz_name = self._context['tz'] or self.env.user.tz
            timezone = tz_name and pytz.timezone(tz_name) or pytz.UTC
            utc_in_time = pytz.utc.localize(
                datetime.strptime(time, "%Y-%m-%d %H:%M:%S"))
            local_time = utc_in_time.astimezone(timezone)
            return local_time

    def get_object(self, data):

        data_list = []
        for timetable_obj in self.env['op.session'].browse(
                data['time_table_ids']):

            oldDate = datetime.strptime(
                timetable_obj.start_datetime, "%Y-%m-%d %H:%M:%S")
            day = datetime.weekday(oldDate)

            timetable_data = {
                'period': timetable_obj.timing_id.name,
                'sequence': timetable_obj.timing_id.sequence,
                'start_datetime': self._convert_to_local_timezone(
                    timetable_obj.start_datetime).strftime(
                    "%Y-%m-%d %H:%M:%S"),
                'day': str(day),
                'subject': timetable_obj.subject_id.name,
                'faculty': timetable_obj.faculty_id.name,
            }
            data_list.append(timetable_data)
        ttdl = sorted(data_list, key=lambda k: k['sequence'])
        final_list = self.sort_tt(ttdl)
        return final_list