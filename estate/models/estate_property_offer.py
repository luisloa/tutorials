from odoo import fields, models 

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'offer to real estate property'

    price = fields.Float(required=True)
    status = fields.Selection(copy=False,
                              string='Status Offer',
                              selection=[
                                  ('accepted', 'Accepted'),
                                  ('refused', 'Refused')
                              ])
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
