## python-cam

A Python wrapper for the Cam API.

#### Quick links

- Users
    - [List users](#list-users)
    - [Read a single user](#read-a-user)
- Organizations
    - [List organizations](#list-organizations)
    - [Read an organization](#read-an-organization)
- Requests
    - [List requests](#list-requests)
    - [Read a request](#read-a-request)
    - [Create a network request](#create-a-network-request)
- Contributors
    - [List contributors](#list-contributors)
    - [Read a contributor](#read-a-contributor)
- Assets
    - [List assets](#list-assets)
    - [Read an asset](#read-an-asset)

#### Authentication

The Cam API makes use of API keys for authentication. To create your own API, open the Cam app, navigate to the API management page and create a new one.

All `python-cam` API calls must pass the API key:

```python
import cam
cam.api_key = 'your-api-key'
```

### Users

#### List users

- Ordering: `created`
- Filtering: none available
- Paging: `limit` (default: 50), `offset` (default: 0)

```python
import cam
response = cam.users.list({'limit': 10})
```

**Response**

```python
{
    'meta': {
        'limit': 10,
        'offset': 0,
        'total_count': 1
    },
    'objects': [{
        'uuid': 'b7a28f1c-2a09-4c7e-9238-f7e28faf83e3', 
        'created': '2019-10-09T14:31:45.255381Z', 
        'modified': '2019-10-09T14:31:45.588183Z', 
        'created_by': '/v1/users/b7a28f1c-2a09-4c7e-9238-f7e28faf83e3/', 
        'modified_by': '/v1/users/b7a28f1c-2a09-4c7e-9238-f7e28faf83e3/', 
        'email': 'peter@camayak.com', 
        'first_name': 'Peter Evans', 
        'last_name': 'Peter', 
        'display_name': 'Peter Evans', 
        'profile_picture': '', 
        'resource_uri': '/v1/users/b7a28f1c-2a09-4c7e-9238-f7e28faf83e3/'
    }]
}

```

#### Read a user

```python
import cam
response = cam.users.read('b7a28f1c-2a09-4c7e-9238-f7e28faf83e3')
```

**Response**

```python
{
    'uuid': 'b7a28f1c-2a09-4c7e-9238-f7e28faf83e3', 
    'created': '2019-10-09T14:31:45.255381Z', 
    'modified': '2019-10-09T14:31:45.588183Z', 
    'created_by': '/v1/users/b7a28f1c-2a09-4c7e-9238-f7e28faf83e3/', 
    'modified_by': '/v1/users/b7a28f1c-2a09-4c7e-9238-f7e28faf83e3/', 
    'email': 'peter@camayak.com', 
    'first_name': 'Peter Evans', 
    'last_name': 'Peter', 
    'display_name': 'Peter Evans', 
    'profile_picture': '', 
    'resource_uri': '/v1/users/b7a28f1c-2a09-4c7e-9238-f7e28faf83e3/'
}
```

### Organizations

#### List organizations

- Ordering: `created`
- Filtering: none available
- Paging: `limit` (default: 50), `offset` (default: 0)

```python
import cam
response = cam.organizations.list({'limit': 10})
```

**Response**

```python
{
    'meta': {
        'limit': 10,
        'offset': 0,
        'total_count': 1
    },
    'objects': [{
        'uuid': 'b0b9844e-ce79-4b88-9939-5b3a63ef7ce3', 
        'created': '2019-07-02T10:23:58.866772Z', 
        'modified': '2019-07-29T09:45:33.408992Z', 
        'created_by': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
        'modified_by': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
        'name': 'Camayak Inc.', 
        'owner': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
        'resource_uri': '/v1/organizations/b0b9844e-ce79-4b88-9939-5b3a63ef7ce3/'
    }]
}
```

#### Read an organization

```python
import cam
response = cam.organizations.read('b0b9844e-ce79-4b88-9939-5b3a63ef7ce3')
```

**Response**

```python
{
    'uuid': 'b0b9844e-ce79-4b88-9939-5b3a63ef7ce3', 
    'created': '2019-07-02T10:23:58.866772Z', 
    'modified': '2019-07-29T09:45:33.408992Z', 
    'created_by': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
    'modified_by': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
    'name': 'Camayak Inc.', 
    'owner': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
    'resource_uri': '/v1/organizations/b0b9844e-ce79-4b88-9939-5b3a63ef7ce3/'
}
```

### Requests

#### List requests

- Ordering: `created`
- Filtering: none available
- Paging: `limit` (default: 50), `offset` (default: 0)

```python
import cam
response = cam.requests.list({'limit': 10})
```

**Response**

```python
{
    'meta': {
        'limit': 10, 
        'offset': 0,
        'total_count': 1
    },
    'objects': [{
        'uuid': '81a1de6e-4df0-4e95-9a22-fb9fc9a518d7', 
        'created': '2019-10-15T13:18:52.050928Z', 
        'modified': '2019-10-15T13:18:52.050911Z', 
        'created_by': {
            'uuid': '1e9e6d2d-582e-47df-a181-4906040b7da6', 
            'created': '2019-10-02T11:20:14.479127Z', 
            'modified': '2019-10-15T13:18:52.047903Z', 
            'created_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
            'modified_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
            'email': 'peter@camayak.com', 
            'first_name': '', 
            'last_name': '', 
            'display_name': 'Peter Evans', 
            'profile_picture': '', 
            'resource_uri': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/'
        }, 
        'modified_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
        'is_trash': False, 
        'title': 'Rugby World Cup - ENG vs. FR', 
        'mime_types': ['image/*'], 
        'is_network': True, 
        'instructions': 'I need photos of the ENG vs. FR Rugby World Cup game.', 
        'expires': '2019-10-29T13:18:51.723120+00:00', 
        'event_start_date': None, 
        'contributors': [], 
        'pending_verification': True, 
        'subscription_metadata': {}, 
        'organization': {
            'uuid': 'b0b9844e-ce79-4b88-9939-5b3a63ef7ce3', 
            'created': '2019-07-02T10:23:58.866772Z', 
            'modified': '2019-07-29T09:45:33.408992Z', 
            'created_by': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
            'modified_by': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
            'name': 'Camayak Inc.', 
            'owner': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
            'resource_uri': '/v1/organizations/b0b9844e-ce79-4b88-9939-5b3a63ef7ce3/'
        },
        'resource_uri': '/v1/requests/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/'
    }]
}
```

#### Read a request

```python
import cam
response = cam.requests.read('81a1de6e-4df0-4e95-9a22-fb9fc9a518d7')
```

**Response**

```python
{
    'uuid': '81a1de6e-4df0-4e95-9a22-fb9fc9a518d7', 
    'created': '2019-10-15T13:18:52.050928Z', 
    'modified': '2019-10-15T13:18:52.050911Z', 
    'created_by': {
        'uuid': '1e9e6d2d-582e-47df-a181-4906040b7da6', 
        'created': '2019-10-02T11:20:14.479127Z', 
        'modified': '2019-10-15T13:18:52.047903Z', 
        'created_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
        'modified_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
        'email': 'peter@camayak.com', 
        'first_name': '', 
        'last_name': '', 
        'display_name': 'Peter Evans', 
        'profile_picture': '', 
        'resource_uri': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/'
    }, 
    'modified_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
    'is_trash': False, 
    'title': 'Rugby World Cup - ENG vs. FR', 
    'mime_types': ['image/*'], 
    'is_network': True, 
    'instructions': 'I need photos of the ENG vs. FR Rugby World Cup game.', 
    'expires': '2019-10-29T13:18:51.723120+00:00', 
    'event_start_date': None, 
    'contributors': [], 
    'pending_verification': True, 
    'subscription_metadata': {}, 
    'organization': {
        'uuid': 'b0b9844e-ce79-4b88-9939-5b3a63ef7ce3', 
        'created': '2019-07-02T10:23:58.866772Z', 
        'modified': '2019-07-29T09:45:33.408992Z', 
        'created_by': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
        'modified_by': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
        'name': 'Camayak Inc.', 
        'owner': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
        'resource_uri': '/v1/organizations/b0b9844e-ce79-4b88-9939-5b3a63ef7ce3/'
    },
    'resource_uri': '/v1/requests/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/'
}
```

#### Create a network request

```python
import cam
response = cam.requests.create({
    'created_by': {
        'display_name': 'Peter Evans',
        'email': 'peter@camayak.com'
    },
    'title': 'Rugby World Cup - ENG vs. FR',
    'instructions': 'I need photos of the ENG vs. FR Rugby World Cup game.',
    'mime_types': ['image/*'],
    'is_network': True
})
```

**Response**

```python
{
    'uuid': '81a1de6e-4df0-4e95-9a22-fb9fc9a518d7', 
    'created': '2019-10-15T13:18:52.050928Z', 
    'modified': '2019-10-15T13:18:52.050911Z', 
    'created_by': {
        'uuid': '1e9e6d2d-582e-47df-a181-4906040b7da6', 
        'created': '2019-10-02T11:20:14.479127Z', 
        'modified': '2019-10-15T13:18:52.047903Z', 
        'created_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
        'modified_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
        'email': 'peter@camayak.com', 
        'first_name': '', 
        'last_name': '', 
        'display_name': 'Peter Evans', 
        'profile_picture': '', 
        'resource_uri': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/'
    }, 
    'modified_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
    'is_trash': False, 
    'title': 'Rugby World Cup - ENG vs. FR', 
    'mime_types': ['image/*'], 
    'is_network': True, 
    'instructions': 'I need photos of the ENG vs. FR Rugby World Cup game.', 
    'expires': '2019-10-29T13:18:51.723120+00:00', 
    'event_start_date': None, 
    'contributors': [], 
    'pending_verification': True, 
    'subscription_metadata': {}, 
    'organization': {
        'uuid': 'b0b9844e-ce79-4b88-9939-5b3a63ef7ce3', 
        'created': '2019-07-02T10:23:58.866772Z', 
        'modified': '2019-07-29T09:45:33.408992Z', 
        'created_by': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
        'modified_by': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
        'name': 'Camayak Inc.', 
        'owner': '/v1/users/742ac8e0-09ce-4114-a167-9859d151bd9f/', 
        'resource_uri': '/v1/organizations/b0b9844e-ce79-4b88-9939-5b3a63ef7ce3/'
    },
    'resource_uri': '/v1/requests/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/'
}
```

### Contributors

#### List contributors

- Ordering: `created`
- Filtering: `request`
- Paging: `limit` (default: 50), `offset` (default: 0)

```python
import cam
response = cam.contributors.list({'request': '9da6ab1e-97e4-49c0-9d2f-24e9972eafd9'})
```

**Response**

```python
{
    'meta': {
        'limit': 50,
        'offset': 0,
        'total_count': 1
    },
    'objects': [{
        'uuid': '6c7faa16-3942-40b8-9af8-e88aaca2984f',
        'created': '2019-10-02T13:44:07.872374Z', 
        'modified': '2019-10-02T13:44:07.873160Z', 
        'created_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
        'modified_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
        'is_trash': False,
        'email': 'peter@camayak.com',
        'upload_count': 0, 
        'user': {
            'uuid': '21a98076-9d6a-46c8-ba5b-d1b2f1174447', 
            'created': '2019-06-28T12:05:10.288780Z', 
            'modified': '2019-10-02T13:45:54.782317Z', 
            'created_by': '/v1/users/21a98076-9d6a-46c8-ba5b-d1b2f1174447/', 
            'modified_by': '/v1/users/21a98076-9d6a-46c8-ba5b-d1b2f1174447/', 
            'email': 'peter@camayak.com', 
            'first_name': 'Peter', 
            'last_name': 'Evans', 
            'display_name': 'Peter Evans', 
            'profile_picture': '', 
            'resource_uri': '/v1/users/21a98076-9d6a-46c8-ba5b-d1b2f1174447/'
        }, 
        'request': '/v1/requests/9da6ab1e-97e4-49c0-9d2f-24e9972eafd9/',
        'resource_uri': '/v1/request_contributors/6c7faa16-3942-40b8-9af8-e88aaca2984f/'
    }]
}
```

#### Read a contributor

```python
import cam
response = cam.contributors.read('6c7faa16-3942-40b8-9af8-e88aaca2984f')
```

**Response**

```python
{
    'uuid': '6c7faa16-3942-40b8-9af8-e88aaca2984f',
    'created': '2019-10-02T13:44:07.872374Z', 
    'modified': '2019-10-02T13:44:07.873160Z', 
    'created_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
    'modified_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
    'is_trash': False,
    'email': 'peter@camayak.com',
    'upload_count': 0, 
    'user': {
        'uuid': '21a98076-9d6a-46c8-ba5b-d1b2f1174447', 
        'created': '2019-06-28T12:05:10.288780Z', 
        'modified': '2019-10-02T13:45:54.782317Z', 
        'created_by': '/v1/users/21a98076-9d6a-46c8-ba5b-d1b2f1174447/', 
        'modified_by': '/v1/users/21a98076-9d6a-46c8-ba5b-d1b2f1174447/', 
        'email': 'peter@camayak.com', 
        'first_name': 'Peter', 
        'last_name': 'Evans', 
        'display_name': 'Peter Evans', 
        'profile_picture': '', 
        'resource_uri': '/v1/users/21a98076-9d6a-46c8-ba5b-d1b2f1174447/'
    }, 
    'request': '/v1/requests/9da6ab1e-97e4-49c0-9d2f-24e9972eafd9/',
    'resource_uri': '/v1/request_contributors/6c7faa16-3942-40b8-9af8-e88aaca2984f/'
}
```

### Assets

#### List assets

- Ordering: `created`
- Filtering: `request`
- Paging: `limit` (default: 50), `offset` (default: 0)

```python
import cam
response = cam.assets.list({'request': '81a1de6e-4df0-4e95-9a22-fb9fc9a518d7'})
```

**Response**

```python
{
    'meta': {
        'limit': 50,
        'offset': 0,
        'total_count': 1
    },
    'objects': [{
        'uuid': 'cc7d5956-930a-415b-8c89-e0fbdc667b33', 
        'created': '2019-10-15T13:42:34.084457Z', 
        'modified': '2019-10-15T13:42:34.084428Z', 
        'created_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
        'modified_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
        'is_trash': False, 
        'title': 'A rugby tackle', 
        'credit': 'Peter Evans', 
        'status': 'success', 
        'filename': 'tackle.png', 
        'mime_type': 'image/png', 
        'description': 'A photo of a rugby player being tackled at the World Cup', 
        'source': '1e9e6d2d-582e-47df-a181-4906040b7da6/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/cc7d5956-930a-415b-8c89-e0fbdc667b33.png', 
        'thumbnails': {
            'mid': '1e9e6d2d-582e-47df-a181-4906040b7da6/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/cc7d5956-930a-415b-8c89-e0fbdc667b33-mid.png', 
            'grid': '1e9e6d2d-582e-47df-a181-4906040b7da6/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/cc7d5956-930a-415b-8c89-e0fbdc667b33-grid.png'
        }, 
        'request': '/v1/requests/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/', 
        'resource_uri': '/v1/assets/cc7d5956-930a-415b-8c89-e0fbdc667b33/'
    }]
}
```

#### Read an asset

```python
import cam
response = cam.assets.read('cc7d5956-930a-415b-8c89-e0fbdc667b33')
```

**Response**

```python
{
    'uuid': 'cc7d5956-930a-415b-8c89-e0fbdc667b33', 
    'created': '2019-10-15T13:42:34.084457Z', 
    'modified': '2019-10-15T13:42:34.084428Z', 
    'created_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
    'modified_by': '/v1/users/1e9e6d2d-582e-47df-a181-4906040b7da6/', 
    'is_trash': False, 
    'title': 'A rugby tackle', 
    'credit': 'Peter Evans', 
    'status': 'success', 
    'filename': 'tackle.png', 
    'mime_type': 'image/png', 
    'description': 'A photo of a rugby player being tackled at the World Cup', 
    'source': '1e9e6d2d-582e-47df-a181-4906040b7da6/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/cc7d5956-930a-415b-8c89-e0fbdc667b33.png', 
    'thumbnails': {
        'mid': '1e9e6d2d-582e-47df-a181-4906040b7da6/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/cc7d5956-930a-415b-8c89-e0fbdc667b33-mid.png', 
        'grid': '1e9e6d2d-582e-47df-a181-4906040b7da6/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/cc7d5956-930a-415b-8c89-e0fbdc667b33-grid.png'
    }, 
    'request': '/v1/requests/81a1de6e-4df0-4e95-9a22-fb9fc9a518d7/', 
    'resource_uri': '/v1/assets/cc7d5956-930a-415b-8c89-e0fbdc667b33/'
}
```
