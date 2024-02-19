# xleap._client.V1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_ai_scores_data_point**](V1Api.md#calculate_ai_scores_data_point) | **POST** /v1/api/data/{id}/calculate_ai_scores | 
[**create_api_key**](V1Api.md#create_api_key) | **POST** /v1/api/api-keys | 
[**create_data_point_create**](V1Api.md#create_data_point_create) | **POST** /v1/api/data | 
[**create_metrics_data**](V1Api.md#create_metrics_data) | **POST** /v1/api/metrics | 
[**create_ml_model**](V1Api.md#create_ml_model) | **POST** /v1/api/model | 
[**create_org_list**](V1Api.md#create_org_list) | **POST** /v1/api/org | 
[**create_project_create**](V1Api.md#create_project_create) | **POST** /v1/api/projects | 
[**create_prompt**](V1Api.md#create_prompt) | **POST** /v1/api/prompts | 
[**create_run**](V1Api.md#create_run) | **POST** /v1/api/runs | 
[**destroy_data_point**](V1Api.md#destroy_data_point) | **DELETE** /v1/api/data/{id} | 
[**destroy_metrics_data**](V1Api.md#destroy_metrics_data) | **DELETE** /v1/api/metrics/{id} | 
[**destroy_ml_model**](V1Api.md#destroy_ml_model) | **DELETE** /v1/api/model/{id} | 
[**destroy_org_list**](V1Api.md#destroy_org_list) | **DELETE** /v1/api/org/{id} | 
[**destroy_prompt**](V1Api.md#destroy_prompt) | **DELETE** /v1/api/prompts/{id} | 
[**destroy_run**](V1Api.md#destroy_run) | **DELETE** /v1/api/runs/{id} | 
[**exchange_token_exchange_token_request**](V1Api.md#exchange_token_exchange_token_request) | **POST** /v1/api/oauth/exchange-token | 
[**get_api_key_token_obtain**](V1Api.md#get_api_key_token_obtain) | **POST** /v1/api/api-keys/get_api_key | 
[**get_user_org_member**](V1Api.md#get_user_org_member) | **GET** /v1/api/api-keys/get_user | 
[**get_user_settings_user_preference**](V1Api.md#get_user_settings_user_preference) | **GET** /v1/api/api-keys/get_user_settings | 
[**list_api_keys**](V1Api.md#list_api_keys) | **GET** /v1/api/api-keys | 
[**list_data_points**](V1Api.md#list_data_points) | **GET** /v1/api/data | 
[**list_metrics_datas**](V1Api.md#list_metrics_datas) | **GET** /v1/api/metrics | 
[**list_ml_models**](V1Api.md#list_ml_models) | **GET** /v1/api/model | 
[**list_org_lists**](V1Api.md#list_org_lists) | **GET** /v1/api/org | 
[**list_projects**](V1Api.md#list_projects) | **GET** /v1/api/projects | 
[**list_prompts**](V1Api.md#list_prompts) | **GET** /v1/api/prompts | 
[**list_runs**](V1Api.md#list_runs) | **GET** /v1/api/runs | 
[**partial_update_api_key_update**](V1Api.md#partial_update_api_key_update) | **PATCH** /v1/api/api-keys/{id} | 
[**partial_update_data_point_create**](V1Api.md#partial_update_data_point_create) | **PATCH** /v1/api/data/{id} | 
[**partial_update_metrics_data**](V1Api.md#partial_update_metrics_data) | **PATCH** /v1/api/metrics/{id} | 
[**partial_update_ml_model**](V1Api.md#partial_update_ml_model) | **PATCH** /v1/api/model/{id} | 
[**partial_update_org_list**](V1Api.md#partial_update_org_list) | **PATCH** /v1/api/org/{id} | 
[**partial_update_project**](V1Api.md#partial_update_project) | **PATCH** /v1/api/projects/{id} | 
[**partial_update_prompt**](V1Api.md#partial_update_prompt) | **PATCH** /v1/api/prompts/{id} | 
[**partial_update_run**](V1Api.md#partial_update_run) | **PATCH** /v1/api/runs/{id} | 
[**retrieve_api_key**](V1Api.md#retrieve_api_key) | **GET** /v1/api/api-keys/{id} | 
[**retrieve_chart_data**](V1Api.md#retrieve_chart_data) | **GET** /v1/api/chart/{id} | 
[**retrieve_data_point**](V1Api.md#retrieve_data_point) | **GET** /v1/api/data/{id} | 
[**retrieve_metrics_data**](V1Api.md#retrieve_metrics_data) | **GET** /v1/api/metrics/{id} | 
[**retrieve_ml_model**](V1Api.md#retrieve_ml_model) | **GET** /v1/api/model/{id} | 
[**retrieve_org_detail**](V1Api.md#retrieve_org_detail) | **GET** /v1/api/org/{id} | 
[**retrieve_project_detail**](V1Api.md#retrieve_project_detail) | **GET** /v1/api/projects/{id} | 
[**retrieve_prompt**](V1Api.md#retrieve_prompt) | **GET** /v1/api/prompts/{id} | 
[**retrieve_run**](V1Api.md#retrieve_run) | **GET** /v1/api/runs/{id} | 
[**stat_project**](V1Api.md#stat_project) | **GET** /v1/api/projects/{id}/stat | 
[**update_api_key_update**](V1Api.md#update_api_key_update) | **PUT** /v1/api/api-keys/{id} | 
[**update_data_point_create**](V1Api.md#update_data_point_create) | **PUT** /v1/api/data/{id} | 
[**update_metrics_data**](V1Api.md#update_metrics_data) | **PUT** /v1/api/metrics/{id} | 
[**update_ml_model**](V1Api.md#update_ml_model) | **PUT** /v1/api/model/{id} | 
[**update_org_list**](V1Api.md#update_org_list) | **PUT** /v1/api/org/{id} | 
[**update_project**](V1Api.md#update_project) | **PUT** /v1/api/projects/{id} | 
[**update_prompt**](V1Api.md#update_prompt) | **PUT** /v1/api/prompts/{id} | 
[**update_run**](V1Api.md#update_run) | **PUT** /v1/api/runs/{id} | 


# **calculate_ai_scores_data_point**
> DataPoint calculate_ai_scores_data_point(id, data_point=data_point)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.data_point import DataPoint
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 
    data_point = xleap._client.DataPoint() # DataPoint |  (optional)

    try:
        api_response = api_instance.calculate_ai_scores_data_point(id, data_point=data_point)
        print("The response of V1Api->calculate_ai_scores_data_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->calculate_ai_scores_data_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data_point** | [**DataPoint**](DataPoint.md)|  | [optional] 

### Return type

[**DataPoint**](DataPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key**
> APIKey create_api_key(api_key=api_key)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.api_key import APIKey
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    api_key = xleap._client.APIKey() # APIKey |  (optional)

    try:
        api_response = api_instance.create_api_key(api_key=api_key)
        print("The response of V1Api->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | [**APIKey**](APIKey.md)|  | [optional] 

### Return type

[**APIKey**](APIKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_point_create**
> DataPoint create_data_point_create(data_point_create=data_point_create)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.data_point import DataPoint
from xleap._client.models.data_point_create import DataPointCreate
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    data_point_create = xleap._client.DataPointCreate() # DataPointCreate |  (optional)

    try:
        api_response = api_instance.create_data_point_create(data_point_create=data_point_create)
        print("The response of V1Api->create_data_point_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_data_point_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_point_create** | [**DataPointCreate**](DataPointCreate.md)|  | [optional] 

### Return type

[**DataPoint**](DataPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metrics_data**
> Metrics create_metrics_data(metrics=metrics)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.metrics import Metrics
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    metrics = xleap._client.Metrics() # Metrics |  (optional)

    try:
        api_response = api_instance.create_metrics_data(metrics=metrics)
        print("The response of V1Api->create_metrics_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_metrics_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics** | [**Metrics**](Metrics.md)|  | [optional] 

### Return type

[**Metrics**](Metrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ml_model**
> MLModel create_ml_model(ml_model=ml_model)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.ml_model import MLModel
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    ml_model = xleap._client.MLModel() # MLModel |  (optional)

    try:
        api_response = api_instance.create_ml_model(ml_model=ml_model)
        print("The response of V1Api->create_ml_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_ml_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ml_model** | [**MLModel**](MLModel.md)|  | [optional] 

### Return type

[**MLModel**](MLModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_org_list**
> OrgList create_org_list(org_list=org_list)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.org_list import OrgList
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    org_list = xleap._client.OrgList() # OrgList |  (optional)

    try:
        api_response = api_instance.create_org_list(org_list=org_list)
        print("The response of V1Api->create_org_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_org_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_list** | [**OrgList**](OrgList.md)|  | [optional] 

### Return type

[**OrgList**](OrgList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_create**
> ProjectCreate create_project_create(project_create=project_create)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.project_create import ProjectCreate
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    project_create = xleap._client.ProjectCreate() # ProjectCreate |  (optional)

    try:
        api_response = api_instance.create_project_create(project_create=project_create)
        print("The response of V1Api->create_project_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_project_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create** | [**ProjectCreate**](ProjectCreate.md)|  | [optional] 

### Return type

[**ProjectCreate**](ProjectCreate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_prompt**
> Prompt create_prompt(prompt=prompt)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.prompt import Prompt
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    prompt = xleap._client.Prompt() # Prompt |  (optional)

    try:
        api_response = api_instance.create_prompt(prompt=prompt)
        print("The response of V1Api->create_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt** | [**Prompt**](Prompt.md)|  | [optional] 

### Return type

[**Prompt**](Prompt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_run**
> RunCreate create_run(run_create=run_create)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.run_create import RunCreate
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    run_create = xleap._client.RunCreate() # RunCreate |  (optional)

    try:
        api_response = api_instance.create_run(run_create=run_create)
        print("The response of V1Api->create_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_create** | [**RunCreate**](RunCreate.md)|  | [optional] 

### Return type

[**RunCreate**](RunCreate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_data_point**
> destroy_data_point(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.destroy_data_point(id)
    except Exception as e:
        print("Exception when calling V1Api->destroy_data_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_metrics_data**
> destroy_metrics_data(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique integer value identifying this metrics data.

    try:
        api_instance.destroy_metrics_data(id)
    except Exception as e:
        print("Exception when calling V1Api->destroy_metrics_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this metrics data. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_ml_model**
> destroy_ml_model(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this ml model.

    try:
        api_instance.destroy_ml_model(id)
    except Exception as e:
        print("Exception when calling V1Api->destroy_ml_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this ml model. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_org_list**
> destroy_org_list(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.destroy_org_list(id)
    except Exception as e:
        print("Exception when calling V1Api->destroy_org_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_prompt**
> destroy_prompt(id, parent_id=parent_id, root_id=root_id, base_query=base_query)





### Example


```python
import time
import os
import xleap._client
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this prompt.
    parent_id = 'parent_id_example' # str | parent_id (optional)
    root_id = 'root_id_example' # str | root_id (optional)
    base_query = 'base_query_example' # str | base_query (optional)

    try:
        api_instance.destroy_prompt(id, parent_id=parent_id, root_id=root_id, base_query=base_query)
    except Exception as e:
        print("Exception when calling V1Api->destroy_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this prompt. | 
 **parent_id** | **str**| parent_id | [optional] 
 **root_id** | **str**| root_id | [optional] 
 **base_query** | **str**| base_query | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_run**
> destroy_run(id, parent_run_id=parent_run_id, session_name=session_name, root_node=root_node)





### Example


```python
import time
import os
import xleap._client
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this run.
    parent_run_id = 'parent_run_id_example' # str | parent_run_id (optional)
    session_name = 'session_name_example' # str | session_name (optional)
    root_node = 'root_node_example' # str | root_node (optional)

    try:
        api_instance.destroy_run(id, parent_run_id=parent_run_id, session_name=session_name, root_node=root_node)
    except Exception as e:
        print("Exception when calling V1Api->destroy_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this run. | 
 **parent_run_id** | **str**| parent_run_id | [optional] 
 **session_name** | **str**| session_name | [optional] 
 **root_node** | **str**| root_node | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_token_exchange_token_request**
> ExchangeTokenRequest exchange_token_exchange_token_request(exchange_token_request=exchange_token_request)



given credentials get token pair.

### Example


```python
import time
import os
import xleap._client
from xleap._client.models.exchange_token_request import ExchangeTokenRequest
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    exchange_token_request = xleap._client.ExchangeTokenRequest() # ExchangeTokenRequest |  (optional)

    try:
        api_response = api_instance.exchange_token_exchange_token_request(exchange_token_request=exchange_token_request)
        print("The response of V1Api->exchange_token_exchange_token_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->exchange_token_exchange_token_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_token_request** | [**ExchangeTokenRequest**](ExchangeTokenRequest.md)|  | [optional] 

### Return type

[**ExchangeTokenRequest**](ExchangeTokenRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key_token_obtain**
> TokenResponse get_api_key_token_obtain(token_obtain=token_obtain)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.token_obtain import TokenObtain
from xleap._client.models.token_response import TokenResponse
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    token_obtain = xleap._client.TokenObtain() # TokenObtain |  (optional)

    try:
        api_response = api_instance.get_api_key_token_obtain(token_obtain=token_obtain)
        print("The response of V1Api->get_api_key_token_obtain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_api_key_token_obtain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_obtain** | [**TokenObtain**](TokenObtain.md)|  | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_org_member**
> OrgMember get_user_org_member()





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.org_member import OrgMember
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)

    try:
        api_response = api_instance.get_user_org_member()
        print("The response of V1Api->get_user_org_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_user_org_member: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgMember**](OrgMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_settings_user_preference**
> UserPreference get_user_settings_user_preference()





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.user_preference import UserPreference
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)

    try:
        api_response = api_instance.get_user_settings_user_preference()
        print("The response of V1Api->get_user_settings_user_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_user_settings_user_preference: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserPreference**](UserPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> ListAPIKeys200Response list_api_keys(cursor=cursor, page_size=page_size)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.list_api_keys200_response import ListAPIKeys200Response
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    cursor = 'cursor_example' # str | The pagination cursor value. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.list_api_keys(cursor=cursor, page_size=page_size)
        print("The response of V1Api->list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**ListAPIKeys200Response**](ListAPIKeys200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_points**
> ListDataPoints200Response list_data_points(cursor=cursor, page_size=page_size, project=project, include_all=include_all, filter=filter)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.list_data_points200_response import ListDataPoints200Response
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    cursor = 'cursor_example' # str | The pagination cursor value. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    project = 'project_example' # str | project (optional)
    include_all = 'include_all_example' # str | include_all (optional)
    filter = 'filter_example' # str | Filter (optional)

    try:
        api_response = api_instance.list_data_points(cursor=cursor, page_size=page_size, project=project, include_all=include_all, filter=filter)
        print("The response of V1Api->list_data_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_data_points: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **project** | **str**| project | [optional] 
 **include_all** | **str**| include_all | [optional] 
 **filter** | **str**| Filter | [optional] 

### Return type

[**ListDataPoints200Response**](ListDataPoints200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metrics_datas**
> ListMetricsDatas200Response list_metrics_datas(cursor=cursor, page_size=page_size)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.list_metrics_datas200_response import ListMetricsDatas200Response
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    cursor = 'cursor_example' # str | The pagination cursor value. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.list_metrics_datas(cursor=cursor, page_size=page_size)
        print("The response of V1Api->list_metrics_datas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_metrics_datas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**ListMetricsDatas200Response**](ListMetricsDatas200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ml_models**
> ListMLModels200Response list_ml_models(cursor=cursor, page_size=page_size)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.list_ml_models200_response import ListMLModels200Response
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    cursor = 'cursor_example' # str | The pagination cursor value. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.list_ml_models(cursor=cursor, page_size=page_size)
        print("The response of V1Api->list_ml_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_ml_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**ListMLModels200Response**](ListMLModels200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_lists**
> ListOrgLists200Response list_org_lists(cursor=cursor, page_size=page_size)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.list_org_lists200_response import ListOrgLists200Response
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    cursor = 'cursor_example' # str | The pagination cursor value. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.list_org_lists(cursor=cursor, page_size=page_size)
        print("The response of V1Api->list_org_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_org_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**ListOrgLists200Response**](ListOrgLists200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ListProjects200Response list_projects(cursor=cursor, page_size=page_size)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.list_projects200_response import ListProjects200Response
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    cursor = 'cursor_example' # str | The pagination cursor value. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.list_projects(cursor=cursor, page_size=page_size)
        print("The response of V1Api->list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**ListProjects200Response**](ListProjects200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_prompts**
> ListPrompts200Response list_prompts(cursor=cursor, page_size=page_size, parent_id=parent_id, root_id=root_id, base_query=base_query)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.list_prompts200_response import ListPrompts200Response
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    cursor = 'cursor_example' # str | The pagination cursor value. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    parent_id = 'parent_id_example' # str | parent_id (optional)
    root_id = 'root_id_example' # str | root_id (optional)
    base_query = 'base_query_example' # str | base_query (optional)

    try:
        api_response = api_instance.list_prompts(cursor=cursor, page_size=page_size, parent_id=parent_id, root_id=root_id, base_query=base_query)
        print("The response of V1Api->list_prompts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_prompts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **parent_id** | **str**| parent_id | [optional] 
 **root_id** | **str**| root_id | [optional] 
 **base_query** | **str**| base_query | [optional] 

### Return type

[**ListPrompts200Response**](ListPrompts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runs**
> ListRuns200Response list_runs(cursor=cursor, page_size=page_size, parent_run_id=parent_run_id, session_name=session_name, root_node=root_node)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.list_runs200_response import ListRuns200Response
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    cursor = 'cursor_example' # str | The pagination cursor value. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    parent_run_id = 'parent_run_id_example' # str | parent_run_id (optional)
    session_name = 'session_name_example' # str | session_name (optional)
    root_node = 'root_node_example' # str | root_node (optional)

    try:
        api_response = api_instance.list_runs(cursor=cursor, page_size=page_size, parent_run_id=parent_run_id, session_name=session_name, root_node=root_node)
        print("The response of V1Api->list_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **parent_run_id** | **str**| parent_run_id | [optional] 
 **session_name** | **str**| session_name | [optional] 
 **root_node** | **str**| root_node | [optional] 

### Return type

[**ListRuns200Response**](ListRuns200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_api_key_update**
> APIKeyUpdate partial_update_api_key_update(id, api_key_update=api_key_update)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.api_key_update import APIKeyUpdate
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 
    api_key_update = xleap._client.APIKeyUpdate() # APIKeyUpdate |  (optional)

    try:
        api_response = api_instance.partial_update_api_key_update(id, api_key_update=api_key_update)
        print("The response of V1Api->partial_update_api_key_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->partial_update_api_key_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **api_key_update** | [**APIKeyUpdate**](APIKeyUpdate.md)|  | [optional] 

### Return type

[**APIKeyUpdate**](APIKeyUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_data_point_create**
> DataPoint partial_update_data_point_create(id, data_point_create=data_point_create)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.data_point import DataPoint
from xleap._client.models.data_point_create import DataPointCreate
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 
    data_point_create = xleap._client.DataPointCreate() # DataPointCreate |  (optional)

    try:
        api_response = api_instance.partial_update_data_point_create(id, data_point_create=data_point_create)
        print("The response of V1Api->partial_update_data_point_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->partial_update_data_point_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data_point_create** | [**DataPointCreate**](DataPointCreate.md)|  | [optional] 

### Return type

[**DataPoint**](DataPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_metrics_data**
> Metrics partial_update_metrics_data(id, metrics=metrics)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.metrics import Metrics
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique integer value identifying this metrics data.
    metrics = xleap._client.Metrics() # Metrics |  (optional)

    try:
        api_response = api_instance.partial_update_metrics_data(id, metrics=metrics)
        print("The response of V1Api->partial_update_metrics_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->partial_update_metrics_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this metrics data. | 
 **metrics** | [**Metrics**](Metrics.md)|  | [optional] 

### Return type

[**Metrics**](Metrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_ml_model**
> MLModel partial_update_ml_model(id, ml_model=ml_model)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.ml_model import MLModel
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this ml model.
    ml_model = xleap._client.MLModel() # MLModel |  (optional)

    try:
        api_response = api_instance.partial_update_ml_model(id, ml_model=ml_model)
        print("The response of V1Api->partial_update_ml_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->partial_update_ml_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this ml model. | 
 **ml_model** | [**MLModel**](MLModel.md)|  | [optional] 

### Return type

[**MLModel**](MLModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_org_list**
> OrgList partial_update_org_list(id, org_list=org_list)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.org_list import OrgList
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 
    org_list = xleap._client.OrgList() # OrgList |  (optional)

    try:
        api_response = api_instance.partial_update_org_list(id, org_list=org_list)
        print("The response of V1Api->partial_update_org_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->partial_update_org_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org_list** | [**OrgList**](OrgList.md)|  | [optional] 

### Return type

[**OrgList**](OrgList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_project**
> Project partial_update_project(id, project=project)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.project import Project
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 
    project = xleap._client.Project() # Project |  (optional)

    try:
        api_response = api_instance.partial_update_project(id, project=project)
        print("The response of V1Api->partial_update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->partial_update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **project** | [**Project**](Project.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_prompt**
> Prompt partial_update_prompt(id, parent_id=parent_id, root_id=root_id, base_query=base_query, prompt=prompt)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.prompt import Prompt
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this prompt.
    parent_id = 'parent_id_example' # str | parent_id (optional)
    root_id = 'root_id_example' # str | root_id (optional)
    base_query = 'base_query_example' # str | base_query (optional)
    prompt = xleap._client.Prompt() # Prompt |  (optional)

    try:
        api_response = api_instance.partial_update_prompt(id, parent_id=parent_id, root_id=root_id, base_query=base_query, prompt=prompt)
        print("The response of V1Api->partial_update_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->partial_update_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this prompt. | 
 **parent_id** | **str**| parent_id | [optional] 
 **root_id** | **str**| root_id | [optional] 
 **base_query** | **str**| base_query | [optional] 
 **prompt** | [**Prompt**](Prompt.md)|  | [optional] 

### Return type

[**Prompt**](Prompt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_run**
> Run partial_update_run(id, parent_run_id=parent_run_id, session_name=session_name, root_node=root_node, run=run)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.run import Run
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this run.
    parent_run_id = 'parent_run_id_example' # str | parent_run_id (optional)
    session_name = 'session_name_example' # str | session_name (optional)
    root_node = 'root_node_example' # str | root_node (optional)
    run = xleap._client.Run() # Run |  (optional)

    try:
        api_response = api_instance.partial_update_run(id, parent_run_id=parent_run_id, session_name=session_name, root_node=root_node, run=run)
        print("The response of V1Api->partial_update_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->partial_update_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this run. | 
 **parent_run_id** | **str**| parent_run_id | [optional] 
 **session_name** | **str**| session_name | [optional] 
 **root_node** | **str**| root_node | [optional] 
 **run** | [**Run**](Run.md)|  | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_api_key**
> APIKey retrieve_api_key(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.api_key import APIKey
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_api_key(id)
        print("The response of V1Api->retrieve_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->retrieve_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**APIKey**](APIKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_chart_data**
> ChartData retrieve_chart_data(id, metric=metric, count=count)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.chart_data import ChartData
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 
    metric = 'metric_example' # str | metric (optional)
    count = 'count_example' # str | count (optional)

    try:
        api_response = api_instance.retrieve_chart_data(id, metric=metric, count=count)
        print("The response of V1Api->retrieve_chart_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->retrieve_chart_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **metric** | **str**| metric | [optional] 
 **count** | **str**| count | [optional] 

### Return type

[**ChartData**](ChartData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_point**
> DataPoint retrieve_data_point(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.data_point import DataPoint
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_data_point(id)
        print("The response of V1Api->retrieve_data_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->retrieve_data_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DataPoint**](DataPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_metrics_data**
> Metrics retrieve_metrics_data(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.metrics import Metrics
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique integer value identifying this metrics data.

    try:
        api_response = api_instance.retrieve_metrics_data(id)
        print("The response of V1Api->retrieve_metrics_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->retrieve_metrics_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this metrics data. | 

### Return type

[**Metrics**](Metrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_ml_model**
> MLModel retrieve_ml_model(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.ml_model import MLModel
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this ml model.

    try:
        api_response = api_instance.retrieve_ml_model(id)
        print("The response of V1Api->retrieve_ml_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->retrieve_ml_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this ml model. | 

### Return type

[**MLModel**](MLModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_org_detail**
> OrgDetail retrieve_org_detail(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.org_detail import OrgDetail
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_org_detail(id)
        print("The response of V1Api->retrieve_org_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->retrieve_org_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrgDetail**](OrgDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_project_detail**
> ProjectDetail retrieve_project_detail(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.project_detail import ProjectDetail
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_project_detail(id)
        print("The response of V1Api->retrieve_project_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->retrieve_project_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectDetail**](ProjectDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_prompt**
> Prompt retrieve_prompt(id, parent_id=parent_id, root_id=root_id, base_query=base_query)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.prompt import Prompt
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this prompt.
    parent_id = 'parent_id_example' # str | parent_id (optional)
    root_id = 'root_id_example' # str | root_id (optional)
    base_query = 'base_query_example' # str | base_query (optional)

    try:
        api_response = api_instance.retrieve_prompt(id, parent_id=parent_id, root_id=root_id, base_query=base_query)
        print("The response of V1Api->retrieve_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->retrieve_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this prompt. | 
 **parent_id** | **str**| parent_id | [optional] 
 **root_id** | **str**| root_id | [optional] 
 **base_query** | **str**| base_query | [optional] 

### Return type

[**Prompt**](Prompt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_run**
> Run retrieve_run(id, parent_run_id=parent_run_id, session_name=session_name, root_node=root_node)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.run import Run
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this run.
    parent_run_id = 'parent_run_id_example' # str | parent_run_id (optional)
    session_name = 'session_name_example' # str | session_name (optional)
    root_node = 'root_node_example' # str | root_node (optional)

    try:
        api_response = api_instance.retrieve_run(id, parent_run_id=parent_run_id, session_name=session_name, root_node=root_node)
        print("The response of V1Api->retrieve_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->retrieve_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this run. | 
 **parent_run_id** | **str**| parent_run_id | [optional] 
 **session_name** | **str**| session_name | [optional] 
 **root_node** | **str**| root_node | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stat_project**
> Project stat_project(id)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.project import Project
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.stat_project(id)
        print("The response of V1Api->stat_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->stat_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key_update**
> APIKeyUpdate update_api_key_update(id, api_key_update=api_key_update)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.api_key_update import APIKeyUpdate
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 
    api_key_update = xleap._client.APIKeyUpdate() # APIKeyUpdate |  (optional)

    try:
        api_response = api_instance.update_api_key_update(id, api_key_update=api_key_update)
        print("The response of V1Api->update_api_key_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_api_key_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **api_key_update** | [**APIKeyUpdate**](APIKeyUpdate.md)|  | [optional] 

### Return type

[**APIKeyUpdate**](APIKeyUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_point_create**
> DataPoint update_data_point_create(id, data_point_create=data_point_create)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.data_point import DataPoint
from xleap._client.models.data_point_create import DataPointCreate
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 
    data_point_create = xleap._client.DataPointCreate() # DataPointCreate |  (optional)

    try:
        api_response = api_instance.update_data_point_create(id, data_point_create=data_point_create)
        print("The response of V1Api->update_data_point_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_data_point_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data_point_create** | [**DataPointCreate**](DataPointCreate.md)|  | [optional] 

### Return type

[**DataPoint**](DataPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metrics_data**
> Metrics update_metrics_data(id, metrics=metrics)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.metrics import Metrics
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique integer value identifying this metrics data.
    metrics = xleap._client.Metrics() # Metrics |  (optional)

    try:
        api_response = api_instance.update_metrics_data(id, metrics=metrics)
        print("The response of V1Api->update_metrics_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_metrics_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this metrics data. | 
 **metrics** | [**Metrics**](Metrics.md)|  | [optional] 

### Return type

[**Metrics**](Metrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ml_model**
> MLModel update_ml_model(id, ml_model=ml_model)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.ml_model import MLModel
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this ml model.
    ml_model = xleap._client.MLModel() # MLModel |  (optional)

    try:
        api_response = api_instance.update_ml_model(id, ml_model=ml_model)
        print("The response of V1Api->update_ml_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_ml_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this ml model. | 
 **ml_model** | [**MLModel**](MLModel.md)|  | [optional] 

### Return type

[**MLModel**](MLModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_list**
> OrgList update_org_list(id, org_list=org_list)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.org_list import OrgList
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 
    org_list = xleap._client.OrgList() # OrgList |  (optional)

    try:
        api_response = api_instance.update_org_list(id, org_list=org_list)
        print("The response of V1Api->update_org_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_org_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org_list** | [**OrgList**](OrgList.md)|  | [optional] 

### Return type

[**OrgList**](OrgList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(id, project=project)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.project import Project
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | 
    project = xleap._client.Project() # Project |  (optional)

    try:
        api_response = api_instance.update_project(id, project=project)
        print("The response of V1Api->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **project** | [**Project**](Project.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prompt**
> Prompt update_prompt(id, parent_id=parent_id, root_id=root_id, base_query=base_query, prompt=prompt)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.prompt import Prompt
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this prompt.
    parent_id = 'parent_id_example' # str | parent_id (optional)
    root_id = 'root_id_example' # str | root_id (optional)
    base_query = 'base_query_example' # str | base_query (optional)
    prompt = xleap._client.Prompt() # Prompt |  (optional)

    try:
        api_response = api_instance.update_prompt(id, parent_id=parent_id, root_id=root_id, base_query=base_query, prompt=prompt)
        print("The response of V1Api->update_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this prompt. | 
 **parent_id** | **str**| parent_id | [optional] 
 **root_id** | **str**| root_id | [optional] 
 **base_query** | **str**| base_query | [optional] 
 **prompt** | [**Prompt**](Prompt.md)|  | [optional] 

### Return type

[**Prompt**](Prompt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run**
> Run update_run(id, parent_run_id=parent_run_id, session_name=session_name, root_node=root_node, run=run)





### Example


```python
import time
import os
import xleap._client
from xleap._client.models.run import Run
from xleap._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = xleap._client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with xleap._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xleap._client.V1Api(api_client)
    id = 'id_example' # str | A unique value identifying this run.
    parent_run_id = 'parent_run_id_example' # str | parent_run_id (optional)
    session_name = 'session_name_example' # str | session_name (optional)
    root_node = 'root_node_example' # str | root_node (optional)
    run = xleap._client.Run() # Run |  (optional)

    try:
        api_response = api_instance.update_run(id, parent_run_id=parent_run_id, session_name=session_name, root_node=root_node, run=run)
        print("The response of V1Api->update_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this run. | 
 **parent_run_id** | **str**| parent_run_id | [optional] 
 **session_name** | **str**| session_name | [optional] 
 **root_node** | **str**| root_node | [optional] 
 **run** | [**Run**](Run.md)|  | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

