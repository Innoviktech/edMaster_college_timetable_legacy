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

from odoo import models, fields,api


class OpTiming(models.Model):
    _inherit = 'op.timing'


    hour = fields.Selection(
        [('0','0'),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
         ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
         ('11', '11'), ('12', '12')], 'Start Hours', required=True)

    minute = fields.Selection(
        [('00', '00'), ('05', '05'),('10', '10'), ('15', '15'), ('20', '20'),
         ('25', '25'), ('30', '30'), ('35', '35'), ('40', '40'), ('45', '45'),
         ('50', '50'), ('55', '55'), ('60', '60')], 'Start Minute',
        required=True)
    end_hour = fields.Selection(
        [('0','0'),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
         ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
         ('11', '11'), ('12', '12')], 'End Hours', required=True)

    end_minute = fields.Selection(
        [('00', '00'), ('05', '05'),('10', '10'), ('15', '15'), ('20', '20'),
         ('25', '25'), ('30', '30'), ('35', '35'), ('40', '40'), ('45', '45'),
         ('50', '50'), ('55', '55'), ('60', '60')], 'End Minute',
        required=True)
    pm_am = fields.Selection(
        [('am', 'AM'), ('pm', 'PM')], 'AM/PM', required=True)

    duration = fields.Float(compute = '_compute_duration', string='Duration')

    def _compute_duration(self):
         for record in self:

             if record.am_pm == 'am' and record.pm_am == 'am':
                 record.duration = ((((float(record.end_hour)) + (float(record.end_minute) / 60)) -
                                     (float(record.hour) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'am' and record.pm_am == 'am' and record.hour == '12':
                 record.duration = ((((float(record.end_hour) + (float(record.end_minute) / 60)) -
                                      (float(record.hour) - float('12')) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'am' and record.pm_am == 'am' and record.hour == '12' and record.end_hour == '12':
                 record.duration = ((((float(record.end_hour) + (float(record.end_minute) / 60)) -
                                      (float(record.hour)) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'am' and record.pm_am == 'pm':
                 record.duration = ((((float(record.end_hour) + float('12')) + (float(record.end_minute) / 60)) -
                                     (float(record.hour) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'am' and record.pm_am == 'pm' and record.end_hour == '12':
                 record.duration = ((((float(record.end_hour)) + (float(record.end_minute) / 60)) -
                                     (float(record.hour) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'am' and record.pm_am == 'pm' and record.end_hour == '12' and record.end_hour == '12':
                 record.duration = ((((float(record.end_hour)) + (float(record.end_minute) / 60)) -
                                     (float(record.hour) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'pm' and record.pm_am == 'pm':
                 record.duration = ((((float(record.end_hour)) + (float(record.end_minute) / 60)) -
                                     (float(record.hour) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'pm' and record.pm_am == 'pm' and record.hour == '12':
                 record.duration = ((((float(record.end_hour) + (float(record.end_minute) / 60)) -
                                      (float(record.hour) - float('12')) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'pm' and record.pm_am == 'pm' and record.hour == '12' and record.end_hour == '1':
                 record.duration = ((((float(record.end_hour) + float('12') + (float(record.end_minute) / 60)) -
                                      (float(record.hour)) - (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'pm' and record.pm_am == 'pm' and record.hour == '12' and record.end_hour == '12':
                 record.duration = ((((float(record.end_hour) + (float(record.end_minute) / 60)) -
                                      (float(record.hour)) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'pm' and record.pm_am == 'am':
                 record.duration = ((((float(record.end_hour) + float('12')) + (float(record.end_minute) / 60)) -
                                     (float(record.hour) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'pm' and record.pm_am == 'am' and record.end_hour == '12':
                 record.duration = ((((float(record.end_hour)) + (float(record.end_minute) / 60)) -
                                     (float(record.hour) + (float(record.minute) / 60))) * 60) / 60

             if record.am_pm == 'pm' and record.pm_am == 'am' and record.end_hour == '12' and record.end_hour == '12':
                 record.duration = ((((float(record.end_hour)) + (float(record.end_minute) / 60)) -
                                     (float(record.hour) - float('12') + (float(record.minute) / 60))) * 60) / 60
             # if record.am_pm == 'pm' and record.pm_am == 'am' and record.end_hour == '12' and record.end_hour == '12':
             #     record.duration = ((((float(record.end_hour)) + (float(record.end_minute) / 60)) -
             #                         (float(record.hour) - float('12') + (float(record.minute) / 60))) * 60) / 60








