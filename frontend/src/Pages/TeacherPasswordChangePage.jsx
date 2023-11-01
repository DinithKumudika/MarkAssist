import React,{useState} from 'react';
import { Link, useNavigate , useParams} from 'react-router-dom';
import { FcGoogle } from "react-icons/fc";
import Logo from '../photos/loginLogo.png'
import InputField from '../Components/InputField';
import SubmitButton from '../Components/SubmitButton';
import classnames from 'classnames';
// import { AuthContext } from '../Contexts/AuthContext';
import axios from 'axios';
import jwt_decode from "jwt-decode";
function TeacherPasswordChangePage(){
    const { token } = useParams();
    const navigate = useNavigate();

    const classes= classnames('rounded shadow shadow-gray-400 w-full h-9 p-2 my-3');

    // const {auth, setAuth} = useContext(AuthContext)

    const [formData , setFormData] = useState({
        password: '',
        confirmpassword: '',
    });

    const { password ,confirmpassword} = formData;

    const [error, setError] = useState();

    const onChange =(event) =>{
        setFormData((prevState)=>({
            ...prevState,
            [event.target.name]: event.target.value
        }))
    }

    const handleSubmit = async (event)=>{
        event.preventDefault();
        if(password === confirmpassword){
        // console.log(formData);
        const loginData = new FormData();
        // loginData.append('username', formData.username);
        loginData.append('password', formData.password);
        console.log(formData)
        axios
        .post(`/auth/complete-registration/${token}`,{password:formData.password})
        .then((response)=>{
            navigate('/');
        })
        .catch((error) => {
            console.error(error);
            // setMarks(null)
            // Handle the error, e.g., display an error message to the user
            setError(error.response.data.message);
          });
        }else{
            setError("Passwords do not match")
        }
    }


    return (
        <div className="flex items-center justify-center h-full bg-sky-100">
            <div className="flex flex-col items-center h-screen justify-center px-10 py-10 rounded-sm shadow shadow-gray-600 w-[500px] bg-sky-50 max-sm:w-[350px]">
                <div className="w-5/12 my-5"><img src={Logo} alt="Logo"/></div>
                <div className="items-center justify-center w-full font-semibold mb-5" style={{ display: 'flex', alignItems: 'center' }}>
                    Enter New Password
                </div>
                <div className="w-full">
                    <form className="flex flex-col items-center justify-center w-full" onSubmit={handleSubmit}>
                        {error && <div className="w-full p-2 mb-6 text-sm text-center text-white bg-red-500 rounded">{error}</div>}
                        {/* <div className="flex flex-col w-full pb-4 font-light items-right justify-right mb-5">Enter new Password */}
                            <input className={classes} name="password" type="password" value={password}  placeholder='Enter new Password' onChange={onChange}/>
                        {/* </div> */}
                        {/* <div className="flex flex-col w-full pb-10 font-light justify-right items-right">Confirm new Password */}
                            <input className={classes} name="confirmpassword" type="password" placeholder='Confirm new Password' value={confirmpassword} onChange={onChange}/>
                        {/* </div> */}
                        <SubmitButton classes="mt-5" type="submit">Change Password</SubmitButton>
                    </form>
                </div>
                {/* <div className="text-sm text-slate-500 mt-7">Don't have an account?</div>
                <div className="mt-2 text-sm text-cyan-600"><Link to="/register">Create account</Link></div> */}
            </div>
        </div>
    )
}
export default TeacherPasswordChangePage;