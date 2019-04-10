from odoo import fields, osv, models, api
from odoo.exceptions import UserError, ValidationError

class BelshStockPicking(models.Model):
	_inherit = "stock.picking"

	@api.multi
	def _barrels_stock(self):
		barrels_ids = self.env['stock.production.lot'].search([('product_id', '=', 159)])
		if barrels_ids:
			raise ValidationError(barrels_ids)
		else:
			raise ValidationError('Testing Compute')

	barril = fields.Char('Barriles', compute=_barrels_stock)

