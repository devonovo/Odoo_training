from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name=fields.Char(string='Name', required=True)
    description=fields.Text(string='Description')
    postcode=fields.Char(string='Postcode')
    date_available=fields.Datetime(string='Date Available')
    expected_price=fields.Float(string='Expected Price', required=True)
    selling_price=fields.Float(string='Selling Price')
    bedrooms=fields.Integer(string='Bedrooms')
    living_area=fields.Integer(string='Living Area')
    facades=fields.Integer(string='Facades')
    garage=fields.Boolean(string='Garage')
    garden=fields.Boolean(string='Garden')
    garden_area=fields.Integer(string='Garden Area')
    garden_orientation=fields.Selection(string='Garden Orientation',selection=[('Nord','nord'),('Sud','sud'),('Ovest','ovest'),('Est','est')],help='seleziona coordinate')


