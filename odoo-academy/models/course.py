# -*- coding:utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    
    _name = 'academy.course'
    _description = "Course Info"
    
    name = fields.Char(string='Title', required=True)
    description= fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    