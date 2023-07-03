import { useState,useRef,useCallback } from 'react';
import {useDropzone} from 'react-dropzone';
import { AiOutlinePlus, AiOutlineClose,AiOutlineUpload} from "react-icons/ai";
import  ReactDOM  from 'react-dom';
import { Link ,useLocation, useParams } from 'react-router-dom';
import axios from 'axios'
import Button from '../Button';
import SubmitButton from '../SubmitButton';
function SubjectAddBox({closeFunc}) {
    
    const currentYear = new Date().getFullYear();

    const [error, setError] = useState();
    const [formData , setFormData] = useState({
        subjectCode: '',
        subjectStream: 'IS',
        subjectName: '',
        subjectYear: `${currentYear-1}/${currentYear}`,
        assignmentMarks: '',
        semester: 1,
        paperMarks: '',
        editingTeacher: 'saman',
        nonEditingTeacher: 'saman',

    });

    const { subjectCode, subjectStream , subjectName, subjectYear, assignmentMarks, semester, paperMarks, editingTeacher, nonEditingTeacher } = formData;

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
        // console.log(formData);
        if(!formData.subjectCode || !formData.subjectStream || !formData.subjectName || !formData.subjectYear || !formData.assignmentMarks || !formData.semester || !formData.paperMarks || !formData.editingTeacher || !formData.nonEditingTeacher){
            setError("Please fill all the fields");
            console.log("error");
            return;
        }else{
            console.log("no error");
            setError("");
        }
        const formdata = new FormData();
        formdata.append('subjectCode', formData.subjectCode);
        formdata.append('subjectStream', formData.subjectStream);
        formdata.append('subjectName', formData.subjectName);
        formdata.append('subjectYear', formData.subjectYear);
        formdata.append('semester', formData.semester);
        formdata.append('assignmentMarks', formData.assignmentMarks);
        formdata.append('paperMarks', formData.paperMarks);
        formdata.append('editingTeacher', formData.editingTeacher);
        formdata.append('nonEditingTeacher', formData.nonEditingTeacher);
        // try{
        //     // const response = await axios.post('http://127.0.0.1:8000/api_v1/auth/token',formdata);
           
        //     // navigate('/subjects');
        // }catch(error){
        //     // console.log("error:"+error.response.data.message);
        //     if(error.response && error.response.status >=400 && error.response.status <500){
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
                    <p className='font-bold text-[#191854] text-2xl'>Add a Subject</p>
                    <div className='flex flex-row'>
                        {/* <Button classNames="" onClick={handleSave}></Button> */}
                        <SubmitButton type="submit"  classes="rounded-[5px]">Save</SubmitButton>
                        <Button classNames="ml-4" onClick={closeFunc}>Close</Button>
                    </div>
                </div>
                <div className='border-b-4 w-full'>
                    {error && <div className="bg-red-500 text-white text-sm mb-2 w-full p-2 rounded text-center mb-6">{error}</div>}

                    <p className='font-bold text-blue-950 text-xl mb-8'>Basic Information</p>
                        <div>
                            <div className='flex flex-row items-center justify-between max-md:flex-col'>
                                <div className='max-md:ml-0 max-md:w-[85%] ml-8 w-[45%] flex flex-row items-center mb-8 '>
                                    <label className='mr-4 font-sans w-36'>Subject Code</label>
                                    <select name='subjectStream' className='items-center w-[15%] h-8 text-center shadow shadow-gray-500 rounded ' value={subjectStream} onChange={handleSelectChange}>
                                      <option value="IS" className='text-bold items-center w-[15%] h-8 text-center shadow shadow-gray-500 rounded '>IS</option>
                                      <option value="SCS" className='text-bold items-center w-[15%] h-8 text-center shadow shadow-gray-500 rounded '>SCS</option>
                                      <option value="CS" className='text-bold items-center w-[15%] h-8 text-center shadow shadow-gray-500 rounded '>CS</option>
                                    </select>
                                    <input type="text" value={subjectCode}  onChange={onChange} name="subjectCode" placeholder="SCS2213" className='ml-[1%] w-[49%] h-8  p-2 shadow shadow-gray-500 rounded'/>
                                </div>
                                <div className='max-md:mr-0 max-md:w-[85%] mr-8 w-[45%] flex flex-row items-center mb-8'>
                                    <label className='mr-4 font-sans w-24 max-md:w-36'>Subject Year</label>
                                    <input type="text" value={currentYear} onChange={onChange} name="subjectCode" placeholder="Subject Code" className='w-[65%] h-8  p-2 shadow shadow-gray-500 rounded' disabled/>
                                    {/* <select name='subjectYear' className='items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded ' value={subjectYear} onChange={handleSelectChange}>
                                      <option value={`${currentYear-1}/${currentYear}`} className='text-bold items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded '>{`${currentYear}`}</option>
                                      <option value={`${currentYear}/${currentYear+1}`} className='text-bold items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded '>{`${currentYear}`}</option>
                                    </select> */}
                                </div>
                            </div>
                            <div className='flex flex-row items-center justify-between max-md:flex-col'>
                                <div className='max-md:ml-0 max-md:w-[85%] ml-8 w-[45%] flex flex-row items-center mb-8 '>
                                    <label className='mr-4 font-sans w-36'>Subject Name</label>
                                    <input type="text" value={subjectName} onChange={onChange} name="subjectName" placeholder="Subject Name" className='w-[65%] h-8  p-2 shadow shadow-gray-500 rounded'/>
                                </div>
                                <div className='max-md:mr-0 max-md:w-[85%] mr-8 w-[45%] flex flex-row items-center mb-8'>
                                    <label className='mr-4 font-sans w-24 max-md:w-36'>Semester</label>
                                    {/* <input type="text" onChange={onChange} name="subjectCode" placeholder="Subject Code" className='w-[65%] h-8  p-2 shadow shadow-gray-500 rounded'/> */}
                                    <select name='semester' className='items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded ' value={semester} onChange={handleSelectChange}>
                                      <option value="1" className='text-bold items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded '>1</option>
                                      <option value="2" className='text-bold items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded '>2</option>
                                    </select>
                                </div>
                            </div>
                            <div className='flex flex-row items-center justify-between max-md:flex-col '>
                                <div className='max-md:ml-0 max-md:w-[85%] ml-8 w-[45%] flex flex-row items-center mb-8 '>
                                    <label className='mr-4 font-sans w-36'>Assignment Marks</label>
                                    <input type="text" value={assignmentMarks} onChange={onChange} name="assignmentMarks" placeholder="30" className='w-[65%] h-8  p-2 shadow shadow-gray-500 rounded'/>
                                </div>
                                <div className='max-md:mr-0 max-md:w-[85%] mr-8 w-[45%] flex flex-row items-center mb-8'>
                                    <label className='mr-4 font-sans w-24 max-md:w-36'>Paper Marks</label>
                                    <input type="text" value={paperMarks} onChange={onChange} name="paperMarks" placeholder="70" className='w-[65%] h-8  p-2 shadow shadow-gray-500 rounded'/>
                                </div>
                            </div>
                        </div>
                </div>
                <div className='w-full'>
                    <p className='font-bold text-blue-950 text-xl my-4 '>Controller Information</p>
                    {/* <form > */}
                        <div>
                            <div className='flex flex-col items-center justify-center max-md:flex-col '>
                                <div className='max-md:w-[85%] w-[50%] flex flex-row items-center mb-8 justify-between max-md:justify-start'>
                                    <label className='mr-4 font-sans w-36'>Editing Teacher</label>
                                    <select name="editingTeacher" className='items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded ' value={editingTeacher} onChange={handleSelectChange}>
                                      <option value="saman" className='text-bold items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded '>Saman Kumara</option>
                                      <option value="kapila" className='text-bold items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded '>Kapila Senadheera</option>
                                    </select>
                                </div>
                                <div className='max-md:w-[85%] w-[50%] flex flex-row items-center mb-8 justify-between max-md:justify-start'>
                                    <label className='mr-4 font-sans w-36'>Non Editing Teacher</label>
                                    <select name="nonEditingTeacher" className='items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded ' value={nonEditingTeacher} onChange={handleSelectChange}>
                                      <option value="saman" className='text-bold items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded '>Saman Kumara</option>
                                      <option value="kapila" className='text-bold items-center w-[65%] h-8 text-center shadow shadow-gray-500 rounded '>Kapila Senadheera</option>
                                    </select>
                                </div>
                                {/* <Button classNames="text-center w-[50%]">Add Controller</Button> */}
                            </div>
                        </div>
                    {/* </form> */}
                </div>
            </form>
        </div>

      </div>,
    document.querySelector('.modal-container')
  )
}

export default SubjectAddBox
