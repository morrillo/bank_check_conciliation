# -*- coding: utf-8 -*-
from openerp import models, api, fields


class account_bank_statement_line(models.Model):
	_inherit = "account.bank.statement.line"

	check_id = fields.Many2one('account.check',domain=[('state','in',[('holding')])])

	@api.onchange('check_id')
	def change_check(self):
		if self.check_id.source_partner_id:
			self.partner_id = self.check_id.source_partner_id.id
		if self.check_id.amount:
			self.amount = self.check_id.amount


