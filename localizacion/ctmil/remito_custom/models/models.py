from odoo import fields, osv, models, api
from odoo.exceptions import UserError, ValidationError

class BelshStockPicking(models.Model):
	_inherit = "stock.picking"

	@api.multi
	def _barrels_stock(self):
		barrels_ids = self.env['stock.production.lot'].search([('product_id', '=', 159)])
		nro_barril = ''
		table = ''
		quant_ids = []
		locs = []
		history = []
		barrel_data = []

		if barrels_ids:
			for rec in self:
				for barrel in barrels_ids:
					nro_barril = barrel.name
					if barrel.quant_ids:
						quant_ids.append(barrel.quant_ids)

					if quant_ids:
						for qids in quant_ids:
							for qid in qids:
								if qid.location_id.id == 9:
									locs.append(qid)

					if locs:
						for his in locs:
							history.append(his.history_ids)

					if history:
						for res in history:
							for h_res in res:
								if h_res[-1].location_dest_id.id == 9:
									barrel_data.append(h_res[-1])

					if barrel_data:
						if barrel_data.partner_id == rec.partner_id:
							table = '<table><tr><th>Orden de Venta</th><th>Nro Factura</th><th>Fecha Factura</th><th>Nro Remito</th><th>Nro Barril</th><th>Antiguedad</th><th>Retira</th><th>Firma</th></tr>'
							table = table + '<tr><td>' + str(b.origin) + '</td><td> </td><td> </td><td>' + str(b.picking_id.name) + '</td><td>' + str(nro_barril) + '</td><td></td><td> </td><td> </td></tr>'

							rec.barril = table + '</table>'
					else:
						rec.barril = ''

		else:
			for rec in self:
				rec.barril = ''

	barril = fields.Html('Barriles', compute=_barrels_stock)

