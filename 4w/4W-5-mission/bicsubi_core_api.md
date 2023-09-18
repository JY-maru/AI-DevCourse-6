# BigSuBi API Documentation

API for managing books in a bookstore.

## Base URL
http://127.0.0.1:5000/

## Endpoints
- get your Git ID
- return query STRING
- weapon CRUD

---
### Get my Git ID
- **HTTP Method**: `GET`
- **Endpoint**: `/whoami`

#### Description
Returns my Git ID

#### Response
- **Status Code**: 200 OK
- **Response Format**: JSON

---

### return query STRING
- **HTTP Method**: `GET`
- **Endpoint**: `/echo?string="string"`

#### Description
Return `"string"`

#### Response
- **Status Code**: 200 OK
- **Response Format**: JSON

#### Example Request
```
GET /echo?string=AiDev6
```
#### Example Response
```
{
    "value": "AiDev6"
}
```
---
## weapon CRUD
- Create: Add a new weapon
- Read: Read the currently existing weapon
- Update: Change a specific attribute (name, quantity) in the currently existing weapon.
- Delete: Delete a specific weapon that currently exists

### Create
- **HTTP Method**: `POST`
- **Endpoint**: `/weapon`
#### Example Request
```
POST /weapon
```
#### Example Response
```
[
    [
        "k2",
        2
    ]
]
```

### Read
- **HTTP Method**: `GET`
- **Endpoint**: `/weapon`
#### parameters
- `name` : weapon's name
- `stock` : a number of weapon
#### Example Request
```
GET /weapon
```
#### Example Response
```
[
    [
        "k2",
        2
    ]
]
```
### Update
- **HTTP Method**: `PUT`
- **Endpoint**: `/weapon/{name}`
#### parameters
- `stock` : a number of weapon
#### Example Request
```
PUT /weapon/k2
```
#### Example Response
```
[
    [
        "k2",
        5
    ]
]
```


### Delete
- **HTTP Method**: `DELETE`
- **Endpoint**: `/weapon/{name}`
#### parameters
- `stock` : a number of weapon
#### Example Request
```
PUT /weapon/k2
```
#### Example Response
```
[
    [
        "k2",
        5
    ]
]
```