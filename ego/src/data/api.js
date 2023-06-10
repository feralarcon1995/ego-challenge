import axios from 'axios';

export const getAllCars = () => {
  return axios.get('http://127.0.0.1:8000/cars/')
}

export async function getCategory(category) {
  try {
    const response = await axios.get(`/cars/category/${category}/`);
    return response.data;
  } catch (error) {
    throw new Error('Error al obtener los datos de la categoría');
  }
}