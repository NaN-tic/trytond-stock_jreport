# This file is part stock_jreport module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import shipment


def register():
    Pool.register(
        shipment.Move,
        module='stock_jreport', type_='model')
    Pool.register(
        shipment.DeliveryNote,
        shipment.DeliveryNoteValued,
        module='stock_jreport', type_='report')
