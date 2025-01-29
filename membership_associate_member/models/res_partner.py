from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def get_all_members_of_associate_member(self, associate_member_id):
        """
        param : a member id
        if member is define somewhere as associate_member, return all members where my member in param is the associate_member
        return : list of members (res.partner)
        """

        members = self.env["res.partner"].search(
                        [("associate_member", "=", associate_member_id)]
                    )

        return members