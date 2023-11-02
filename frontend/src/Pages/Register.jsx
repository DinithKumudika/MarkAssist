import React,{useState} from 'react';
import { Link , useNavigate } from 'react-router-dom';
import { FcGoogle } from "react-icons/fc";
import Logo from '../photos/loginLogo.png'
// import input from '../Components/input';
import SubmitButton from '../Components/SubmitButton';
import classnames from 'classnames';
import axios from 'axios';
function Register(){
    const navigate = useNavigate();

    const classes= classnames('rounded shadow shadow-gray-400 w-full h-9 p-2 mb-4');

    const handleClick=()=>{
        alert("clicked");
    }

    const [formData, setFormData] = useState({
        firstName: '',
        lastName: '',
        studentIndex: '',
        email: '',
        password: '',
        userType: 'student',
        confirmPassword: '',
        emailActive : false,
        isDeleted : false,
    });
    
    const [error, setError] = useState();

    const { firstName, lastName,studentIndex, email, password, confirmPassword } = formData;


    const onChange = (e) => {
        setFormData((prevState) => ({
          ...prevState,
          [e.target.name]: e.target.value,
        }))
    }
    const handleSubmit = async (event)=>{
        event.preventDefault();
        if(password !== confirmPassword){
            setError("Passwords do not match");
        }else{
            // console.log(formData);
            const formdata = new FormData();
            formdata.append('firstName', formData.firstName);
            formdata.append('lastName', formData.lastName);
            formdata.append('studentIndex', formData.studentIndex);
            formdata.append('email', formData.email);
            formdata.append('password', formData.password);
            formdata.append('userType', 'student');
            formdata.append('emailActive', false);
            formdata.append('isDeleted', false);
            try{
                const response = await axios.post('/auth/register?type=student',formData);
                console.log(response.data); 
                navigate('/login');
            }catch(error){
                console.log("error:"+error.response.data.message);
                if(error.response && error.response.status >=400 && error.response.status <=500){
                    console.log("ERRORR:::",error.response.data);
                    setError("Invalid fields!");
                }
            }
        }
        
    }

    return (
        <div className=" flex justify-center items-center h-full">
            <div className="flex flex-col items-center rounded rounded-sm shadow shadow-gray-400 w-96 h-fit py-5 pb-10 px-10">
                <div className="w-5/12 mb-10 mt-10"><img src={Logo} alt="Logo"/></div>
                {/* <div className="flex items-center  rounded rounded-sm w-3/4 shadow shadow-gray-300">
                    <button className="flex items-center justify-center p-1" onClick={handleClick}><FcGoogle className=" text-xl mx-3.5"/>
                    Continue with Google</button>
                </div>
                <div className="w-full my-5" style={{ display: 'flex', alignItems: 'center' }}>
                  <div style={{ flex: '1', borderTop: '1px solid black' }}></div>
                  <span style={{ margin: '0 10px' }}>or</span>
                  <div style={{ flex: '1', borderTop: '1px solid black' }}></div>
                </div> */}
                <div className="w-full">
                    <form className="flex flex-col items-center justify-center w-full" action="" onSubmit={handleSubmit}>
                        {error && <div className="bg-red-500 text-white text-sm mb-2 w-full p-2 rounded text-center mb-6">{error}</div>}
                        <input className={classes} type="text" name="firstName" placeholder="First Name" value={firstName} onChange={onChange}/>
                        <input className={classes} type="text" name="lastName" placeholder="Last Name" value={lastName} onChange={onChange}/>
                        <input className={classes} type="text" name="studentIndex" placeholder="Index No." value={studentIndex} onChange={onChange}/>
                        <input className={classes} type="email" name="email" placeholder="Email" value={email} onChange={onChange}/>
                        {/* <select value={userType} onChange={handleUserTypeChange} className='rounded shadow shadow-gray-400 w-full h-9 p-2 mb-4'>
                          <option value="">Select user type</option>
                          <option value="Lecturer">Lecturer</option>
                          <option value="Student">Student</option>
                        </select> */}
                        <input className={classes} type="password" name="password" placeholder="Password" value={password} onChange={onChange}/>
                        <input className={classes} type="password" name="confirmPassword" placeholder="Confirm password" value={confirmPassword} onChange={onChange}/>
                        <SubmitButton type="submit">Continue</SubmitButton>
                    </form>
                </div>
            </div>
        </div>
    )
}
export default Register;