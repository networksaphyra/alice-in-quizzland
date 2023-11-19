import { Button } from '@mui/joy'
import { Link } from 'react-router-dom'
import { useState } from 'react'
export const Home = () => {

    return <div className='Home'>
        <img className="bg" style={{width: "100vw", opacity: 0.5}} src="background.jpg" />
        <div className='frame'>
            <img className='frameImg' src="frame.png"/>
            
        </div>
    </div>
}