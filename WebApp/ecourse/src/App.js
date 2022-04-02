import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Header from './layout/Header';
import Footer from './layout/Footer';
import Home from './compoments/Home';
import Lesson from './compoments/Lesson';
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => {
  return (
    <BrowserRouter>
    <Header />
    
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/courses/:courseId/lessons" element={<Lesson/>} />
    </Routes>

    <Footer />

  </BrowserRouter>
  )
}

export default App;