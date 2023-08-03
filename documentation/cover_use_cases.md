*Api documentation avaible at ``/api/schema/swagger-ui/#/``*


## Table of Contents
- [User Registration](#user-registration)
- [User Login](#user-login)
- [Creating a Trip](#creating-a-trip)
- [Listing All Trips](#listing-all-trips)
- [Retrieving a Single Trip](#retrieving-a-single-trip)
- [Updating a Trip](#updating-a-trip)
- [Adding a Destination to a Trip](#adding-a-destination-to-a-trip)
- [Managing Cities](#managing-cities)
- [Managing Hotels](#managing-hotels)

---

### User Registration
To register a new user, send a POST request to the registration endpoint:

```
POST /api/auth/register/
```

The request body should include a JSON object with user details:

```json
{
  "username": "newuser",
  "password": "your_password",
  "password2": "your_password",
  "email": "newuser@example.com",
  "first_name": "jhon",
  "last_name": "smith"
}
```

### User Login
To log in, send a POST request to the login endpoint:

```
POST /api/auth/token/
```

The request body should include a JSON object with user credentials:

```json
{
	"username": "newuser",
	"password": "your_password"
}
```

The response will include the access and refresh JWT tokens. The access token can be used to authenticate future requests.


### Creating a Trip
To create a new trip, send a POST request to the trips endpoint:

```
POST /trips/
```

The request body should include a JSON object with trip details:

```json
{
	"title": "Italy Trip",
	"participants": [],
	"start_date": "2023-08-01",
	"end_date": "2023-08-15",
	"budget": "2000.00"
}
```


### Listing All Trips
To list all user's trips, send a GET request to the trips endpoint:

```
GET /trips/
```


### Retrieving a Single Trip
To retrieve details of a single trip, send a GET request to the specific trip endpoint with the trip ID:

```
GET /trips/<trip_id>/
```


### Updating a Trip
To update the details of a trip, send a PUT or PATCH request to the specific trip endpoint with the trip ID:

```
PUT /trips/<trip_id>/
```


### Adding a Destination to a Trip
To add a new destination to a trip, send a POST request to the destinations endpoint:

```
POST /destinations/
```

The request body should include a JSON object with destination details:

```json
{
	"trip": <trip_id>,
	"city": <city_id>,
	"arrival_date": "2023-08-01",
	"departure_date": "2023-08-05"
}

```

  
### Managing Cities
To create, view, update or delete cities, use the following endpoints:

- Create a new city: `POST /cities/`
- View all cities: `GET /cities/`
- View a single city: `GET /cities/<city_id>/`
- Update a city: `PUT /cities/<city_id>/`
- Delete a city: `DELETE /cities/<city_id>/`


### Managing Hotels
To create, view, update or delete hotels, use the following endpoints:

- Create a new hotel: `POST /hotels/`
- View all hotels: `GET /hotels/`
- View a single hotel: `GET /hotels/<hotel_id>/`
- Update a hotel: `PUT /hotels/<hotel_id>/`
- Delete a hotel: `DELETE /hotels/<hotel_id>/`

  
*Remember to include the `Authorization: Bearer <access_token>` header in requests that require authentication.*