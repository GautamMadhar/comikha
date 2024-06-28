from odoo import http
from odoo.http import request

class WebsiteForm(http.Controller):
    @http.route('/comikha-contact-form', type="http", auth="user", website=True, csrf=False)
    def submit_form(self, **kw):
        if request.httprequest.method == 'POST':
            # Extract form data
            profile_photo = kw.get('picture')
            i_card = kw.get('i_card')
            trader_card = kw.get('trader_card')
            miner_card = kw.get('miner_card')
            values = {
                'name': kw.get('name'),
                'birth_date': kw.get('birth_date'),
                'nationality': kw.get('nationality'),
                'street': kw.get('address'),
                'phone': kw.get('phone'),
                'first_name': kw.get('first_name'),
                'birth_place': kw.get('birth_place'),
                'occupation': kw.get('occupation'),
                'zip': kw.get('zipcode'),
                'email': kw.get('email'),
            }
            #Create a new res.partner record
            partner = request.env['res.partner'].sudo().create(values)

        return request.render('custom_form_snippet.contact_form_comikha', {})
