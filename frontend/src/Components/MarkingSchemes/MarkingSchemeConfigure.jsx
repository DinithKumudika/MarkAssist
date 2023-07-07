import classnames from 'classnames'
import { AiOutlinePlus } from "react-icons/ai";
import { BiFilter } from "react-icons/bi";
import { useState } from 'react'
import MakingSchemeConfigureBox from './MakingSchemeConfigureBox'
import axios from 'axios'
function MarkingSchemeConfigure({clicked, data,subjectId}) {
  const [formData, setFormData] = useState([]);

  const handleFormSubmit = () => {
    // Submit the form data
    console.log(formData);
    // axios
    // .put(`http://127.0.0.1:8000/api_v1/markings/update/${subjectId}`,formData)
    // .then((response)=>{
    //   console.log(response);
    // })
    // .catch((error) => {
    //   console.error(error);
    //   // Handle the error, e.g., display an error message to the user
    // });
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
              <p className='text-xl font-bold text-custom-blue-3'>Marking scheme</p>
              <p className='text-lg text-black opacity-80 text-center'>Check your marcking scheme and deselect the unnecessary answers</p>
            </div>
            {/* <MakingSchemeConfigureBox key="1" index="1" formData={data1} onChange={handleFormChange}/> */}
            {markings}
        </div>
        <div className='w-full flex justify-center'>
            <button onClick={handleFormSubmit}className='rounded-[5px] w-52 bg-[#4457FF] text-white font-bold p-1 px-4 cursor-pointer ' >Submit</button>
        </div>
    </div>
  )
}

export default MarkingSchemeConfigure
