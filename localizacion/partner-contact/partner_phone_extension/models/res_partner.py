# -*- coding: utf-8 -*-
# Copyright 2013-2014 Savoir-faire Linux
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    phone_extension = fields.Char('Phone Extension', oldname="extension",
                                  help="Phone Number Extension.")
