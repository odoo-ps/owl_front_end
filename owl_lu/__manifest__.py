{
    'name': "owl_lu",
    'version': '17.0',
    'depends': ['base'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
        Tuto for using OWL in Front Web
    """, 
    "depends": [
        "sale_management",
        "website_sale",
        "website"
    ],
    "data": [
        'views/page_categ_by_partner.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'owl_lu/static/src/categ_by_partner/**/*',
            'owl_lu/static/src/categories/**/*',
        ],
    }
}
