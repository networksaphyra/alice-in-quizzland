import { Button } from '@mui/joy'
import { Link } from 'react-router-dom'

export const Home = () => {
    return <div className='Home'>
        <header>
            <h1>Welcome to the Wonderland of Quizzes!</h1>
        </header>
        <img className="logo" src="/logo.png" alt="logo" />
        <h2>Spend Less Time Finding Questions.</h2>
        <Link to="/quiz">
        <Button className="start" href='/quiz'>Click To Knock!</Button>
        </Link>
    </div>
}