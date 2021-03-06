# coding: utf-8

"""
    The Enrichment List

    The THS enrichment list  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contactme@markwilkins.co
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from walklist_api_service.api_client import ApiClient


class AnimalApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def animals_count_get(self, **kwargs):  # noqa: E501
        """animals_count_get  # noqa: E501

        Returns the count of animals records  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_count_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnimalPartial where: Specify and WHERE conditions, add LIKE as a prefix to fuzzy search
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.animals_count_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.animals_count_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def animals_count_get_with_http_info(self, **kwargs):  # noqa: E501
        """animals_count_get  # noqa: E501

        Returns the count of animals records  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_count_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnimalPartial where: Specify and WHERE conditions, add LIKE as a prefix to fuzzy search
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['where']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method animals_count_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userToken']  # noqa: E501

        return self.api_client.call_api(
            '/animals/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def animals_get(self, **kwargs):  # noqa: E501
        """animals_get  # noqa: E501

        Returns an animal, matching the provided QUERY params  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Where where: Specify and WHERE conditions, add LIKE as a prefix to fuzzy search
        :param int page: Specify which page of the paginated results you need. If omitted, page 1 will be sent.
        :param int limit: Specify which page of the paginated results you need. If omitted, page 1 will be sent.
        :param Order order: Specify which column to order by
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.animals_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.animals_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def animals_get_with_http_info(self, **kwargs):  # noqa: E501
        """animals_get  # noqa: E501

        Returns an animal, matching the provided QUERY params  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Where where: Specify and WHERE conditions, add LIKE as a prefix to fuzzy search
        :param int page: Specify which page of the paginated results you need. If omitted, page 1 will be sent.
        :param int limit: Specify which page of the paginated results you need. If omitted, page 1 will be sent.
        :param Order order: Specify which column to order by
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['where', 'page', 'limit', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method animals_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userToken']  # noqa: E501

        return self.api_client.call_api(
            '/animals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def animals_id_delete(self, id, **kwargs):  # noqa: E501
        """animals_id_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.animals_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.animals_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def animals_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """animals_id_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method animals_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `animals_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userToken']  # noqa: E501

        return self.api_client.call_api(
            '/animals/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Response',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def animals_id_get(self, id, **kwargs):  # noqa: E501
        """animals_id_get  # noqa: E501

        Returns an animal, matching the provided ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.animals_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.animals_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def animals_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """animals_id_get  # noqa: E501

        Returns an animal, matching the provided ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method animals_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `animals_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userToken']  # noqa: E501

        return self.api_client.call_api(
            '/animals/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def animals_id_patch(self, id, **kwargs):  # noqa: E501
        """animals_id_patch  # noqa: E501

        Updates animal based by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_patch(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param AnimalPartial body:
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.animals_id_patch_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.animals_id_patch_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def animals_id_patch_with_http_info(self, id, **kwargs):  # noqa: E501
        """animals_id_patch  # noqa: E501

        Updates animal based by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_patch_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param AnimalPartial body:
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method animals_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `animals_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userToken']  # noqa: E501

        return self.api_client.call_api(
            '/animals/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def animals_id_put(self, id, **kwargs):  # noqa: E501
        """animals_id_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_put(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param NewAnimal body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.animals_id_put_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.animals_id_put_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def animals_id_put_with_http_info(self, id, **kwargs):  # noqa: E501
        """animals_id_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_put_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param NewAnimal body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method animals_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `animals_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userToken']  # noqa: E501

        return self.api_client.call_api(
            '/animals/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def animals_id_signin_post(self, id, **kwargs):  # noqa: E501
        """animals_id_signin_post  # noqa: E501

        Creates a new enrichment sessions record  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_signin_post(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param AnimalSigninRequestBody body:
        :return: EnrichmentSessionCreatedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.animals_id_signin_post_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.animals_id_signin_post_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def animals_id_signin_post_with_http_info(self, id, **kwargs):  # noqa: E501
        """animals_id_signin_post  # noqa: E501

        Creates a new enrichment sessions record  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_signin_post_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param AnimalSigninRequestBody body:
        :return: EnrichmentSessionCreatedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method animals_id_signin_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `animals_id_signin_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userToken']  # noqa: E501

        return self.api_client.call_api(
            '/animals/{id}/signin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnrichmentSessionCreatedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def animals_id_signout_post(self, id, **kwargs):  # noqa: E501
        """animals_id_signout_post  # noqa: E501

        Creates a new active enrichment record  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_signout_post(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param NewActiveEnrichmentSession body:
        :return: InlineResponse2016
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.animals_id_signout_post_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.animals_id_signout_post_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def animals_id_signout_post_with_http_info(self, id, **kwargs):  # noqa: E501
        """animals_id_signout_post  # noqa: E501

        Creates a new active enrichment record  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_id_signout_post_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param NewActiveEnrichmentSession body:
        :return: InlineResponse2016
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method animals_id_signout_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `animals_id_signout_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userToken']  # noqa: E501

        return self.api_client.call_api(
            '/animals/{id}/signout', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2016',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def animals_patch(self, **kwargs):  # noqa: E501
        """animals_patch  # noqa: E501

        Updates one or more animals based on WHERE style query params  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_patch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnimalPatchRequestBody body:
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.animals_patch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.animals_patch_with_http_info(**kwargs)  # noqa: E501
            return data

    def animals_patch_with_http_info(self, **kwargs):  # noqa: E501
        """animals_patch  # noqa: E501

        Updates one or more animals based on WHERE style query params  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_patch_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnimalPatchRequestBody body:
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method animals_patch" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userToken']  # noqa: E501

        return self.api_client.call_api(
            '/animals', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def animals_post(self, **kwargs):  # noqa: E501
        """animals_post  # noqa: E501

        Creates a new animal record  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewAnimal body:
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.animals_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.animals_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def animals_post_with_http_info(self, **kwargs):  # noqa: E501
        """animals_post  # noqa: E501

        Creates a new animal record  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.animals_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewAnimal body:
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method animals_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userToken']  # noqa: E501

        return self.api_client.call_api(
            '/animals', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
