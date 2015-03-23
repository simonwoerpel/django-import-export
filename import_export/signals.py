'''
Signals for django-import-export
'''

__author__ = 'simonwoerpel'


from django.dispatch import Signal


import_finished = Signal(providing_args=['result', ])
row_skipped = Signal(providing_args=['row', 'instance', 'original', ])
instance_created = Signal(providing_args=['instance', ])
instance_deleted = Signal(providing_args=['instance', ])
instance_updated = Signal(providing_args=['instance', ])
