# This file is part stock_jreport module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.modules.jasper_reports.jasper import JasperReport

__all__ = ['DeliveryNote', 'DeliveryNoteValued', 'Move']


class DeliveryNote(JasperReport, metaclass=PoolMeta):
    __name__ = 'stock.shipment.out.delivery_note'


class DeliveryNoteValued(JasperReport, metaclass=PoolMeta):
    __name__ = 'stock.shipment.out.delivery_note_valued'


class Move(metaclass=PoolMeta):
    __name__ = 'stock.move'
    lot_number = fields.Function(fields.Char('Lot Number'), 'get_lot_number')

    def get_lot_number(self, name):
        if hasattr(self, "lot"):
            return self.lot.number if self.lot else None
