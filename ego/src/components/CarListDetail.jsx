import { useParams } from 'react-router-dom';
import { useCarsContext } from "../context/CarsContext";

const CarListDetail = () => {
  const { cars } = useCarsContext();
  const { carID } = useParams();

  const vehicle = cars.find((car) => car.model === carID);
  if (!vehicle) {
    return <h2>Vehicle not found</h2>;
  }

  return (
    <>
      <div className='card-header container'>

        <img src={vehicle.img} alt={vehicle.model} />

        <div className="card-header-info">
          <h2>{vehicle.brand} {vehicle.model}</h2>
          <h3>{vehicle.title}</h3>
          <p>{vehicle.description}</p>
        </div>
      </div>
    </>
  );
}

export default CarListDetail;