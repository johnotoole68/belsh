from odoo import fields, osv, models, api
from odoo.exceptions import UserError, ValidationError

class BelshStockPicking(models.Model):
	_inherit = "stock.picking"

	@api.multi
	def _barrels_stock(self):
		#barrels_ids = self.env['stock.production.lot'].search(['product_id', '=', 159])
		raise ValidationError('Probando Computacion')
		for rec in self:
			rec.barril = 'Hola Mundo'

	barril = fields.Char('Barriles', compute=_barrels_stock)

