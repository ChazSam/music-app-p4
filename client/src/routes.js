import Home from "./pages/Home";
import Doctors from "./pages/ListDoctors";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Appointment from "./pages/Appointment";
import ErrorPage from "./pages/ErrorPage";
import Account from "./pages/Account"
import App from "./components/App";
import AddDoctor from "./pages/AddDoctor"
import EditDoctor from "./pages/EditDoctor"
import Admin from "./pages/Admin"
import EditPatient from './pages/EditPatient'
import EditAppointment from './pages/EditAppointment'
import Review from "./pages/Review"
import EditReview from "./pages/EditReview"

const routes = [

    {
        path: "/",
        element: <App />,
        errorElement: <ErrorPage/>,
        children: [
            {
                path: "/",
                element: <Home />,
            },
            {
                path: "/doctors",
                element: <Doctors />,
    
            },
            {
                path: "/login",
                element: <Login  />,

            },
            {
                path: "/signup",
                element: <Signup />,
            
            },
            {
                path: "/appointment",
                element: <Appointment />,
        
            },
            
            {
                path: "/account",
                element: <Account />,
            
            },
            {
                path: "/account/settings",
                element: <EditPatient />,
            
            },
            {
                path: "/account/appointment",
                element: <EditAppointment />,
            
            },
            {
                path: "/account/edit-review",
                element: <EditReview />,
            
            },
            {
                path: "/account/reviews",
                element: <Review />,
            
            },
            {
                path: "/admin",
                element: <Admin />,
            
            },
            {
                path: '/admin/add-doctor',
                element: <AddDoctor/>
            }, 
            {
                path: '/admin/edit-doctor',
                element: <EditDoctor/>
            }
        ]

    },
]

export default routes