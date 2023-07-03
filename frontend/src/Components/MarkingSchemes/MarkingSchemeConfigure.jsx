import classnames from 'classnames'
import { AiOutlinePlus } from "react-icons/ai";
import { BiFilter } from "react-icons/bi";
import { useState } from 'react'
import MakingSchemeConfigureBox from './MakingSchemeConfigureBox'
function MarkingSchemeConfigure({clicked, data}) {
  const [formData, setFormData] = useState([]);

  const handleFormSubmit = () => {
    // Submit the form data
    console.log(formData);
  };

  const handleFormChange = (index, childFormData) => {
    // Update the form data for the specific child component
    const updatedFormData = [...formData];
    updatedFormData[index] = childFormData;
    setFormData(updatedFormData);
    console.log(updatedFormData);
  };

   const data1 = {
    field1: 'Value 1',
    field2: 'Value 2',
    field3: 'Value 3',
    field4: 'Value 4',
  };

  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');
  // const markingSchemas =JSON.stringify(data);
//   if(data){
//     console.log("DATA:"+data)
//     console.log("DATA:"+data.id)
//   }
//   else{
//     console.log("DATAs:"+data)
//   }
  return (
    <div className={`${classes} ${clicked === 'outer' ? 'ml-16 outer' : 'ml-64 inner '} max-sm:ml-16`}>
        <div className=' flex flex-col items-center justify-top w-full h-fit px-10 max-sm:px-4 py-8'>
            <div className='mb-12 text-center  w-full'>
              <p className='text-xl font-bold text-[#191854]'>Marking scheme</p>
              <p className='text-lg text-black opacity-80 text-center'>Check your marcking scheme and deselect the unnecessary answers</p>
            </div>
            <MakingSchemeConfigureBox key="1" index="1" formData={data1} onChange={handleFormChange}/>
        </div>
        <div className='w-full flex justify-center'>
            <button onClick={handleFormSubmit}className='rounded-[5px] w-52 bg-[#4457FF] text-white font-bold p-1 px-4 cursor-pointer ' >Submit</button>
        </div>
    </div>
  )
}

export default MarkingSchemeConfigure
