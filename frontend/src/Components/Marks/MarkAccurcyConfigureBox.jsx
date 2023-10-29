import { useState } from "react";

function MarkAccurcyConfigureBox({handleAddChild,handleRemoveChild,index,data,add, Minus,handleFormChange}) {
  // let colorMax = "bg-custom-gray-1";
  const [colorMax,setColorMax] = useState("");
  const [colorMarks,setColorMarks] = useState("");
  const handleClick = (event) => {
    const val = event.target.value
    console.log("VAL:::"+val)
    if(val==="+"){
      // console.log("+",index)
      handleAddChild(index);
    }else if(val==="-"){
      // console.log("-",index)
      handleRemoveChild(index);
    }
  }

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    const updatedFormData = { ...data, [name]: parseInt(value) };
    if((updatedFormData[name]>100) || (updatedFormData[name] <= 0)){
      console.log("error")
      if(name==="maximum"){
        setColorMax("border-2 border-red-500");
      }else if(name==="percentageOfMarks"){
      // console.log(updatedFormData[name])
        setColorMarks("border-2 border-red-500");
      }
    
      // console.log(updatedFormData)
    }else{
      if(name==="maximum"){
        setColorMax("border-2 border-green-500");
      }else if(name==="percentageOfMarks"){
      // console.log(updatedFormData[name])
        setColorMarks("border-2 border-green-500");
      }
    }
    handleFormChange(index, updatedFormData);
  }
  return (
    <div className="flex flex-row justify-between mb-2">
      <input min="0" max="100" className={`w-[150px] bg-custom-gray-1 text-center rounded py-1 mr-2 max-md:w-[60px]`} type="number" name="minimum" value={data.minimum} disabled/>
      <input min="0" max="100" onChange={handleInputChange} className={`w-[150px]  bg-custom-gray-1 text-center rounded py-1 mr-2 max-md:w-[75px]  ${colorMax}`} type="number" name="maximum" value={data.maximum}/>
      <input min="0" max="100" onChange={handleInputChange} className={`w-[150px] bg-custom-gray-1 text-center rounded py-1 mr-2 max-md:w-[60px] ${colorMarks}`} type="number" name="percentageOfMarks" value={data.percentageOfMarks}/>
      <div onClick={handleClick} className="flex items-center">
      <input onClick={handleClick} onChange={handleInputChange} className="hover:cursor-pointer bg-custom-gray-1 text-center rounded py-1 w-[36px] font-bold mr-2" type="button" name="" value={add}  />
      <input onClick={handleClick} onChange={handleInputChange} className="hover:cursor-pointer bg-custom-gray-1 text-center rounded py-1 w-[36px] font-bold" type="button" name="" value={Minus}  />
      </div>
    </div>
  )
}

export default MarkAccurcyConfigureBox
