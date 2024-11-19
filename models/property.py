from odoo import models, fields

class Property(models.Model):
    _name = "property"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    data_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garder_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')
        ])