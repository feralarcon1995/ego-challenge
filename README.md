
<p align="center">
 <img width="600" height="200" src="./media/egologo.jpg"> 
</p> 
<p align="center">
 EGO CHALLENGE
</p> 
Esta API fue desarrollada en Django y proporciona endpoints para realizar operaciones CRUD en relación a los vehiculos de Toyota. 

## Requisitos:

Antes de comenzar, asegúrate de tener las siguientes aplicaciones instalados en tu sistema:

- [Python (versión 3.10.8) o superior.](https://www.python.org/downloads/)
- [Django ](https://www.djangoproject.com/download/)
- [NodeJS](https://nodejs.org/en/download)

## Pasos para comenzar:
#### Clonamos el repositorio dentro una carpeta en nuestra computadora:
```bash
git clone https://github.com/feralarcon1995/ego-challenge
```
- Una vez abierto el proyecto, abrimos una consola y navegamos hasta la ruta del proyecto

#### Creamos un entorno virtual:
```bash
 python -m venv venv
```
#### Lo activamos:
```bash
 source venv/bin/activate
```
#### Instala las dependencias del proyecto:
```bash
 pip install -r requirements.txt
```
#### Corremos la base de datos:
```bash
 python manage.py migrate
```
#### Levantamos el servidor:
```bash
 python manage.py runserver
```
#### Accede al proyecto en el navegador desde:
```bash
http://localhost:8000/
```
# PLUS FRONTEND

#### Se creo una aplicacion usando **ReactJS** para probar la **API**, utilizando el diseño proporcionado en figma.

#### Dentro del proyecto nos movemos a la carpeta front:
```bash
 cd ego
```
#### Instalamos dependencias:
```bash
 npm install
```
#### Levantamos aplicacion:
```bash
 npm run dev
```
#### Accede al proyecto en el navegador desde:
```bash
http://localhost:5173/
```
# ENDPOINTS Reference
 A continuación se detalla la funcionalidad de cada uno de los endpoints disponibles:

#### Get all cars
```http
GET /cars/
```

#### Read Car 

```http
GET /cars/${id}/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id` **Required**| `string` |  A unique integer value identifying this cars. |

#### Get Category

```http
GET /cars/category/{category}/
```

#### Get List Ordered

```http
GET /cars/ordered-by/{order_by}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `order_by` **Required**| `string` |  |

#### Update Car

```http
PUT /cars/${id}/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id` **Required**| `string` |  A unique integer value identifying this cars. |

```javascript
{
"id": 1,
"brand": "Marca del vehiculo",
"model": "Modelo del vehiculo",
"category": "Categoria del vehiculo",
"img": "Imagen del vehiculo,
"title": "Titulo del vehiuculo",
"description": "Descripcción del vehiculo",
"year": 2019,
"price": 815900
}
```

#### Partial Update Car

```http
PATCH /cars/${id}/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id` **Required**| `string` |  A unique integer value identifying this cars. |

```javascript
{
"id": 1,
"brand": "Marca del vehiculo",
"model": "Modelo del vehiculo",
"category": "Categoria del vehiculo",
"img": "Imagen del vehiculo,
"title": "Titulo del vehiuculo",
"description": "Descripcción del vehiculo",
"year": 2019,
"price": 815900
}
```
#### Delete Car

```http
DELETE /cars/${id}/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id` **Required**| `string` |  A unique integer value identifying this cars. |
