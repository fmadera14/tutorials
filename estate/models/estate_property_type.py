from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Type of the properties"
    _order = "name"

    name = fields.Char(required=True)
    sequence = fields.Integer("Sequence", default=1, help="Used to order stages.")

    property_ids = fields.One2many(
        "estate.property", "estate_property_type_id", string="Properties"
    )

    # SQL checks
    _check_name = models.Constraint(
        "UNIQUE(name)",
        "The type name should be unique.",
    )
