import { useState,useRef,useCallback } from 'react';
import {useDropzone} from 'react-dropzone';
import { AiOutlinePlus, AiOutlineClose,AiOutlineUpload} from "react-icons/ai";
import  ReactDOM  from 'react-dom';
import { Link ,useLocation, useParams } from 'react-router-dom';
import axios from 'axios'
import Button from './Button';
import SubmitButton from './SubmitButton';
import { BarLoader } from 'react-spinners';
function TeacherAddBox({closeFunc}) {
    
    const currentYear = new Date().getFullYear();

    const [error, setError] = useState();
    const [adding, setadding] = useState(false);
    const [formData , setFormData] = useState({
        firstName : '',
        lastName : '',
        email : '',
        userType : 'teacher',
        emailActive : false,
        isDeleted : false,
        title : 'Mr.',
        role : 'Lecturer',
        telephoneNumber : '',
    });

    const { firstName,lastName,email,userType,emailActive,isDeleted,title,role ,telephoneNumber} = formData;
    // const telephoneNumber = ''

    const handleSelectChange = (event) =>{
        setFormData((prevState)=>({
            ...prevState,
            [event.target.name]: event.target.value
        }))
        // console.log(formData);

    }

    const onChange =(event) =>{
        setFormData((prevState)=>({
            ...prevState,
            [event.target.name]: event.target.value
        }))
        // console.log(formData);
    }

    const handleSubmit = async (event)=>{
        event.preventDefault();
        console.log(formData);
        if(!formData.role || !formData.title || !formData.firstName || !formData.lastName || !formData.email || !formData.telephoneNumber ){
            setError("Please fill all the fields");
            console.log("error");
            return;
        }else{
            console.log("no error");
            console.log(formData);
            const formdata = new FormData();
            // formdata.append('subjectCode', formData.subjectCode);
            axios
            .post('http://127.0.0.1:8000/api_v1/auth/register?type=teacher',formData)
            .then((response) => {
                // console.log("Hello:",response);
                window.location.reload();
                setadding(false);
                closeFunc()
                })
                .catch((error) => {
                  if(error.response && error.response.status >=400 && error.response.status <=500){
                    // console.log(error.response.data.message);
                    console.log(error.response.data.detail);
                    setError(error.response.data.detail);
                }
                });
            setError("");
        }
        // try{
        //     // const response = await axios.post('http://127.0.0.1:8000/api_v1/auth/token',formdata);
           
        //     // navigate('/subjects');
        // }catch(error){
        //     // console.log("error:"+error.response.data.message);
        //     if(error.response && error.response.status >=400 && error.response.status <=500){
        //         // console.log(error.response.data.message);
        //         setError(error.response.data.message);
        //     }
        // }
    }

    return ReactDOM.createPortal(
        <div className='w-[95%]'>
        <div className='z-30 fixed inset-0 bg-gray-300 opacity-80' onClick={closeFunc}></div>
        <div className='shadow shadow-gray-500 z-30 absolute top-[15%] left-[4%] h-fit w-[92%] px-2 pb-5 bg-white  flex flex-col items-center max-lg:left-[2%] max-lg:w-[98%]'>
            <form className='w-full pl-2' onSubmit={handleSubmit}>

                <div className='border-b-4 py-4 w-full flex justify-between'>
                    <p className='font-bold text-[#191854] text-2xl'>Add a Person</p>
                    <div className='flex flex-row'>
                        {/* <Button classNames="" onClick={handleSave}></Button> */}
                        <SubmitButton type="submit" classes="rounded-[5px]">Save</SubmitButton>
                        <Button classNames="ml-4" onClick={closeFunc}>Close</Button>
                    </div>
                </div>
                <div className='border-b-4 w-full'>
                    {error && <div className="bg-red-500 text-white text-sm mb-2 w-full p-2 rounded text-center mb-6">{error}</div>}

                    <p className='font-bold text-blue-950 text-xl mb-8'>Basic Information</p>
                        <div>
                            <div className='flex flex-row items-center justify-between max-md:flex-col'>
                                <div className='max-md:ml-0 max-md:w-[85%] ml-8 w-[45%] flex flex-row items-center mb-8 '>
                                    <label className='mr-4 font-sans w-24 max-md:w-36'>First Name</label>
                                    <select name='title' className='items-center w-[15%] h-8 text-center shadow shadow-gray-500 rounded ' value={title} onChange={handleSelectChange}>
                                      <option value="Dr" className='font-bold items-center w-[15%] h-8 text-center shadow shadow-gray-500 hover:text-black '>Dr</option>
                                      <option value="Prof" className='font-bold items-center w-[15%] h-8 text-center shadow shadow-gray-500 hover:text-black '>Prof</option>
                                      <option value="Mr" className='font-bold items-center w-[15%] h-8 text-center shadow shadow-gray-500 hover:text-black '>Mr</option>
                                      <option value="Mrs" className='font-bold items-center w-[15%] h-8 text-center shadow shadow-gray-500 hover:text-black '>Mrs</option>
                                      <option value="Ms" className='font-bold items-center w-[15%] h-8 text-center shadow shadow-gray-500 hover:text-black '>Ms</option>
                                    </select>
                                    <input type="text" value={firstName} onChange={onChange} name="firstName" placeholder="First Name" className='ml-[1%] w-[49%] h-8  p-2 shadow shadow-gray-500 rounded'/>
                                </div>
                                <div className='max-md:mr-0 max-md:w-[85%] mr-8 w-[45%] flex flex-row items-center mb-8'>
                                    <label className='mr-4 font-sans w-36'>Last Name</label>
                                    <input type="text" value={lastName} onChange={onChange} name="lastName" placeholder="Last Name" className='w-[65%] h-8  p-2 shadow shadow-gray-500 rounded'/>
                                    {/* <select name='subjectYear' className='items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded ' value={subjectYear} onChange={handleSelectChange}>
                                      <option value={`${currentYear-1}/${currentYear}`} className='font-bold items-center w-[65%] h-8 text-center shadow shadow-gray-500 hover:text-black '>{`${currentYear}`}</option>
                                      <option value={`${currentYear}/${currentYear+1}`} className='font-bold items-center w-[65%] h-8 text-center shadow shadow-gray-500 hover:text-black '>{`${currentYear}`}</option>
                                    </select> */}
                                </div>
                            </div>
                            <div className=' flex flex-row items-center justify-between max-md:flex-col'>
                                <div className='max-md:ml-0 max-md:w-[85%] ml-8 w-[45%] flex flex-row items-center mb-8 '>
                                    <label className='mr-4 font-sans w-24 max-md:w-36'>Email</label>
                                    <input type="email" value={email} onChange={onChange} name="email" placeholder="Email" className='w-[65%] h-8  p-2 shadow shadow-gray-500 rounded'/>
                                </div>
                                <div className='max-md:mr-0 max-md:w-[85%] mr-8 w-[45%] flex flex-row items-center mb-8'>
                                    <label className='mr-4 font-sans w-36'>Telephone No.</label>
                                    <input type="text" pattern="[0][0-9]{9}" value={telephoneNumber} onChange={onChange} name="telephoneNumber" placeholder="0123456789" className='w-[65%] h-8  p-2 shadow shadow-gray-500 rounded'/>
                                </div>
                            </div>
                            <div className='flex flex-row items-center justify-between max-md:flex-col '>
                                <div className=' max-md:ml-0 max-md:w-[85%] ml-8 w-[100%] flex flex-row items-center  justify-center mb-8 max-md:justify-start  '>
                                    <label className='mr-4 font-sans w-24 max-md:w-36'>Role</label>
                                    <select name='role' className='max-md:w-[65%] items-center w-[30%] h-8 text-center shadow shadow-gray-500 rounded ' value={role} onChange={handleSelectChange}>
                                      <option value="Lecturer" className='max-md:w-[65%] font-bold items-center w-[30%] h-8 text-center shadow shadow-gray-500 hover:text-black '>Lecturer</option>
                                      <option value="Assistant Lecturer" className='max-md:w-[65%] font-bold items-center w-[30%] h-8 text-center shadow shadow-gray-500 hover:text-black '>Assistant Lecturer</option>
                                      <option value="Instructor" className='max-md:w-[65%] font-bold items-center w-[30%] h-8 text-center shadow shadow-gray-500 hover:text-black '>Instructor</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                </div>
                <div className='w-full'>
                    <p className='font-bold text-blue-950 text-xl my-4 '>Other Information</p>
                </div>
                {adding && <BarLoader color="#4457FF" height={6} width={128} />}

            </form>
        </div>

      </div>,
    document.querySelector('.modal-container')
  )
}

export default TeacherAddBox
