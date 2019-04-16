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
					quants_ids = []
					locs = []
					barrel_data = []
					nro_barril = barrel.name
					if barrel.quant_ids:
						quant_ids.append(barrel.quant_ids)

					if quant_ids:
						if quant_ids[-1][-1].location_id.id == 9:
							locs.append(quant_ids[-1][-1].history_ids[-1])

					if locs:
						if locs[-1].location_dest_id.id == 9:
							barrel_data.append(locs[-1])

					if barrel_data:
						#if rec.partner_id.id == barrel_data[0].partner_id.id
						table = table + " " + str(barrel_data[0].origin)
					"""if barrel_data:
						if barrel_data.partner_id == rec.partner_id:
							table = '<table><tr><th>Orden de Venta</th><th>Nro Factura</th><th>Fecha Factura</th><th>Nro Remito</th><th>Nro Barril</th><th>Antiguedad</th><th>Retira</th><th>Firma</th></tr>'
							table = table + '<tr><td>' + str(b.origin) + '</td><td> </td><td> </td><td>' + str(b.picking_id.name) + '</td><td>' + str(nro_barril) + '</td><td></td><td> </td><td> </td></tr>'

							rec.barril = table + '</table>'
					else:
						rec.barril = ''"""
				if table:
					rec.barril = table
		else:
			for rec in self:
				rec.barril = ''

	barril = fields.Html('Barriles', compute=_barrels_stock)
