import { Button } from '@mui/joy'
import { Link } from 'react-router-dom'

export const Home = () => {
    return <div className='Home'>
        <h1>Quiz Maker</h1>
        <img className="logo" src="/logo.png" alt="logo" />
        <h2>Spend Less Time Finding Questions.</h2>
        <Link to="/quiz">
        <Button className="start" href='/quiz'>Start Now!</Button>
        </Link>
    </div>
}