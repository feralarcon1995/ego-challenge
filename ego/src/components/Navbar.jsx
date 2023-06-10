import { useState } from "react";
import { Link, useLocation } from "react-router-dom"
import Logo from '../assets/logo.jpeg';
import { BiMenu } from 'react-icons/bi';
import { GrFormClose } from 'react-icons/gr';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  }

  return (
    <header >
      <nav>
        <Link to="/" ><img src={Logo} alt="Ego Logo" className="nav__brand" /></Link>
        <div className="nav__links">
          <Link className={location.pathname === '/' ? 'active' : ''} to="/">Modelos</Link>
          {location.pathname === '/' ? '' : <Link className={location.pathname !== '/' ? 'active' : ''}>Ficha de modelo</Link>}
        </div>
        <div className="nav__links">
          <Link onClick={toggleMenu}>
            Menú <BiMenu />
          </Link>
        </div>
      </nav>
      <div className={`${isOpen ? 'bg-op' : ''}`}></div>
      <div className={`nav__list ${isOpen ? 'active' : ''}`}>
        <Link className="close" onClick={toggleMenu}>
          Cerrar <GrFormClose />
        </Link>
        <ul>
          <li>
            <Link to="/">Modelos</Link>
          </li>
          <li>Servicios y Accesorios</li>
          <li>Financiación</li>
          <li>Reviews y Comunidad</li>
        </ul>
        <ul>
          <li>Toyota Mobility Service</li>
          <li>Toyota Gazoo Racing</li>
          <li>Toyota Híbridos</li>
        </ul>
        <ul>
          <li>Concesionarios</li>
          <li>Test Drive</li>
          <li>Contacto</li>
        </ul>
        <ul>
          <li>Actividades</li>
          <li>Servicios al Cliente</li>
          <li>Ventas Especiales</li>
          <li>Ventas Especiales</li>
          <li>Prensa</li>
          <li>Acerca de...</li>
        </ul>
      </div>


    </header>
  )
}

export default Navbar