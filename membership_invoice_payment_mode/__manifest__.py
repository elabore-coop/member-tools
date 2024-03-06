# Copyright 2020 Lokavaluto ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "membersip_invoice_payment_mode",
    "version": "12.0.1.0.0",
    "author": "Élabore",
    "maintainer": "False",
    "website": "elabore.coop",
    "license": "",
    "category": "",
    "summary": "Add payment mode in merbership invoice wizard",
    # any module necessary for this one to work correctly
    "depends": [
        "account_payment_mode",
    ],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "wizard/membership_invoice_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
    "application": False,
}
