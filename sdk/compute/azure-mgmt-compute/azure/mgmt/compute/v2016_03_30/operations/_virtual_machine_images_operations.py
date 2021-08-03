# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_get_request(
    location,  # type: str
    publisher_name,  # type: str
    offer,  # type: str
    skus,  # type: str
    version,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2016-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions/{version}')
    path_format_arguments = {
        'location': _SERIALIZER.url("location", location, 'str'),
        'publisherName': _SERIALIZER.url("publisher_name", publisher_name, 'str'),
        'offer': _SERIALIZER.url("offer", offer, 'str'),
        'skus': _SERIALIZER.url("skus", skus, 'str'),
        'version': _SERIALIZER.url("version", version, 'str'),
        'subscriptionId': _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    location,  # type: str
    publisher_name,  # type: str
    offer,  # type: str
    skus,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    expand = kwargs.pop('expand', None)  # type: Optional[str]
    top = kwargs.pop('top', None)  # type: Optional[int]
    orderby = kwargs.pop('orderby', None)  # type: Optional[str]

    api_version = "2016-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions')
    path_format_arguments = {
        'location': _SERIALIZER.url("location", location, 'str'),
        'publisherName': _SERIALIZER.url("publisher_name", publisher_name, 'str'),
        'offer': _SERIALIZER.url("offer", offer, 'str'),
        'skus': _SERIALIZER.url("skus", skus, 'str'),
        'subscriptionId': _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if expand is not None:
        query_parameters['$expand'] = _SERIALIZER.query("expand", expand, 'str')
    if top is not None:
        query_parameters['$top'] = _SERIALIZER.query("top", top, 'int')
    if orderby is not None:
        query_parameters['$orderby'] = _SERIALIZER.query("orderby", orderby, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_offers_request(
    location,  # type: str
    publisher_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2016-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers')
    path_format_arguments = {
        'location': _SERIALIZER.url("location", location, 'str'),
        'publisherName': _SERIALIZER.url("publisher_name", publisher_name, 'str'),
        'subscriptionId': _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_publishers_request(
    location,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2016-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers')
    path_format_arguments = {
        'location': _SERIALIZER.url("location", location, 'str'),
        'subscriptionId': _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_skus_request(
    location,  # type: str
    publisher_name,  # type: str
    offer,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2016-03-30"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus')
    path_format_arguments = {
        'location': _SERIALIZER.url("location", location, 'str'),
        'publisherName': _SERIALIZER.url("publisher_name", publisher_name, 'str'),
        'offer': _SERIALIZER.url("offer", offer, 'str'),
        'subscriptionId': _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class VirtualMachineImagesOperations(object):
    """VirtualMachineImagesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.compute.v2016_03_30.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get(
        self,
        location,  # type: str
        publisher_name,  # type: str
        offer,  # type: str
        skus,  # type: str
        version,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.VirtualMachineImage"
        """Gets a virtual machine image.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :param offer: A valid image publisher offer.
        :type offer: str
        :param skus: A valid image SKU.
        :type skus: str
        :param version: A valid image SKU version.
        :type version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineImage, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2016_03_30.models.VirtualMachineImage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.VirtualMachineImage"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_request(
            location=location,
            publisher_name=publisher_name,
            offer=offer,
            skus=skus,
            version=version,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("VirtualMachineImage", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions/{version}"}  # type: ignore

    def list(
        self,
        location,  # type: str
        publisher_name,  # type: str
        offer,  # type: str
        skus,  # type: str
        expand=None,  # type: Optional[str]
        top=None,  # type: Optional[int]
        orderby=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.VirtualMachineImageResource"]
        """Gets a list of all virtual machine image versions for the specified location, publisher, offer,
        and SKU.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :param offer: A valid image publisher offer.
        :type offer: str
        :param skus: A valid image SKU.
        :type skus: str
        :param expand: The expand expression to apply on the operation.
        :type expand: str
        :param top:
        :type top: int
        :param orderby:
        :type orderby: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2016_03_30.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_list_request(
            location=location,
            publisher_name=publisher_name,
            offer=offer,
            skus=skus,
            subscription_id=self._config.subscription_id,
            expand=expand,
            top=top,
            orderby=orderby,
            template_url=self.list.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions"}  # type: ignore

    def list_offers(
        self,
        location,  # type: str
        publisher_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.VirtualMachineImageResource"]
        """Gets a list of virtual machine image offers for the specified location and publisher.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2016_03_30.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_list_offers_request(
            location=location,
            publisher_name=publisher_name,
            subscription_id=self._config.subscription_id,
            template_url=self.list_offers.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_offers.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers"}  # type: ignore

    def list_publishers(
        self,
        location,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.VirtualMachineImageResource"]
        """Gets a list of virtual machine image publishers for the specified Azure location.

        :param location: The name of a supported Azure region.
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2016_03_30.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_list_publishers_request(
            location=location,
            subscription_id=self._config.subscription_id,
            template_url=self.list_publishers.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_publishers.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers"}  # type: ignore

    def list_skus(
        self,
        location,  # type: str
        publisher_name,  # type: str
        offer,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.VirtualMachineImageResource"]
        """Gets a list of virtual machine image SKUs for the specified location, publisher, and offer.

        :param location: The name of a supported Azure region.
        :type location: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :param offer: A valid image publisher offer.
        :type offer: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2016_03_30.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_list_skus_request(
            location=location,
            publisher_name=publisher_name,
            offer=offer,
            subscription_id=self._config.subscription_id,
            template_url=self.list_skus.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_skus.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus"}  # type: ignore
