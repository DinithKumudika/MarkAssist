import React,{useState} from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { FcGoogle } from "react-icons/fc";
import Logo from '../photos/loginLogo.png'
import InputField from '../Components/InputField';
import SubmitButton from '../Components/SubmitButton';
import classnames from 'classnames';
// import { AuthContext } from '../Contexts/AuthContext';
import axios from 'axios';
import jwt_decode from "jwt-decode";
function Login(){
    const navigate = useNavigate();

    const classes= classnames('rounded shadow shadow-gray-400 w-full h-9 p-2 mb-4');

    const handleClick=()=>{
        alert("clicked");
    }

    // const {auth, setAuth} = useContext(AuthContext)

    const [formData , setFormData] = useState({
        username: '',
        password: '',
    });

    const { username, password } = formData;

    const [error, setError] = useState();

    const onChange =(event) =>{
        setFormData((prevState)=>({
            ...prevState,
            [event.target.name]: event.target.value
        }))
    }

    const handleSubmit = async (event)=>{
        event.preventDefault();
        // console.log(formData);
        const loginData = new FormData();
        loginData.append('username', formData.username);
        loginData.append('password', formData.password);
        console.log(formData)
        try{
            const response = await axios.post('http://127.0.0.1:8000/api_v1/auth/token',loginData);
            
            const allItems = jwt_decode(response.data.access_token);
            localStorage.setItem('accessToken', response.data.access_token)
            localStorage.setItem('tokenData', JSON.stringify(allItems));

            console.log(localStorage.getItem('tokenData'));
            console.log(localStorage.getItem('accessToken'));

            switch (allItems['user_role']) {
                case "student":
                    navigate('/subjects');
                    break;
                case "teacher":
                    navigate('/subjects');
                    break;
                case "admin":
                    navigate('/admin/dashboard');
                    break;
                default:
                    break;
            }
        }catch(error){
            // console.log("error:"+error.response.data.message);
            if(error.response && error.response.status >=400 && error.response.status <500){
                // console.log(error.response.data.message);
                setError(error.response.data.message);
            }
        }
    }


    return (
        <div className="flex items-center justify-center h-full bg-sky-100">
            <div className="flex flex-col items-center h-screen px-10 py-10 rounded-sm shadow shadow-gray-600 w-96 bg-sky-50">
                <div className="w-5/12 mt-10 mb-10"><img src={Logo} alt="Logo"/></div>
                <div className="flex items-center w-3/4 rounded-sm shadow shadow-gray-300">
                    {/* <button className="flex items-center justify-center p-1" onClick={handleClick}><FcGoogle className=" text-xl mx-3.5"/>
                    Continue with Google</button> */}
                </div>
                <div className="items-center justify-center w-full my-16 font-semibold " style={{ display: 'flex', alignItems: 'center' }}>
                    {/* <div style={{ flex: '1', borderTop: '1px solid black' }}></div>
                    <span style={{ margin: '0 10px' }}>or</span>
                    <div style={{ flex: '1', borderTop: '1px solid black' }}></div> */}
                    <span style={{ margin: '0 10px' }}>Enter New Password</span>
                </div>
                <div className="w-full">
                    <form className="flex flex-col items-center justify-center w-full" onSubmit={handleSubmit}>
                        {error && <div className="w-full p-2 mb-6 text-sm text-center text-white bg-red-500 rounded">{error}</div>}
                        <div className="flex flex-col w-full pb-4 font-light items-right justify-right">Enter new Password
                            <input className={classes} name="password" type="password" value={username}  onChange={onChange}/>
                        </div>
                        <div className="flex flex-col w-full pb-10 font-light justify-right items-right">Confirm new Password
                            <input className={classes} name="password" type="password" value={password} onChange={onChange}/>
                        </div>
                        <SubmitButton type="submit">Change Password</SubmitButton>
                    </form>
                </div>
                {/* <div className="text-sm text-slate-500 mt-7">Don't have an account?</div>
                <div className="mt-2 text-sm text-cyan-600"><Link to="/register">Create account</Link></div> */}
            </div>
        </div>
    )
}
export default Login;