
import { Routes, Route } from 'react-router-dom'
import './App.css'
//PAGES
import Home from './pages/Home'
//COMPONENTS
import Navbar from './components/Navbar'
import CarListDetail from './components/CarListDetail'
import Footer from './components/Footer'


function App() {

  return (
    <>
    <Navbar/>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/cars/:carID" element={<CarListDetail/>} />
      </Routes>
      <Footer/>
    </>
  )
}

export default App
