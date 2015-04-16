#!/usr/bin/env python
# coding: utf-8

"""
StoreApi.py
Copyright 2015 Reverb Technologies, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os
import urllib

from models import *


class StoreApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def get_inventory(self, **kwargs):
        """Returns pet inventories by status

        Args:
            
        
        Returns: map(String, int)
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_inventory" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/store/inventory'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        accepts = ['application/json', 'application/xml']
        headerParams['Accept'] = ', '.join(accepts)

        content_types = []
        headerParams['Content-Type'] = content_types[0] if len(content_types) > 0 else 'application/json'

        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'map(String, int)')
        return responseObject
        
        
        
    
    def place_order(self, **kwargs):
        """Place an order for a pet

        Args:
            
            body, Order: order placed for purchasing the pet (required)
            
            
        
        Returns: Order
        """

        allParams = ['body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method place_order" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/store/order'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        accepts = ['application/json', 'application/xml']
        headerParams['Accept'] = ', '.join(accepts)

        content_types = []
        headerParams['Content-Type'] = content_types[0] if len(content_types) > 0 else 'application/json'

        

        

        

        

        
        if ('body' in params):
            bodyParam = params['body']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Order')
        return responseObject
        
        
        
    
    def get_order_by_id(self, **kwargs):
        """Find purchase order by ID

        Args:
            
            order_id, str: ID of pet that needs to be fetched (required)
            
            
        
        Returns: Order
        """

        allParams = ['order_id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_order_by_id" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/store/order/{orderId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        accepts = ['application/json', 'application/xml']
        headerParams['Accept'] = ', '.join(accepts)

        content_types = []
        headerParams['Content-Type'] = content_types[0] if len(content_types) > 0 else 'application/json'

        

        

        
        if ('order_id' in params):
            replacement = str(self.apiClient.toPathValue(params['order_id']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'orderId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Order')
        return responseObject
        
        
        
    
    def delete_order(self, **kwargs):
        """Delete purchase order by ID

        Args:
            
            order_id, str: ID of the order that needs to be deleted (required)
            
            
        
        Returns: 
        """

        allParams = ['order_id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method delete_order" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/store/order/{orderId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        accepts = ['application/json', 'application/xml']
        headerParams['Accept'] = ', '.join(accepts)

        content_types = []
        headerParams['Content-Type'] = content_types[0] if len(content_types) > 0 else 'application/json'

        

        

        
        if ('order_id' in params):
            replacement = str(self.apiClient.toPathValue(params['order_id']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'orderId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        
        
    

