from odoo import fields, models
from datetime import date
from dateutil.relativedelta import relativedelta



class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Información de propiedade inmobiliaria'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, 
                                    default=date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=False, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[
            ('nort', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ])
    state = fields.Selection(
        string = 'State',
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled')
        ],
        default='new',
    )
    active = fields.Boolean(default=True)

    property_type_id = fields.Many2one('estate.property.type', string='Type of Property', ondelete='restrict')
    seller_id = fields.Many2one('res.users', string='Seller', default=lambda self: self.env.user.id, ondelete='restrict')
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False, ondelete='restrict')
    
    tag_ids = fields.Many2many('estate.property.tag', 
                               relation='estate_property_estate_property_tag',
                               column1='property_id',
                               column2='tag_id',
                               string='Tags of propery',
                               ondelete='restrict')

    offer_ids = fields.One2many('estate.property.offer', 'property_id',
                                strting='Offer',
                                delegate=True)
    



