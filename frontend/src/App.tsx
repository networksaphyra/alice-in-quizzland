import React from 'react';
import './App.css';
import { Navbar } from './components/Navbar';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Home } from './pages/Home';
import { Quiz } from './pages/Quiz';
import { Statistics } from './pages/Statistics';
import { Practice } from './pages/Practice';

const App = () => {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
                  <Route path='/' element={<Home />} />
                  <Route path='/quiz' element={<Quiz />} />
                  <Route path='/practice' element={<Practice />} />
                  <Route path='/stats' element={<Statistics />} />
              </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
