# coding= utf-8

{
    "name": "Sur Motors",
    "version": "1.0",
    "depends": [
        "base", "sale", "fleet", "hr", "purchase",
        "mrp", "mrp_operations", "product_manufacturer",
        "board",
    ],
    "auhtor": "Edgard Pimentel - SIDET",
    "website": "",
    "category": "Module Customized",
    "description": "Vehiculos",
    'data': [
        "security/ir.model.access.csv",
        "data/department_data.xml",
        "data/bahia_data.xml"
    ],
    'init_xml': [
        "security/surmotors_security.xml",
        "fleet/fleet_view.xml",
        "sale/sale_view.xml",
        "surmotors_bahias/surmotors_bahia_view.xml",
        #"surmotors_bahias/surmotors_bahia_workflow.xml",
        "mrp/mrp_view.xml",
        "product/product_view.xml",
        "purchase/purchase_view.xml",
        "stock/stock_view.xml",
        "account/account_view.xml",
        "fleet/surmotors_contract_workflow.xml",
        "hr/hr_view.xml",
        "res_partner/res_partner_view.xml",
        "stock/wizard/stock_report_view.xml",
        "deleted_menu.xml"
    ],
    'installable': True,
    'active': False
}
