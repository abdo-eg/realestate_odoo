from odoo import models, fields, api
# to use exceptions
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = "property"

    name = fields.Char(required=1)
    description = fields.Text()
    postcode = fields.Char(required=1)
    data_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer() #use constrains, 0 will considered as a value!
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')
        ])
    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold')
    ] ,default='draft')
    #add constrains
    @api.constrains('selling_price')
    def _check_selling_price_not_zero(self):
        for record in self:
            if record.selling_price == 1:
                raise ValidationError("please enter selling price")
    

    @api.model_create_multi
    def create(self,vals):
        res = super(Property , self).create(vals)
        print("\033[92minside create function!\033[0m")

        return res
