from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from datetime import date

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'offer to real estate property'

    price = fields.Float(required=True)
    validity = fields.Integer(default=7)
    status = fields.Selection(copy=False,
                              string='Status Offer',
                              selection=[
                                  ('accepted', 'Accepted'),
                                  ('refused', 'Refused')
                              ])
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)


    # ======= fields computed =======
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date.date() + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline and record.create_date:
                delta = record.date_deadline - record.create_date.date()
                record.validity = delta.days
    
