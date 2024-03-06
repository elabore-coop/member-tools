from odoo import fields, models


class MembershipInvoice(models.TransientModel):
    _inherit = "membership.invoice"

    payment_mode_id = fields.Many2one(
        comodel_name='account.payment.mode', string="Payment Mode",
        domain=[("payment_type", "=", 'inbound')],
        )

    def membership_invoice(self):
        res = super(MembershipInvoice, self).membership_invoice()
        invoice_ids = None
        for d in res['domain']:
            if d[0] == 'id' and d[1] == 'in':
                invoice_ids = d[2]
                if invoice_ids:
                    self.env['account.invoice'].browse(invoice_ids).write({
                    'payment_mode_id':self.payment_mode_id.id,
                    })
        return res
