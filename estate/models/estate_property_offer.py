from odoo import fields, models


class EstatePropertyOffers(models.Model):
    _name = "estate.property.offer"
    _description = "Offers of a property"

    price = fields.Float()
    status = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ]
    )
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", string="Property", required=True)
