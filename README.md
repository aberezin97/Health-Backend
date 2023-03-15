
# Health (Backend)

Backend part of Health application


## Demo

https://another-health.herokuapp.com


## API Reference

#### Sign In

```http
  POST /api/user/signin/
```

| Parameter  | Type     | Description             |
|:-----------|:---------|:------------------------|
| `username` | `string` | Username (**Required**) |
| `password` | `string` | Password (**Required**) |

#### Sign Up

```http
  POST /api/user/signup/
```

| Parameter    | Type     | Description               |
|:-------------|:---------|:--------------------------|
| `username`   | `string` | Username (**Required**)   |
| `email`      | `string` | Email (**Required**)      |
| `first_name` | `string` | First name (**Required**) |
| `last_name`  | `string` | Last name (**Required**)  |
| `password`   | `string` | Password (**Required**)   |


#### Activate user

```http
  PUT /api/user/activate/${uidb64}/${token}/
```

#### Delete user

```http
  DELETE /api/user/delete/
```

| Parameter  | Type     | Description                     |
|:-----------|:---------|:--------------------------------|
| `password` | `string` | Current password (**Required**) |

#### Get User Products

```http
  GET /api/user/products/
```

#### Add, Modify User Product

```http
  POST /api/user/products/
  PUT /api/user/products/${id}/
```

| Parameter       | Type     | Description                                 |
|:----------------|:---------|:--------------------------------------------|
| `name`          | `string` | Name of the product (**Required**)          |
| `calories`      | `number` | Calories of the product (**Required**)      |
| `proteins`      | `number` | Proteins of the product (**Required**)      |
| `fats`          | `number` | Fats of the product (**Required**)          |
| `carbohydrates` | `number` | Carbohydrates of the product (**Required**) |

#### Get, Delete User Product

```http
  GET /api/user/products/${id}/
  DELETE /api/user/products/${id}/
```

#### Send Password Reset Link

```http
  POST /api/user/password_reset/
```

| Parameter | Type     | Description                  |
|:----------|:---------|:-----------------------------|
| `email`   | `string` | Current email (**Required**) |

#### Reset Password

```http
  POST /api/user/password_reset/confirm/
```

| Parameter  | Type     | Description                 |
|:-----------|:---------|:----------------------------|
| `password` | `string` | New password (**Required**) |
| `token`    | `string` | Token (**Required**)        |

#### Change User Password

```http
  PUT /api/user/change_password/
```

| Parameter      | Type     | Description                 |
|:---------------|:---------|:----------------------------|
| `old_password` | `string` | Old password (**Required**) |
| `new_password` | `string` | New password (**Required**) |

#### Change User Data

```http
  PUT /api/user/change_data/
```

| Parameter    | Type     | Description                   |
|:-------------|:---------|:------------------------------|
| `username`   | `string` | New username (**Required**)   |
| `first_name` | `string` | New first name (**Required**) |
| `last_name`  | `string` | New last name (**Required**)  |

#### Change User Image

```http
  PUT /api/user/change_image/
```

| Parameter | Type   | Description              |
|:----------|:-------|:-------------------------|
| `image`   | `data` | New image (**Required**) |

#### Get Stats

```http
  GET /api/stats/
```

#### Get Weight Entries

```http
  GET /api/weight/
```

#### Add, Modify Weight Entry

```http
  POST /api/weight/
  PUT /api/weight/${id}/
```

| Parameter | Type     | Description           |
|:----------|:---------|:----------------------|
| `date`    | `string` | Date (**Required**)   |
| `weight`  | `number` | Weight (**Required**) |

#### Get, Delete Weight Entry

```http
  GET /api/weight/${id}/
  DELETE /api/weight/${id}/
```

#### Get Nutrition Entries

```http
  GET /api/nutrition/
  GET /api/nutrition/${year}/${month}/${day}/
```

#### Add, Modify Nutrition Entry

```http
  POST /api/nutrition/
  POST /api/nutrition/${year}/${month}/${day}/
  PUT /api/nutrition/${id}/
```

| Parameter       | Type     | Description                                 |
|:----------------|:---------|:--------------------------------------------|
| `name`          | `string` | Name of the product (**Required**)          |
| `time`          | `string` | Time of intake (**Required**)               |
| `calories`      | `number` | Calories of the product (**Required**)      |
| `proteins`      | `number` | Proteins of the product (**Required**)      |
| `fats`          | `number` | Fats of the product (**Required**)          |
| `carbohydrates` | `number` | Carbohydrates of the product (**Required**) |
| `weight`        | `number` | Weight of the product (**Required**)        |

#### Get, Delete Nutrition Entry

```http
  GET /api/nutrition/${id}/
  DELETE /api/nutrition/${id}/
```

#### Modify Nutrition Goals

```http
  PUT /api/nutrition/modify_goals/
  PUT /api/nutrition/${year}/${month}/${day}/modify_goals/
```

| Parameter            | Type     | Description                        |
|:---------------------|:---------|:-----------------------------------|
| `limitCalories`      | `number` | Limit calories (**Required**)      |
| `goalCalories`       | `number` | Goal calories (**Required**)       |
| `limitProteins`      | `number` | Limit proteins (**Required**)      |
| `goalProteins`       | `number` | Goal proteins (**Required**)       |
| `limitFats`          | `number` | Limit fats (**Required**)          |
| `goalFats`           | `number` | Goal fats (**Required**)           |
| `limitCarbohydrates` | `number` | Limit carbohydrates (**Required**) |
| `goalCarbohydrates`  | `number` | Goal carbohydrates (**Required**)  |