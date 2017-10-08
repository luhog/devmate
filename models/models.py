# -*- coding: utf-8 -*-

from odoo import models, fields, api

class betavision(models.Model):
     _inherit = ['account.invoice']
     @api.model
     def run_confirm_invoices(self,ids=None):
            ids=self.search([('state','=', 'draft')]).ids
            res=self.browse(ids).action_invoice_open()
            return res
     
class SaleOrder(models.Model):
     _inherit = ['sale.order']
      
     @api.multi
     def action_quotation_send(self):
        '''
        This function opens a window to compose an email, with the edi sale template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('betavision', 'email_template_edi_sale2')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = dict()
        ctx.update({
            'default_model': 'sale.order',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "sale.mail_template_data_notification_email_sale_order2"
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }
     
     
     
class AccountInvoice(models.Model):
     _inherit = ['account.invoice']
      
     @api.multi
     def action_invoice_sent(self):
        """ Open a window to compose an email, with the edi invoice template
        '''
