import classnames from 'classnames'
import { AiOutlinePlus } from "react-icons/ai";
import { BiFilter } from "react-icons/bi";
import { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import MakingSchemeConfigureBox from './MakingSchemeConfigureBox'
import Button from '../Button';
import axios from 'axios'
function MarkingSchemeConfigure({clicked, data,subjectId}) {
  const [formData, setFormData] = useState([]);
  const navigate = useNavigate();
  const handleClose = () => {
    navigate(-1);
  };

  const [showImages, setShowImages] = useState(false);
  const handleIconClick = () => {
    setShowImages((prev) => !prev);
  };

  const handleFormSubmit = () => {
    // Submit the form data
    // console.log("formData:",formData);
    //Filtering out and removing undefined indexes in the formData array
    const definedData = formData.filter((item) => item !== undefined);
    // console.log("DefinedData:",definedData);
    axios
    .put(`http://127.0.0.1:8000/api_v1/markings/update/${subjectId}`,definedData)
    .then((response)=>{
      console.log(response);
      navigate(-1);
    })
    .catch((error) => {
      console.error(error);
      // Handle the error, e.g., display an error message to the user
    });
  };

  const handleFormChange = (index, childFormData) => {
    // Update the form data for the specific child component
    const updatedFormData = [...formData];
    updatedFormData[index] = childFormData;
    setFormData(updatedFormData);
    const updatedData = [...data];
    updatedData[index] = childFormData;
    data[index] = childFormData;
    // console.log(updatedFormData);
  };
  var markings = []
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');
  // const markingSchemas =JSON.stringify(data);
  if(data){
    markings = data.map((marking, index) => (
      <MakingSchemeConfigureBox
        key={marking.id}
        index={index}
        formData={marking}
        onChange={handleFormChange}
        showImages={showImages}
      />
    ));
  }
  else{
    // console.log("DATAs:"+data)
  }
  return (
    <div className={`${classes} ${clicked === 'outer' ? 'ml-16 outer' : 'ml-64 inner '} max-sm:ml-16`}>
        <div className=' flex flex-col items-center justify-top w-full h-fit px-10 max-sm:px-4 py-8'>
            <div className='mb-12 text-center  w-full'>
              <p className='text-xl font-bold text-custom-blue-3'>Marking scheme configure</p>
              <p className='text-lg text-black opacity-80 text-center'>Check your marking scheme and configure</p>
              {
                showImages ? <Button onClick={handleIconClick} classNames="w-24 text-center bg-custom-blue-2 absolute left-[85%] mt-2">Hide All</Button>
                : <Button onClick={handleIconClick} classNames="w-24 text-center bg-custom-blue-2 absolute left-[85%] mt-2">View All</Button>
              }

            </div>
            {/* <MakingSchemeConfigureBox key="1" index="1" formData={data1} onChange={handleFormChange}/> */}
            {markings}
        </div>
        <div className='w-full flex justify-center'>
            {/* <button onClick={handleFormSubmit}className='rounded-[5px] w-52 bg-[#4457FF] text-white font-bold p-1 px-4 cursor-pointer ' >Submit</button> */}
            <Button onClick={handleFormSubmit} classNames="bg-custom-blue-2 mb-2 mr-2">Submit</Button>
            <Button onClick={handleClose} classNames="bg-custom-blue-2 mb-2">Cancel</Button>
        </div>
    </div>
  )
}

export default MarkingSchemeConfigure