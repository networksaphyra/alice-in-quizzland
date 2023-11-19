import { Button } from '@mui/joy'
import { Link,  } from 'react-router-dom'
import '../Home.css'; // Make sure the correct path to the CSS file is here
import { useNavigate } from 'react-router-dom';

export const Home = () => {
    const history = useNavigate();
    return (
        <div className="container">
            <h1 className="title">Alice in Quizzland</h1>
            <button className="knock-button" onClick={() => history("/quiz")} >Knock to go in</button>
            <div className="rabbit rabbit-left"></div>
            <div className="rabbit rabbit-right"></div>
        </div>
    );
}