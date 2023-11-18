import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Home } from './pages/Home';
import { Quiz } from './pages/Quiz';

const App = () => {
  return (
    <div className="App">
      <BrowserRouter>
        <Navbar></Navbar>
        <Routes>
                  <Route path='/' element={<Home />} />
                  <Route path='/quiz' element={<Quiz />} />
              </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
