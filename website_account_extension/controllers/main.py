from odoo import http
from odoo.http import request
import base64



class WebsiteForm(http.Controller):
    @http.route('/comikha-contact-form', type="http", auth="user", website=True, csrf=False)
    def submit_form(self, **kw):
        if request.httprequest.method == 'POST':
            # Extract form data
            # profile_photo = kw.get('picture')
            # i_card = kw.get('i_card')
            # trader_card = kw.get('trader_card')
            # miner_card = kw.get('miner_card')
            # picture_data = self.process_uploaded_file(profile_photo)
            # id_card_data = self.process_uploaded_file(i_card)
            # trader_card_data = self.process_uploaded_file(trader_card)
            # miner_card_data = self.process_uploaded_file(miner_card)
        
            values = {
                # 'image_1920': picture_data,
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
                'purpose_of_membership' : kw.get('options')
            }
            print(values)
            # print(ans)
            #Create a new res.partner record
            partner = request.env['res.partner'].sudo().create(values)

        return request.render('website_account_extension.contact_form_comikha', {})
    
    def process_uploaded_file(self, file):
        # Example function to process uploaded file data
        if file:
            # Read and process file content
            file_data = file.read()
            # You can save the file_data to database or perform other operations
            return base64.b64encode(file_data).decode('utf-8')  # Return encoded file data for example
        return None
