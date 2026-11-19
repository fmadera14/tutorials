from datetime import timedelta
from odoo import api, fields, models


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
    validity = fields.Integer()
    date_deadline = fields.Date(
        compute="_compute_date_deadline", inverse="_inverse_date_deadline"
    )

    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", string="Property", required=True)

    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            if not record.create_date:
                continue

            record.date_deadline = record.create_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if not record.create_date:
                continue

            record.validity = (record.date_deadline - record.create_date.date()).days
