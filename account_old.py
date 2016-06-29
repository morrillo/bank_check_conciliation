# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
from openerp.tools import float_is_zero
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from openerp.report import report_sxw
from openerp.tools import float_compare, float_round

import time

class account_bank_statement(osv.osv):
	_inherit = 'account.bank.statement'

	
	def button_confirm_bank(self, cr, uid, ids, context=None):
		res = super(account_bank_statement, self).button_confirm_bank(cr, uid, ids, context=context)
		import pdb;pdb.set_trace()
		for statement_id in statement_ids:
			bank_statement = self.pool.get('account.bank.statement').browse(cr,uid,statement_id)
			for line in bank_statement.line_ids:
				if line.check_id:
					check = self.pool.get('account.check').browse(cr,uid,line.check_id.id)
					check.action_deposit()
		return res

account_bank_statement()
