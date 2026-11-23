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
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_menus.xml",
        "views/res_users_views.xml",
    ],
    "author": "Francisco Madera",
    "license": "AGPL-3",
}
