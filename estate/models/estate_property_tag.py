from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tags for the properties"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer(string="Color")

    # SQL checks
    _check_name = models.Constraint(
        "UNIQUE(name)",
        "The tag name should be unique.",
    )
