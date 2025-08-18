from odoo import fields, models, api, exceptions, _
from dateutil.relativedelta import relativedelta
from datetime import date

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'offer to real estate property'

    price = fields.Float(required=True)
    validity = fields.Integer(default=7)
    status = fields.Selection(copy=False,
                              default=None,
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
    
    
    # ====== Buttons offer ======
    def button_accept_offer(self):
        self.ensure_one()
        property = self.property_id
        if property.state in ['sold', 'cancelled', 'offer_accepted']:
            raise exceptions.UserError(_('This property cannot accept offers now.'))
        self.status = 'accepted'
        property.selling_price = self.price
        property.state = 'offer_accepted'

    def button_refuse_offer(self):
        self.ensure_one()
        property = self.property_id
        if self.status == 'accepted':
            property.selling_price = 0.0
            property.state = None
            self.status = 'refused'