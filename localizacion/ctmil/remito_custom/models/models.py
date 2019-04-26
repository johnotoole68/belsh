import datetime
from datetime import date

from odoo import fields, osv, models, api
from odoo.exceptions import UserError, ValidationError

class BelshStockPicking(models.Model):
	_inherit = "stock.picking"

	@api.multi
	def _barrels_stock(self):
		barrels_ids = self.env['stock.production.lot'].search([('product_id', '=', 159)])
		nro_barril = ''
		table = ''

		if barrels_ids:
			for rec in self:
				for barrel in barrels_ids:
					quant_ids = []
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
						if rec.partner_id.id == barrel_data[0].partner_id.id:
							account = self.env['account.invoice'].search([('origin', '=', barrel_data[0].origin)])
							inv_num = ''
							date_invoice = ''
							days = ''
							if account:
								inv_num = account.document_number
								date_invoice = account.date_invoice
								delta = date.today() - date_invoice
								days = str(delta.days)

							table = table + '<tr><td>' + str(barrel_data[0].origin) + '</td><td>' + inv_num + '</td><td>' + str(date_invoice) + '</td><td>' + str(barrel_data[0].picking_id.name) + '</td><td>' + str(nro_barril) + '</td><td>' + days + '</td><td> </td><td> </td></tr>'

				if table:
					rec.barril = '<table style="width:100%;" class="table table-bordered"><thead><tr><th>Orden de Venta</th><th>Nro Factura</th><th>Fecha Factura</th><th>Nro Remito</th><th>Nro Barril</th><th>Antiguedad</th><th>Retira</th><th>Firma</th></tr></thead><tbody>' + table + '</tbody></table>'
		else:
			for rec in self:
				rec.barril = ''

	barril = fields.Html('Barriles', compute=_barrels_stock)