__author__ = 'simonwoerpel'


class BaseValidator(object):
    def __init__(self):
        self.error_list = []

    def validate(self):
        '''
        :return: bool
        '''
        raise NotImplementedError()

    def get_errors(self):
        '''
        :return: list
        '''
        return self.error_list

    @property
    def is_valid(self):
        self.validate()
        if self.error_list:
            return False
        return True

    @property
    def errors(self):
        if self.get_errors():
            return self.get_errors()
        return None


class BaseDatasetValidator(BaseValidator):
    '''
    Validates the given dataset before import (dry_run=True)
    stops import progress if is not valid
    '''
    def __init__(self, dataset):
        super(BaseDatasetValidator, self).__init__()
        self.dataset = dataset


class BaseInstanceDBValidator(BaseValidator):
    '''
    Validates the given instance against the db before import
    stops import progress if is not valid
    '''
    def __init__(self, instance):
        super(BaseInstanceDBValidator, self).__init__()
        self.instance = instance
