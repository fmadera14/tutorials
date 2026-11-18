{
    "name": "estate",
    "depends": [
        # "base_setup",
        "base",
    ],
    "application": True,
    "installable": True,
    "data": [
        "security/ir.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menus.xml",
    ],
}
