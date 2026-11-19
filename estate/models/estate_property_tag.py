from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tags for the properties"

    name = fields.Char(required=True)

    # SQL checks
    _check_name = models.Constraint(
        "UNIQUE(name)",
        "The tag name should be unique.",
    )
