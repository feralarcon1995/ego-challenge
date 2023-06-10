/* eslint-disable react-refresh/only-export-components */
/* eslint-disable react/prop-types */
import { createContext, useContext, useState, useEffect } from 'react';
import { getAllCars } from '../data/api';

const CarsContext = createContext();
export const useCarsContext = () => useContext(CarsContext);

const CarsContextProvider = ({ children }) => {

    const [cars, setCars] = useState([]);

    useEffect(() => {
        async function loadCars() {
            const res = await getAllCars();
            setCars(res.data);
            console.log(res.data);
        }
        loadCars();
    }, []);

    
    return (
        <CarsContext.Provider value={{
            cars,
            setCars,
        }}>
            {children}
        </CarsContext.Provider>
    )
}

export default CarsContextProvider