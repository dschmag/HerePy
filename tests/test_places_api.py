#!/usr/bin/env python

import os
import sys
import unittest
import responses
import codecs
import herepy

class PlacesApiTest(unittest.TestCase):

    def setUp(self):
        api = herepy.PlacesApi('app_id', 'app_code')
        self._api = api

    def test_initiation(self):
        self.assertIsInstance(self._api, herepy.PlacesApi)
        self.assertEqual(self._api._app_id, 'app_id')
        self.assertEqual(self._api._app_code, 'app_code')
        self.assertEqual(self._api._base_url, 'https://places.cit.api.here.com/places/v1/')

    @responses.activate
    def test_onebox_search_whensucceed(self):
        with open('testdata/models/places_api.json', 'r') as f:
            expectedResponse = f.read()
        responses.add(responses.GET, 'https://places.cit.api.here.com/places/v1/discover/search',
                  expectedResponse, status=200)
        response = self._api.onebox_search([37.7905,-122.4107], 'restaurant')
        self.assertTrue(response)
        self.assertIsInstance(response, herepy.PlacesResponse)

    @responses.activate
    def test_onebox_search_whenerroroccured(self):
        with open('testdata/models/places_api_error.json', 'r') as f:
            expectedResponse = f.read()
        responses.add(responses.GET, 'https://places.cit.api.here.com/places/v1/discover/search',
                  expectedResponse, status=200)
        response = self._api.onebox_search([37.7905,-122.4107], '')
        self.assertIsInstance(response, herepy.HEREError)

    @responses.activate
    def test_places_at_whensucceed(self):
        with open('testdata/models/places_api.json', 'r') as f:
            expectedResponse = f.read()
        responses.add(responses.GET, 'https://places.cit.api.here.com/places/v1/discover/explore',
                  expectedResponse, status=200)
        response = self._api.places_at([37.7905,-122.4107])
        self.assertTrue(response)
        self.assertIsInstance(response, herepy.PlacesResponse)

    @responses.activate
    def test_places_at_whenerroroccured(self):
        with open('testdata/models/places_api_error.json', 'r') as f:
            expectedResponse = f.read()
        responses.add(responses.GET, 'https://places.cit.api.here.com/places/v1/discover/explore',
                  expectedResponse, status=200)
        response = self._api.places_at([-9999.0, -9999.0])
        self.assertIsInstance(response, herepy.HEREError)

    @responses.activate
    def test_category_places_at_whensucceed(self):
        with open('testdata/models/places_api.json', 'r') as f:
            expectedResponse = f.read()
        responses.add(responses.GET, 'https://places.cit.api.here.com/places/v1/discover/explore',
                  expectedResponse, status=200)
        response = self._api.category_places_at([37.7905,-122.4107], [herepy.PlacesCategory.eat_drink])
        self.assertTrue(response)
        self.assertIsInstance(response, herepy.PlacesResponse)

    @responses.activate
    def test_category_places_at_whenerroroccured(self):
        with open('testdata/models/places_api_error.json', 'r') as f:
            expectedResponse = f.read()
        responses.add(responses.GET, 'https://places.cit.api.here.com/places/v1/discover/explore',
                  expectedResponse, status=200)
        response = self._api.category_places_at([-9999.0, -9999.0], [herepy.PlacesCategory.eat_drink])
        self.assertIsInstance(response, herepy.HEREError)

    def test_category_places_at_withoutnocategories(self):
        with self.assertRaises(Exception) as context:
            self._api.category_places_at([37.7905,-122.4107])
        self.assertTrue('category_places_at function requires category types!' in str(context.exception))

    @responses.activate
    def test_nearby_places_whensucceed(self):
        with open('testdata/models/places_api.json', 'r') as f:
            expectedResponse = f.read()
        responses.add(responses.GET, 'https://places.cit.api.here.com/places/v1/discover/here',
                  expectedResponse, status=200)
        response = self._api.nearby_places([37.7905,-122.4107])
        self.assertTrue(response)
        self.assertIsInstance(response, herepy.PlacesResponse)

    @responses.activate
    def test_nearby_places_whenerroroccured(self):
        with open('testdata/models/places_api_error.json', 'r') as f:
            expectedResponse = f.read()
        responses.add(responses.GET, 'https://places.cit.api.here.com/places/v1/discover/here',
                  expectedResponse, status=200)
        response = self._api.nearby_places([-9999.0, -9999.0])
        self.assertIsInstance(response, herepy.HEREError)
