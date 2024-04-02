from odoo import http, _, fields
from odoo.http import request
from odoo.exceptions import UserError

class ProductCategoriesController(http.Controller):

    @http.route(['/products/load_categories'], type="http", auth="user", website=True, csrf=False, methods=["GET"])
    def load_categories(self):
        partner = request.env.user.partner_id
        if not partner:
            raise UserError(_('Please login to continue'))
        sale_orders = request.env['sale.order'].sudo().search([('partner_id', '=', partner.id)])

        return request.render("owl_lu.categ_by_partenr_page", {
            'categories': [{
            'id': categ_id.id,
            'name': categ_id.name,
        } for categ_id in sale_orders.order_line.product_template_id.categ_id ],
        })
