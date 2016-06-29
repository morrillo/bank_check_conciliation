# -*- coding: utf-8 -*-
from openerp import models, api, fields


class account_bank_statement_line(models.Model):
	_inherit = "account.bank.statement.line"

	check_id = fields.Many2one('account.check',domain=[('state','in',[('holding')])
