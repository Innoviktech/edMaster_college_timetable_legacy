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



from odoo import models, fields,api, _
import logging



class OpSession(models.Model):
    _inherit = 'op.session'

    year_id = fields.Many2one(
        'op.college.year', 'Year', required=True)
    alter_faculty_id = fields.Many2one('op.faculty', 'Alternative Faculty')
    course_id = fields.Many2one(
        'op.course', 'Semester',domain = "[('year_id','=',year_id)]", required=True)

    @api.onchange('subject_id')
    def onchange_subject(self):
        if self.subject_id.name:
            subject_ids = self.env['op.faculty'].search([
                ('faculty_subject_ids.name', '=', self.subject_id.name)])
            return {
                'domain': {'alter_faculty_id': [('id', 'in', subject_ids.ids)]}}
        return {'domain': {'alter_faculty_id': []}}

