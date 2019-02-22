 # -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError
from odoo.tools.safe_eval import safe_eval

from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
import logging
_logger = logging.getLogger(__name__)


class AccountPayment(models.Model):
    _inherit = 'account.payment'

#Reporte de Pagos:
#Numero de factura - Fecha de factura - Empresa - Monto Facturado - Fecha de Pago - Diario de Pago - Monto pagado - Estado (validada, pagada, etc) -
#Provincia

#Reporte de Cobranzas: Numero de factura - Fecha de factura - Empresa - Monto Facturado - Fecha de Cobro -  Diario de Cobro -  Monto Cobrado -Estado- Provincia  (agrego este que es lo

class AccountPaymentXlsx(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, payments):

        report_name = "Pagos"

        sheet = workbook.add_worksheet(report_name[:31])
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, report_name, bold)

        headers = ['Numero de factura','Fecha de factura','Proveedor/Cliente','Empresa','Monto Facturado','Fecha de pago','Diario de pago','Monto de pago','Estado']

        index = 0
        for header in headers:
            sheet.write(3,index,header,bold)
            index = index + 1

        row_index = 4
        for obj in payments:
            invoice = False
            invoice_date = ''
            invoice_amount = ''
            invoice_state = ''
            invoice_name = ''
            partner_type = 'Cliente'
            if (obj.partner_type=='supplier'):
                partner_type = 'Proveedor'
            if (obj.communication):
                invoice_name = obj.communication
                #_logger.info(obj.invoice_ids)
                #invoice = self.env["account.invoice"].search( [ ('name','=',obj.communication) ] )
                if (obj.invoice_ids):
                    invoice = obj.invoice_ids[0]

                if (invoice==False):
                    #movelines = self.env['account.move.line'].search([('payment_id','=',obj.id)])
                    #movelines =
                    if (len(obj.move_line_ids)):
                        _logger.info(obj.move_line_ids)
                        for ml in obj.move_line_ids:
                            _logger.info(ml)
                            if (ml.invoice_id):
                                invoice = ml.invoice_id

                if (invoice):
                    if (invoice.id):
                        invoice_date = invoice.date_invoice
                        invoice_amount = invoice.amount_total
                        invoice_state = invoice.state
                        invoice_name = invoice.display_name


            sheet.write(row_index,0,invoice_name)
            sheet.write(row_index,1,invoice_date)
            sheet.write(row_index,2,partner_type)
            sheet.write(row_index,3,obj.partner_id.name)
            sheet.write(row_index,4,invoice_amount)
            sheet.write(row_index,5,obj.payment_date)
            sheet.write(row_index,6,obj.journal_id.name)
            sheet.write(row_index,7,obj.amount)
            sheet.write(row_index,8,invoice_state)
            row_index = row_index + 1

AccountPaymentXlsx('report.account.payment.xlsx','account.payment')
