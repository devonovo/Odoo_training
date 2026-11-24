from odoo import fields, models
from odoo.tools import populate

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

_populate_sizes = {
        'small': 100,
        'medium': 1_000,
        'large': 10_000,
    }

def _populate_factories(self):
    return [
        ('name', populate.constant('Property {counter}')),
        ('expected_price', populate.randfloat(50000, 500000)),
        ('selling_price', populate.randfloat(50000, 500000)),
        ('bedrooms', populate.randint(1, 6)),
        ('living_area', populate.randint(30, 300)),
        ('facades', populate.randint(1, 4)),
        ('garage', populate.cartesian([True, False])),
        ('garden', populate.cartesian([True, False])),
        ('garden_area', populate.randint(0, 500)),
        ('garden_orientation', populate.randomize(['Nord', 'Sud', 'Ovest', 'Est'])),
    ]
