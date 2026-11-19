from datetime import timedelta, date
from odoo import api, exceptions, fields, models


class EstatePropertyOffers(models.Model):
    _name = "estate.property.offer"
    _description = "Offers of a property"
    _offer = "price desc"

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
                record.date_deadline = fields.Date.today() + timedelta(
                    days=record.validity
                )
            else:
                record.date_deadline = record.create_date + timedelta(
                    days=record.validity
                )

    def _inverse_date_deadline(self):
        for record in self:
            if not record.create_date:
                record.validity = (record.date_deadline - date.today()).days
            else:
                record.validity = (
                    record.date_deadline - record.create_date.date()
                ).days

    def action_accept_offer(self):
        for record in self:
            if any(
                offer != self and offer.status == "accepted"
                for offer in record.property_id.offer_ids
            ):
                raise exceptions.UserError("Already an offer accepted.")
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            record.property_id.state = "offer accepted"

    def action_refuse_offer(self):
        for record in self:
            record.status = "refused"
            if record.property_id.selling_price == record.price:
                record.property_id.selling_price = 0
            if record.property_id.buyer_id == record.partner_id:
                record.property_id.buyer_id = None
            if not any(
                offer.status == "accepted" for offer in record.property_id.offer_ids
            ):
                record.property_id.state = "offer received"

    # SQL checks
    _check_price = models.Constraint(
        "CHECK(price >= 0)",
        "The offer price should be extrictly positive.",
    )
