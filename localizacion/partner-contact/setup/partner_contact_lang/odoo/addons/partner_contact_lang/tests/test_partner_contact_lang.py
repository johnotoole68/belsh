# -*- coding: utf-8 -*-
# Copyright 2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2017 Vicent Cubells <vicent.cubells@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import common


class TestPartnerContactLang(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestPartnerContactLang, cls).setUpClass()
        cls.ResPartner = cls.env['res.partner']
        cls.partner = cls.ResPartner.create({
            'name': 'Partner test',
            'lang': 'en_US',
        })
        cls.contact = cls.ResPartner.create({
            'name': 'Contact test',
            'lang': False,
            'parent_id': cls.partner.id,
        })

    def test_onchange_parent_id(self):
        self.contact.parent_id = False
        res = self.contact.onchange_parent_id()
        self.assertIsNone(res)
        self.contact.parent_id = self.partner
        res = self.contact.onchange_parent_id()
        self.assertEqual(res.get('value', {}).get('lang'), 'en_US')

    def test_write_parent_lang(self):
        self.partner.lang = False
        self.partner.lang = 'en_US'
        self.assertEqual(self.contact.lang, 'en_US')
