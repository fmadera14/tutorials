from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Type of the properties"

    name = fields.Char(required=True)

    # SQL checks
    _check_name = models.Constraint(
        "UNIQUE(name)",
        "The type name should be unique.",
    )
