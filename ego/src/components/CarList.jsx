import { useState } from "react";
import { Link } from "react-router-dom";
import { useCarsContext } from "../context/CarsContext";
import { CiMenuKebab } from 'react-icons/ci';

const CarList = () => {
    const { cars, setCars } = useCarsContext();

    const [filtro, setFiltro] = useState('all');
    const [orden, setOrden] = useState([]);
    const [isMenuVisible, setIsMenuVisible] = useState(false);
    const [openMenu, setOpenMenu] = useState(false);

    const handleFiltroClick = (valor) => {
        setFiltro(valor);
    };

    const handleToggleMenu = () => {
        setIsMenuVisible(!isMenuVisible);
    };

    const handleOpenFilter = () => {
        setOpenMenu(!openMenu);
    }

    const filterConditions = {
        'all': () => true,
        'car': car => car.category === 'car',
        'pickup': car => car.category === 'pickup' || car.category === 'comercial',
        'suv': car => car.category === 'suv' || car.category === 'cross',
    };

    const filteredCars = cars.filter(filterConditions[filtro] || (() => false));

    const handleOrdenar = (filtroOrden) => {
        let sorted = [...filteredCars];

        if (filtroOrden === "menorprice") {
            sorted.sort((a, b) => a.price - b.price);
        } else if (filtroOrden === "mayorprice") {
            sorted.sort((a, b) => b.price - a.price);
        } else if (filtroOrden === "nuevosPrimero") {
            sorted.sort((a, b) => b.year - a.year);
        } else if (filtroOrden === "viejosPrimero") {
            sorted.sort((a, b) => a.year - b.year);
        }

        setOrden(filtroOrden);
        setCars(sorted);
    };

    return (
        <>
            <section className="filters">
                <div className="filters-cat">
                    <p>Filtrar por</p> <CiMenuKebab onClick={handleOpenFilter} />
                    <ul className={`${openMenu ? 'cat-list' : 'd-none'}`} >
                        <li onClick={() => handleFiltroClick('all')}> Todos </li>
                        <li onClick={() => handleFiltroClick('car')}>Autos</li>
                        <li onClick={() => handleFiltroClick('pickup')} className="fil-btn">Pickups y Comerciales</li>
                        <li onClick={() => handleFiltroClick('suv')} className="fil-btn">SUVs y Crossovers</li>
                    </ul>
                </div>

                <div className="filters-order">
                    <p>Ordenar por</p> <CiMenuKebab onClick={handleToggleMenu} />
                    {isMenuVisible && (
                        <ul className={`${isMenuVisible ? 'filters-order-list' : 'd-none'}`}>
                            <li onClick={() => handleOrdenar('')}>Nada</li>
                            <li onClick={() => handleOrdenar("menorprice")}>De <b>menor</b> a <b>mayor</b> precio</li>
                            <li onClick={() => handleOrdenar("mayorprice")}>De <b>mayor</b> a <b>menor</b> precio</li>
                            <li onClick={() => handleOrdenar("nuevosPrimero")}>Más <b>nuevos</b> primero</li>
                            <li onClick={() => handleOrdenar("viejosPrimero")}>Más <b>viejos</b> primero</li>
                        </ul>
                    )}
                </div>
            </section>
            <section className="cards">
                {filteredCars.map((car) => (
                    <article key={car.id}>
                        <h2>{car.model}</h2>
                        <p>{car.year} | {car.price}</p>
                        <img src={car.img} alt={car.brand} />
                        <Link to={`/cars/${car.model}`}>Ver Modelo</Link>
                    </article>
                ))}
            </section>
        </>
    )
}

export default CarList;
