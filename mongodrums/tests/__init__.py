from unittest import TestCase

import pymongo

from mongodrums.config import get_config, configure

# TODO: use ming's "mongo in memory"?


class BaseTest(TestCase):
    TEST_DB = 'mongodrums_test'
    def setUp(self):
        self.saved_config = get_config()
        self.client = pymongo.MongoClient()
        self.client.drop_database(self.__class__.TEST_DB)
        self.db = self.client[self.__class__.TEST_DB]

    def tearDown(self):
        configure(self.saved_config)
        self.client.drop_database(self.__class__.TEST_DB)

