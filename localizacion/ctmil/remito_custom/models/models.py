from odoo import fields, osv, models, api
from odoo.exceptions import UserError, ValidationError

class BelshStockPicking(models.Model):
	_inherit = "stock.picking"

	@api.multi
	def _barrels_stock(self):
		barrels_ids = self.env['stock.production.lot'].search([('product_id', '=', 159)])
		quant_ids = []
		locs = []

		if barrels_ids:
			for rec in self:
				for barrel in barrels_ids:
					if barrel.quant_ids:
						quant_ids.append(barrel.quant_ids)

				if quant_ids:
					for qids in quant_ids:
						for qid in qids:
							if qid.location_id == 9:
								locs.append(qid.location_id)
				raise ValidationError(locs)
		else:
			for rec in self:
				rec.barril = ''

	barril = fields.Char('Barriles', compute=_barrels_stock)

