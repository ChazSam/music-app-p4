
import { useOutletContext } from "react-router-dom"
function Home(){
    const {user} = useOutletContext()
    // console.log(isLoggedIn, user)
    return(
        <>
            <h1>Home Page</h1>
            {/* {isLoggedIn && (
                <h2>Welcome {user.first_name}</h2>
            )} */}
            <h2>Welcome {user.first_name} to the Doctor medical system. Please login or search our doctors to find the best doctor for you!</h2>
            <p>If you're new here, please go to the sign up page and create an account</p>
            <p>If you have an account, go to the log in page and create an appointment</p>
        </>
    )
}

export default Home